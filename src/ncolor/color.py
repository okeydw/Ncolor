from __future__ import annotations

import re
from ._config import Config

_ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


class FGC:
    """
    Foreground (text) colors.
    """

    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37
    NONE = 38
    LIGHT_BLACK = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_PURPLE = 95
    LIGHT_CYAN = 96
    LIGHT_WHITE = 97


class BGC:
    """
    Background colors.
    """

    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47
    NONE = 48
    LIGHT_BLACK = 100
    LIGHT_RED = 101
    LIGHT_GREEN = 102
    LIGHT_YELLOW = 103
    LIGHT_BLUE = 104
    LIGHT_PURPLE = 105
    LIGHT_CYAN = 106
    LIGHT_WHITE = 107


class VWC:
    """
    Text styles.
    """

    NONE = 0
    BOLD = 1
    DIM = 2
    UNDERLINED = 4
    RARE_BLINK = 5
    OFTEN_BLINK = 6
    REVERSE = 7
    HIDDEN = 8


class Color:

    @staticmethod
    def c(
        text: str,
        fg: int | None = None,
        bg: int | None = None,
        view: int = 0,
        reset: bool | None = None,
    ) -> str:
        """
        Apply ANSI color and style.

        :param text: Input text
        :param fg: Foreground color (FGC)
        :param bg: Background color (BGC)
        :param view: Text style (VWC)
        :param reset: Add reset at the end
        :return: ANSI string
        """

        if not isinstance(text, str) or not Config.color:
            return text

        codes = []
        if view:
            codes.append(str(view))
        if fg is not None:
            codes.append(str(fg))
        if bg is not None:
            codes.append(str(bg))

        if not codes:
            return text

        code = f"\033[{';'.join(codes)}m{text}"

        if reset if reset is not None else Config.autoreset:
            code += "\033[0m"

        return code

    @staticmethod
    def rgb(
        text: str,
        fg: tuple[int, ...] | list[int] | None = None,
        bg: tuple[int, ...] | list[int] | None = None,
        view: int = 0,
        reset: bool | None = None,
    ) -> str:
        """
        Apply RGB color.

        :param text: Input text
        :param fg: Foreground (r, g, b)
        :param bg: Background (r, g, b)
        :param view: Text style (VWC)
        :param reset: Add reset at the end
        :return: ANSI string
        """

        if not isinstance(text, str) or not Config.color:
            return text

        string = str(view) if view else ""

        if fg is not None:
            try:
                r = fg[0] if len(fg) > 0 else 0
                g = fg[1] if len(fg) > 1 else 0
                b = fg[2] if len(fg) > 2 else 0
                string += f";38;2;{r};{g};{b}"
            except (TypeError, IndexError, AttributeError):
                pass

        if bg is not None:
            try:
                r = bg[0] if len(bg) > 0 else 0
                g = bg[1] if len(bg) > 1 else 0
                b = bg[2] if len(bg) > 2 else 0
                string += f";48;2;{r};{g};{b}"
            except (TypeError, IndexError, AttributeError):
                pass

        if not string:
            return text

        code = f"\033[{string.lstrip(';')}m{text}"
        return (
            code + "\033[0m"
            if (reset if reset is not None else Config.autoreset)
            else code
        )

    @staticmethod
    def strip_ansi(text: str) -> str:
        """
        Remove ANSI codes.

        :param text: Input text
        :return: Clean string
        """
        if not isinstance(text, str):
            return text
        return _ANSI_ESCAPE.sub("", text)
