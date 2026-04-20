class Config:
    color = True
    cursor = True
    debug = True
    autoreset = True
    cursor_write = False


def init(
    autoreset: bool = True,
    cursor_write: bool = False,
    color: bool | None = None,
    cursor: bool | None = None,
    debug: bool | None = None,
) -> None:
    """
    Init.
    """
    if color is not None:
        Config.color = color
    if cursor is not None:
        Config.cursor = cursor
    if debug is not None:
        Config.debug = debug

    Config.autoreset = autoreset
    Config.cursor_write = cursor_write

    if Config.color or Config.cursor:
        try:
            from ._platform import enable_windows_vt, setup_utf8

            enable_windows_vt()
            setup_utf8()
        except Exception:
            pass
