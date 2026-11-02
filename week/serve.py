#!/usr/bin/env python3
"""Serve the typical-week view. Standard library only.

    python3 week/serve.py            # then open http://localhost:8737
    python3 week/serve.py 9000       # other port

The page re-reads typical-week.txt every couple of seconds, so save in vim
and the Firefox tab updates on its own.
"""
import json
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "typical-week.txt"
PAGE = ROOT / "index.html"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8737

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
COMMENT = re.compile(r"(?:^|\s)#(?:\s|$)")
CAT = re.compile(r"^@cat\s+(\S+)\s+(#[0-9a-fA-F]{6})\s+(.+)$")
DAY = re.compile(r"^@day\s+(\S+)\s+(.+)$")
ITEM = re.compile(r"^(\S+)\s+(\d{1,2}):(\d\d)-(\d{1,2}):(\d\d)\s+(\S+)\s*(.*)$")


def expand_days(spec):
    """'Mon-Fri', 'Sat,Sun', 'Tue' -> list of day indexes."""
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(DAYS.index(a), DAYS.index(b) + 1))
        else:
            out.append(DAYS.index(part))
    return out


def parse(text):
    cats, items, errors = [], [], []
    day_tags = {}  # day index -> list of tags, e.g. {1: ["office"]}
    for n, raw in enumerate(text.splitlines(), 1):
        line = COMMENT.split(raw, 1)[0].rstrip()
        if not line.strip():
            continue
        mark = ""
        if line[:2] in ("+ ", "- "):
            mark, line = line[0], line[2:]
        line = line.strip()

        if line.startswith("@cat"):
            m = CAT.match(line)
            if m:
                cats.append({"id": m[1], "color": m[2], "name": m[3].strip()})
            else:
                errors.append(f"line {n}: bad @cat: {raw.strip()}")
            continue

        if line.startswith("@day"):
            m = DAY.match(line)
            try:
                for d in expand_days(m[1]):
                    day_tags.setdefault(d, []).append(m[2].strip())
            except (TypeError, ValueError):
                errors.append(f"line {n}: bad @day (use: @day Tue,Thu office)")
            continue

        m = ITEM.match(line)
        if not m:
            errors.append(f"line {n}: can't read: {raw.strip()}")
            continue
        try:
            days = expand_days(m[1])
        except ValueError:
            errors.append(f"line {n}: bad day '{m[1]}' (use Mon..Sun, Mon-Fri, Sat,Sun)")
            continue
        start = int(m[2]) * 60 + int(m[3])
        end = int(m[4]) * 60 + int(m[5])
        if end <= start:
            errors.append(f"line {n}: end is not after start")
            continue
        if m[6] not in {c["id"] for c in cats}:
            errors.append(f"line {n}: unknown category '{m[6]}' (add an @cat line)")
            continue
        label = m[7].strip()
        tentative = label.endswith("?")
        if tentative:
            label = label[:-1].rstrip()
        for d in days:
            items.append({
                "day": d, "start": start, "end": end, "cat": m[6],
                "label": label, "mark": mark, "tentative": tentative, "line": n,
            })
    return {"cats": cats, "items": items, "days": day_tags, "errors": errors}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send(PAGE.read_bytes(), "text/html; charset=utf-8")
        elif self.path.startswith("/data.json"):
            body = json.dumps(parse(DATA.read_text())).encode()
            self.send(body, "application/json")
        else:
            self.send_error(404)

    def send(self, body, ctype):
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"Typical week: http://localhost:{PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
