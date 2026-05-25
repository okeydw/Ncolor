import sys


def enable_windows_vt() -> None:
    if sys.platform != "win32":
        return
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        h_out = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        if h_out == -1:
            return
        mode = ctypes.c_uint()
        kernel32.GetConsoleMode(h_out, ctypes.byref(mode))
        VT_MODE = 0x0004
        if not (mode.value & VT_MODE):
            kernel32.SetConsoleMode(h_out, mode.value | VT_MODE)
    except Exception:
        pass


def setup_utf8() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
