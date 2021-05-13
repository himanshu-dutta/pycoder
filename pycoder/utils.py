from pycoder.config import BOLD, GREEN, RED, CROSS, END, TICK


def formatter(
    st: str,
    color: str = None,
    bold: bool = False,
    tick: bool = False,
    cross: bool = False,
    at_end: bool = True,
) -> str:
    st = str(st)
    if color:
        color = GREEN if color.lower() == "g" else RED
    else:
        color = ""

    bold = BOLD if bold else ""

    if tick:
        st = st + " " + TICK if at_end else TICK + " " + st

    if cross:
        st = st + " " + CROSS if at_end else CROSS + " " + st

    return color + bold + st + END
