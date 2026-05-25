# `cursor.md` - Cursor & Screen Control

## Class `Cursor`
All coordinates are 1-based (`x` = column, `y` = row).  
Method behavior depends on two global flags:
- `Config.cursor`: If `False`, all methods immediately return `None`, completely disabling output.
- `Config.cursor_write`: If `True`, methods return the ANSI string. If `False`, the string is written to `stdout` with `flush()` and `None` is returned.

### Movement Methods
| Method | Signature | ANSI Code | Description |
|--------|-----------|-----------|-------------|
| `UP` | `UP(n: int = 1) -> str \| None` | `\033[{n}A` | Move cursor up `n` lines. |
| `DOWN` | `DOWN(n: int = 1) -> str \| None` | `\033[{n}B` | Move cursor down `n` lines. |
| `FORWARD` | `FORWARD(n: int = 1) -> str \| None` | `\033[{n}C` | Move cursor right `n` columns. |
| `BACK` | `BACK(n: int = 1) -> str \| None` | `\033[{n}D` | Move cursor left `n` columns. |
| `NEXT_LINE` | `NEXT_LINE(n: int = 1) -> str \| None` | `\033[{n}E` | Move to beginning of next line `n` times. |
| `PREV_LINE` | `PREV_LINE(n: int = 1) -> str \| None` | `\033[{n}F` | Move to beginning of previous line `n` times. |
| `COLUMN` | `COLUMN(n: int = 1) -> str \| None` | `\033[{n}G` | Move to column `n` in current row. |
| `POS` | `POS(x: int = 1, y: int = 1) -> str \| None` | `\033[{y};{x}H` | Set absolute position `(x, y)`. |
| `POS_ALT` | `POS_ALT(x: int = 1, y: int = 1) -> str \| None` | `\033[{y};{x}f` | Alternative position setter. Functionally identical to `POS`. |
| `HOME` | `HOME() -> str \| None` | `\033[H` | Move to `(1, 1)`. |

> All numeric parameters are validated via internal `_clamp()`, guaranteeing `value ≥ 1`.

### Screen & Line Clearing
| Method | Signature | ANSI Code | Description |
|--------|-----------|-----------|-------------|
| `CLEAR` | `CLEAR(mode: int = 2) -> str \| None` | `\033[{mode}J` | Clear screen. `mode`: `0` → cursor to end, `1` → start to cursor, `2` → whole screen, `3` → screen + scrollback. Clamped to `[0, 3]`. |
| `CLEAR_LINE` | `CLEAR_LINE(mode: int = 0) -> str \| None` | `\033[{mode}K` | Clear current line. `mode`: `0` → cursor to end, `1` → start to cursor, `2` → whole line. Clamped to `[0, 2]`. |

### Cursor State
| Method | Signature | ANSI Code | Description |
|--------|-----------|-----------|-------------|
| `HIDE` | `HIDE() -> str \| None` | `\033[?25l` | Hide cursor. |
| `SHOW` | `SHOW() -> str \| None` | `\033[?25h` | Show cursor. |
| `SAVE` | `SAVE() -> str \| None` | `\033[s` | Save cursor position & state. |
| `RESTORE` | `RESTORE() -> str \| None` | `\033[u` | Restore saved position & state. |

### Direct Output
| Method | Signature | Description |
|--------|-----------|-------------|
| `write` | `write(*codes: str) -> None` | Joins provided strings with spaces and forces output to `stdout` + `flush()`. Ignores both `Config.cursor` and `Config.cursor_write`. Empty strings are skipped. |

---

**Next:** [Debugging (debug.md)](debug.md)