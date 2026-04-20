import sys
from ._config import Config

class Cursor:
    """
    ANSI cursor.md and screen control.
    All positions are 1-based (x = column, y = row).
    """

    @staticmethod
    def _clamp(value: int, min_val: int = 1, max_val: int | None = None) -> int:
        v = max(min_val, int(value))
        return v if max_val is None else min(v, max_val)

    @staticmethod
    def _output(code: str) -> str | None:
        if Config.cursor:
            if not code:
                return None if Config.cursor_write else ""

            if Config.cursor_write:
                return code

            sys.stdout.write(code)
            sys.stdout.flush()
            return None
        return None

    @staticmethod
    def UP(n: int = 1) -> str | None:
        """
        Move cursor.md up.

        :param n: Number of lines
        :return: ANSI string or None (if cursor_write=True)
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}A")

    @staticmethod
    def DOWN(n: int = 1) -> str | None:
        """
        Move cursor.md down.

        :param n: Number of lines
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}B")

    @staticmethod
    def FORWARD(n: int = 1) -> str | None:
        """
        Move cursor.md right.

        :param n: Number of columns
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}C")

    @staticmethod
    def BACK(n: int = 1) -> str | None:
        """
        Move cursor.md left.

        :param n: Number of columns
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}D")

    @staticmethod
    def NEXT_LINE(n: int = 1) -> str | None:
        """
        Move cursor.md to next line start.

        :param n: Number of lines
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}E")

    @staticmethod
    def PREV_LINE(n: int = 1) -> str | None:
        """
        Move cursor.md to previous line start.

        :param n: Number of lines
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}F")

    @staticmethod
    def COLUMN(n: int = 1) -> str | None:
        """
        Move cursor.md to column.

        :param n: Column number
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(n)}G")

    @staticmethod
    def POS(x: int = 1, y: int = 1) -> str | None:
        """
        Set cursor.md position.

        :param x: Column
        :param y: Row
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(y)};{Cursor._clamp(x)}H")

    @staticmethod
    def POS_ALT(x: int = 1, y: int = 1) -> str | None:
        """
        Set cursor.md position (alternative).

        :param x: Column
        :param y: Row
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(y)};{Cursor._clamp(x)}f")

    @staticmethod
    def HOME() -> str | None:
        """
        Move cursor.md to (1, 1).

        :return: ANSI string or None
        """
        return Cursor._output("\033[H")

    @staticmethod
    def CLEAR(mode: int = 2) -> str | None:
        """
        Clear screen.

        :param mode:
            0 - cursor.md to end
            1 - start to cursor.md
            2 - whole screen
            3 - screen and scrollback
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(mode, 0, 3)}J")

    @staticmethod
    def CLEAR_LINE(mode: int = 0) -> str | None:
        """
        Clear current line.

        :param mode:
            0 - cursor.md to end
            1 - start to cursor.md
            2 - whole line
        :return: ANSI string or None
        """
        return Cursor._output(f"\033[{Cursor._clamp(mode, 0, 2)}K")

    @staticmethod
    def HIDE() -> str | None:
        """
        Hide the cursor.md.

        :return: ANSI string or None
        """
        return Cursor._output("\033[?25l")

    @staticmethod
    def SHOW() -> str | None:
        """
        Show the cursor.md.

        :return: ANSI string or None
        """
        return Cursor._output("\033[?25h")

    @staticmethod
    def SAVE() -> str | None:
        """
        Save cursor.md state.

        :return: ANSI string or None
        """
        return Cursor._output("\033[s")

    @staticmethod
    def RESTORE() -> str | None:
        """
        Restore cursor.md state.

        :return: ANSI string or None
        """
        return Cursor._output("\033[u")

    @staticmethod
    def write(*codes: str) -> None:
        """
        Write one or more ANSI codes directly to stdout with flush.
        Works regardless of cursor_write mode.

        :param codes: ANSI code strings to write
        """
        combined = "".join(c for c in codes if c)
        if combined:
            sys.stdout.write(combined)
            sys.stdout.flush()
