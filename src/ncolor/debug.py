from ._config import Config


class Debug:
    """
    Debug helpers.
    """

    @staticmethod
    def all_colors(class_type) -> dict[str, int]:
        """
        Get constants from class.

        :param class_type: FGC, BGC or VWC
        :return: dict
        """
        if Config.debug:
            if not hasattr(class_type, "__dict__"):
                return {}

            return {
                name: value
                for name, value in vars(class_type).items()
                if not name.startswith("_") and isinstance(value, int)
            }
        return {}

    @staticmethod
    def test_rgb_color(r: int, g: int, b: int) -> str | None:
        """
        Show RGB color.

        :param r: Red
        :param g: Green
        :param b: Blue
        :return: ANSI string
        """
        if Config.debug:
            code = f"\033[48;2;{r};{g};{b}m"
            return code + "\n" + "\033[0m"
        return None

    @staticmethod
    def all_ansi(text: str) -> str | None:
        """
        Show control characters.

        :param text: Input text
        :return: Visible string
        """

        if Config.debug:
            return (
                text.replace("\x1b", "<ESC>")
                .replace("\033", "<ESC>")
                .replace("\n", "<LF>")
                .replace("\r", "<CR>")
                .replace("\t", "<TAB>")
            )
        return None
