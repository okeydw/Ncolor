# `color.md` - Colors & Styling

## Constants

### `FGC` (Foreground Colors)
| Constant | Value | Constant | Value |
|----------|-------|----------|-------|
| `BLACK` | `30` | `LIGHT_BLACK` | `90` |
| `RED` | `31` | `LIGHT_RED` | `91` |
| `GREEN` | `32` | `LIGHT_GREEN` | `92` |
| `YELLOW` | `33` | `LIGHT_YELLOW` | `93` |
| `BLUE` | `34` | `LIGHT_BLUE` | `94` |
| `PURPLE` | `35` | `LIGHT_PURPLE` | `95` |
| `CYAN` | `36` | `LIGHT_CYAN` | `96` |
| `WHITE` | `37` | `LIGHT_WHITE` | `97` |
| `NONE` | `38` | | |

### `BGC` (Background Colors)
| Constant | Value | Constant | Value |
|----------|-------|----------|-------|
| `BLACK` | `40` | `LIGHT_BLACK` | `100` |
| `RED` | `41` | `LIGHT_RED` | `101` |
| `GREEN` | `42` | `LIGHT_GREEN` | `102` |
| `YELLOW` | `43` | `LIGHT_YELLOW` | `103` |
| `BLUE` | `44` | `LIGHT_BLUE` | `104` |
| `PURPLE` | `45` | `LIGHT_PURPLE` | `105` |
| `CYAN` | `46` | `LIGHT_CYAN` | `106` |
| `WHITE` | `47` | `LIGHT_WHITE` | `107` |
| `NONE` | `48` | | |

### `VWC` (View/Style Codes)
| Constant | Value | Description |
|----------|-------|-------------|
| `NONE` | `0` | No style |
| `BOLD` | `1` | Bold |
| `DIM` | `2` | Dim |
| `UNDERLINED` | `4` | Underlined |
| `RARE_BLINK` | `5` | Slow blink |
| `OFTEN_BLINK` | `6` | Rapid blink |
| `REVERSE` | `7` | Invert foreground/background |
| `HIDDEN` | `8` | Hidden text |

> ⚠️ All color methods immediately return raw `text` if `Config.color == False`. Styles can be combined via bitwise OR: `VWC.BOLD | VWC.UNDERLINED`.

---

## `Color.c()`
Applies standard ANSI colors and text styles.

### Signature
```python
@staticmethod
def c(
    text: str,
    fg: int | None = None,
    bg: int | None = None,
    view: int = 0,
    reset: bool | None = None,
) -> str:
```

### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | — | Input string. Non-strings are returned as-is. |
| `fg` | `int \| None` | `None` | Foreground color code from `FGC`. |
| `bg` | `int \| None` | `None` | Background color code from `BGC`. |
| `view` | `int` | `0` | Style code from `VWC`. |
| `reset` | `bool \| None` | `None` | Force append `\033[0m`. Falls back to `Config.autoreset` if `None`. |

### Behavior
- Returns `text` immediately if `view == 0`, `fg is None`, and `bg is None`.
- Constructs SGR sequence: `\033[<view>;<fg>;<bg>m<text>`. Omitted parameters are excluded.
- Appends reset sequence if `reset is True` or (`reset is None` and `Config.autoreset is True`).

---

## `Color.rgb()`
Applies TrueColor (24-bit RGB) formatting.

### Signature
```python
@staticmethod
def rgb(
    text: str,
    fg: tuple[int, ...] | list[int] | None = None,
    bg: tuple[int, ...] | list[int] | None = None,
    view: int = 0,
    reset: bool | None = None,
) -> str:
```

### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | — | Input string. Non-strings are returned as-is. |
| `fg` | `tuple \| list \| None` | `None` | `(r, g, b)` for foreground. Missing indices default to `0`. Invalid types are silently ignored. |
| `bg` | `tuple \| list \| None` | `None` | `(r, g, b)` for background. Same fallback/ignore rules as `fg`. |
| `view` | `int` | `0` | Style code from `VWC`. |
| `reset` | `bool \| None` | `None` | Force append `\033[0m`. Falls back to `Config.autoreset` if `None`. |

### Behavior
- Builds extended SGR sequences: `38;2;<r>;<g>;<b>` (foreground) and `48;2;<r>;<g>;<b>` (background).
- If both `fg` and `bg` fail to parse or are `None`, returns raw `text`.
- Reset logic matches `Color.c()`.

---

## `Color.strip_ansi()`
Removes all ANSI escape sequences from a string.

### Signature
```python
@staticmethod
def strip_ansi(text: str) -> str:
```

### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `str` | Input string. Non-strings are returned unchanged. |

### Behavior
- Matches all CSI/OSC/SGR escape patterns using compiled regex.
- Replaces each match with a single space `" "`.
- Returns the cleaned string.

---

**Next:** [Cursor & Screen Control (cursor.md)](cursor.md)
