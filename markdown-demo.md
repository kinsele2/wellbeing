# Markdown Demo

A reference file showing every markdown element rendered by the current Neovim config
(treesitter + render-markdown.nvim). Open this file in Neovim to see the rendering.

---

## Headings

All six heading levels get distinct visual treatment — colour, weight, and a prefix marker.

# H1 — Top Level
## H2 — Section
### H3 — Subsection
#### H4 — Sub-subsection
##### H5
###### H6 — Smallest

---

## Inline Formatting

Normal prose with **bold text**, *italic text*, and ***bold italic text***.

~~Strikethrough text~~ for deletions or corrections.

Inline `code` renders in a highlighted block.

---

## Horizontal Rules

Three or more hyphens, asterisks, or underscores produce a rule:

---

___

***

---

## Blockquotes

> A single-level blockquote. Useful for callouts, excerpts, or notes.

> Nested blockquotes are supported too.
>> This is a second level.
>>> And a third.

---

## Callouts / Alerts

GitHub-style callouts are rendered with icons and coloured borders.

> [!NOTE]
> Highlights information the reader should take into account.

> [!TIP]
> Optional advice that can help the reader do something better.

> [!WARNING]
> Critical content. The reader should read this before proceeding.

> [!IMPORTANT]
> Key information the reader must know to achieve their goal.

> [!CAUTION]
> Negative potential consequences of an action.

---

## Lists

### Unordered

- First item
- Second item
  - Nested item
  - Another nested item
    - Deeply nested
- Third item

### Ordered

1. First step
2. Second step
   1. Sub-step A
   2. Sub-step B
3. Third step

### Task Lists

Checkboxes are rendered as visual tick/cross symbols.

- [x] Completed task
- [ ] Incomplete task
- [x] Another done item
- [ ] Still to do

---

## Code Blocks

Fenced code blocks get a language label and highlighted background.

```lua
-- Lua: Neovim config example
vim.pack.add { 'https://github.com/MeanderingProgrammer/render-markdown.nvim' }
require('render-markdown').setup {}
```

```bash
# Shell: install neovim
brew install neovim
npm install -g tree-sitter-cli
```

```python
# Python: simple example
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

```java
public static void main(String [] args)
```

```
Plain code block with no language — no syntax highlighting, but still styled.
```

---

## Tables

Tables are rendered with proper borders and aligned columns.

| Feature            | Plugin                  | Status    |
| ------------------ | ----------------------- | --------- |
| Syntax highlighting| nvim-treesitter         | Installed |
| Visual rendering   | render-markdown.nvim    | Installed |
| Fuzzy search       | Telescope               | Installed |
| Autocompletion     | blink.cmp               | Installed |
| LSP support        | nvim-lspconfig + Mason  | Installed |
| Formatting         | conform.nvim            | Installed |

A right-aligned and centre-aligned column example:

| Left-aligned | Centre-aligned | Right-aligned |
| :----------- | :------------: | ------------: |
| Text         |     Text       |          Text |
| More text    |   More text    |     More text |

---

## Links

[An inline link](https://neovim.io) with a label and URL.

[A link with a title](https://neovim.io "Neovim homepage") — hover or LSP shows the title.

Bare URL auto-linked: https://github.com/MeanderingProgrammer/render-markdown.nvim

Reference-style link: [Kickstart.nvim][kickstart]

[kickstart]: https://github.com/nvim-kickstart/kickstart.nvim

---

## Images

Images show an icon placeholder in the terminal (no pixel rendering).

![Neovim logo](https://neovim.io/images/logo@2x.png)

---

## Mixed Inline Styles

These can be combined freely:

- **Bold with `inline code` inside**
- *Italic with a [link](https://neovim.io) inside*
- ~~Strikethrough with **bold** inside~~
- `code` alongside **bold** and *italic* in one sentence
