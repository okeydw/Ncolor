# `debug.md` - Debugging

## Class `Debug`
Helper utilities for visualizing and analyzing ANSI output.  
**Important:** All methods actively check `Config.debug`. If `False`, they return `{}` or `None` immediately without processing.

### `Debug.all_colors()`
Extracts public integer constants from a specified class.

#### Signature
```python
@staticmethod
def all_colors(class_type) -> dict[str, int]:
```

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `class_type` | `type` | Constants class (`FGC`, `BGC`, or `VWC`). |

#### Returns
Dictionary `{attribute_name: value}`. Returns `{}` if `Config.debug == False` or object lacks `__dict__`.

---

### `Debug.test_rgb_color()`
Generates a test string for visual RGB background verification.

#### Signature
```python
@staticmethod
def test_rgb_color(r: int, g: int, b: int) -> str | None:
```

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `r` | `int` | Red (0–255) |
| `g` | `int` | Green (0–255) |
| `b` | `int` | Blue (0–255) |

#### Returns
String formatted as `\033[48;2;<r>;<g>;<b>m\n\033[0m` when debugging is enabled, otherwise `None`.

---

### `Debug.all_ansi()`
Replaces control characters with readable tags for console output inspection.

#### Signature
```python
@staticmethod
def all_ansi(text: str) -> str | None:
```

#### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `str` | Input string containing potential ANSI codes. |

#### Returns
String with replacements: `\x1b`/`\033` → `<ESC>`, `\n` → `<LF>`, `\r` → `<CR>`, `\t` → `<TAB>`. Returns `None` if `Config.debug == False`.

**Start:** [Initialization (other.md)](other.md)