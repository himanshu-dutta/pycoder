from pycoder.imports import Path
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


def update_version():
    version = input("Enter version number: ")
    assert (
        len(version.split(".")) == 3
    ), """version represents RELEASE_VERSION.DEV_VERSION.MODEL_VERSION"""

    version_file = Path(__file__).parent / "version.py"

    with version_file.open("w") as fl:
        fl.write(
            f"""\"\"\"version represents RELEASE_VERSION.DEV_VERSION.MODEL_VERSION\"\"\"\n__version__ = "{version}\"
            """
        )
