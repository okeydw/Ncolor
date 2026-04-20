<div align="center">
  <h1>Ncolor</h1>
  <p><strong>ANSI-библиотека для Python</strong></p>
  
  <p>
    <a href="README.md">
      <img src="https://img.shields.io/badge/English-0073B7?style=flat-square" alt="English version">
    </a>
    <a href="docs/ru/other.md">
      <img src="https://img.shields.io/badge/Документация-6666FF?style=flat-square" alt="Документация">
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

### Возможности

- **Нулевые зависимости** - чистый Python, без внешних пакетов
- **Полная поддержка цветов** - стандартные ANSI-цвета + True RGB (24-bit)
- **Управление курсором и экраном** - перемещение, скрытие, отображение, очистка
- **Гибкий вывод** - режим немедленной записи и паттерн builder
- **Кроссплатформенность** - поддержка Windows, Linux и macOS

---

### Установка

```bash
pip install git+https://github.com/okeydw/Ncolor.git
```

---

### Быстрый старт

```python
from ncolor import init, Cursor, Color, FGC, BGC

init()

# Цветной текст
print(Color.c("Hello from ncolor", fg=FGC.GREEN))

# RGB-цвет
print(Color.rgb("Современный RGB-текст", fg=(80, 200, 255)))

# Управление курсором
Cursor.CLEAR()
Cursor.POS(10, 5)
print(Color.c("Текст в позиции", fg=FGC.CYAN, view=1))
Cursor.SHOW()
```

---

### Примеры использования

#### 1. Базовые цвета и стили

```python
from ncolor import Color, FGC, BGC, VWC

print(Color.c("Жирный красный текст", fg=FGC.RED, view=VWC.BOLD))
print(Color.c("Подчёркнутый текст на синем фоне", 
              fg=FGC.WHITE, bg=BGC.BLUE, view=VWC.UNDERLINED))
```

#### 2. RGB-цвета

```python
from ncolor import Color

print(Color.rgb("Яркий циан", fg=(0, 255, 255)))
print(Color.rgb("Тёмно-фиолетовый фон", bg=(90, 30, 180)))
```

#### 3. Управление курсором и экраном

```python
import time
from ncolor import Cursor, Color, FGC

Cursor.CLEAR()
Cursor.HIDE()

for i in range(11):
    Cursor.POS(5, 5)
    print(Color.c(f"Обработка... {i*10}%", fg=FGC.YELLOW))
    time.sleep(0.2)

Cursor.POS(5, 7)
print(Color.c("Успешно завершено", fg=FGC.GREEN))
Cursor.SHOW()
```

#### 4. Режим Builder

```python
from ncolor import init, Cursor, Color, FGC, VWC

init(cursor_write=True)

output = (
    Cursor.CLEAR() +
    Cursor.POS(30, 10) +
    Color.c("Центрированное сообщение", fg=FGC.PURPLE, view=VWC.BOLD)
)

Cursor.write(output)
```

---

### Обзор API

| Компонент | Описание |
|-----------|----------|
| `Color.c()` | Применение стандартных ANSI-цветов и стилей текста |
| `Color.rgb()` | TrueColor (24-bit RGB) для фона и переднего плана |
| `Cursor` | Перемещение, скрытие, отображение курсора; очистка экрана или строк |
| `FGC` / `BGC` | Предопределённые константы цветов переднего плана и фона |
| `VWC` | Константы стилей: жирный, тусклый, подчёркнутый, мигающий, инвертированный |

---

<div align="center">
  <a href="https://github.com/okeydw/Ncolor/issues">
    <img src="https://img.shields.io/badge/Сообщить_о_проблеме-8A2BE2?style=flat-square" alt="Сообщить о проблеме">
  </a>
  <a href="https://github.com/okeydw/Ncolor">
    <img src="https://img.shields.io/badge/Исходный_код-24292e?style=flat-square&logo=github&logoColor=white" alt="Исходный код">
  </a>
</div>
