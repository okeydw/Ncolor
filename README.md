<div align="center">
  <h1>Ncolor</h1>
  <p><strong>ANSI Library for Python</strong></p>
  
  <p>
    <a href="README-ru.md">
      <img src="https://img.shields.io/badge/Русский-0073B7?style=flat-square" alt="English version">
    </a>
    <a href="docs/en/other.md">
      <img src="https://img.shields.io/badge/Docs-6666FF?style=flat-square" alt="Docs">
    </a>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.8-brightgreen?style=flat-square" alt="Python 3.8">
    <img src="https://img.shields.io/badge/Python-3.9-brightgreen?style=flat-square" alt="Python 3.9">
    <img src="https://img.shields.io/badge/Python-3.10-brightgreen?style=flat-square" alt="Python 3.10">
    <img src="https://img.shields.io/badge/Python-3.11-brightgreen?style=flat-square" alt="Python 3.11">
    <img src="https://img.shields.io/badge/Python-3.12-brightgreen?style=flat-square" alt="Python 3.12">
    <img src="https://img.shields.io/badge/Python-3.13-brightgreen?style=flat-square" alt="Python 3.13">
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Windows-0078D6?style=flat-square" alt="Windows">
    <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
    <img src="https://img.shields.io/badge/macOS-000000?style=flat-square&logo=apple&logoColor=white" alt="macOS">
  </p>
</div>

---

### Features

- **Zero dependencies** - pure Python, no external packages required
- **Full color support** - standard ANSI colors + True RGB (24-bit)
- **Cursor & screen control** - move, hide, show, clear with ease
- **Flexible output** - immediate write mode and builder pattern
- **Cross-platform** - consistent behavior on Windows, Linux, and macOS

---

### Installation

```bash
pip install git+https://github.com/okeydw/Ncolor.git
```

---

### Quick Start

```python
from ncolor import init, Cursor, Color, FGC, BGC

init()

# Colored text
print(Color.c("Hello from ncolor", fg=FGC.GREEN))

# RGB color
print(Color.rgb("Modern RGB text", fg=(80, 200, 255)))

# Cursor control
Cursor.CLEAR()
Cursor.POS(10, 5)
print(Color.c("Positioned text", fg=FGC.CYAN, view=1))
Cursor.SHOW()
```

---

### Usage Examples

#### 1. Basic Colors and Styles

```python
from ncolor import Color, FGC, BGC, VWC

print(Color.c("Bold red text", fg=FGC.RED, view=VWC.BOLD))
print(Color.c("Underlined text on blue background", 
              fg=FGC.WHITE, bg=BGC.BLUE, view=VWC.UNDERLINED))
```

#### 2. RGB Colors

```python
from ncolor import Color

print(Color.rgb("Bright cyan", fg=(0, 255, 255)))
print(Color.rgb("Deep purple background", bg=(90, 30, 180)))
```

#### 3. Cursor & Screen Control

```python
import time
from ncolor import Cursor, Color, FGC

Cursor.CLEAR()
Cursor.HIDE()

for i in range(11):
    Cursor.POS(5, 5)
    print(Color.c(f"Processing... {i*10}%", fg=FGC.YELLOW))
    time.sleep(0.2)

Cursor.POS(5, 7)
print(Color.c("Completed successfully", fg=FGC.GREEN))
Cursor.SHOW()
```

#### 4. Builder Mode

```python
from ncolor import init, Cursor, Color, FGC, VWC

init(cursor_write=True)

output = (
    Cursor.CLEAR() +
    Cursor.POS(30, 10) +
    Color.c("Centered message", fg=FGC.PURPLE, view=VWC.BOLD)
)

Cursor.write(output)
```

---

### API Overview

| Component | Description |
|-----------|-------------|
| `Color.c()` | Apply standard ANSI colors and text styles |
| `Color.rgb()` | TrueColor (24-bit RGB) foreground/background |
| `Cursor` | Move, hide, show cursor; clear screen or lines |
| `FGC` / `BGC` | Predefined foreground and background color constants |
| `VWC` | View constants: bold, dim, underlined, blink, reverse |

---

<div align="center">
  <a href="https://github.com/okeydw/Ncolor/issues">
    <img src="https://img.shields.io/badge/Report_Issue-8A2BE2?style=flat-square" alt="Report Issue">
  </a>
  <a href="https://github.com/okeydw/Ncolor">
    <img src="https://img.shields.io/badge/View_Source-24292e?style=flat-square&logo=github&logoColor=white" alt="Source Code">
  </a>
</div>
