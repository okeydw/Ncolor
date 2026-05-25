# `other.md` - Initialization & Configuration

## `init()`
The entry point for global library configuration. Sets up terminal compatibility and applies runtime settings.

### Signature
```python
def init(
    autoreset: bool = True,
    cursor_write: bool = False,
    color: bool | None = None,
    cursor: bool | None = None,
    debug: bool | None = None,
) -> None:
```

### Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `autoreset` | `bool` | `True` | Always updates `Config.autoreset`. Appends `\033[0m` after formatted text when enabled. |
| `cursor_write` | `bool` | `False` | Always updates `Config.cursor_write`. `False` prints directly to `stdout`, `True` returns ANSI strings. |
| `color` | `bool \| None` | `None` | Updates `Config.color` only if not `None`. `False` disables all color processing. |
| `cursor` | `bool \| None` | `None` | Updates `Config.cursor` only if not `None`. `False` disables all cursor/screen control. |
| `debug` | `bool \| None` | `None` | Updates `Config.debug` only if not `None`. `False` disables debug helpers. |

### Behavior
1. Applies provided values to the global `Config` object.
2. If `Config.color` or `Config.cursor` evaluates to `True`, automatically executes platform compatibility routines:
   - `enable_windows_vt()` — Activates ANSI escape sequence support in Windows consoles via `ctypes`.
   - `setup_utf8()` — Reconfigures `sys.stdout` to UTF-8 encoding.
3. All platform setup exceptions are silently suppressed to ensure stability across non-standard terminals.

### Examples
```python
from ncolor import init

# Default initialization
init()

# Disable colors & debug, enable builder mode for Cursor
init(color=False, debug=False, cursor_write=True)

# Modify only autoreset, leave other settings unchanged
init(autoreset=False)
```

### `Config` Object
All settings are stored in `ncolor._config.Config`. Direct modification is possible but bypasses platform setup triggers:
```python
from ncolor._config import Config

Config.cursor = False      # Disable cursor/screen control
Config.debug = False       # Disable debug helpers
Config.autoreset = False   # Disable automatic style reset
```
> ⚠️ Directly modifying `Config` after `init()` takes effect immediately but **does not** re-trigger `_platform` routines.

---

**Next:** [Colors & Styling (color.md)](color.md)