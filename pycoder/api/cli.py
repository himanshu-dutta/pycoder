from pycoder.api.main import query
from pycoder.utils import formatter
from pycoder.version import __version__
from pycoder.imports import (
    time,
    List,
    echo,
    Exit,
    Typer,
    Option,
    Optional,
    spinner,
    highlight,
    PythonLexer,
    TerminalFormatter,
    system,
)

app = Typer()


def version_callback(value: bool):
    if value:
        echo(f"Pycoder 🐍 CLI version: {__version__}")
        raise Exit()


############################
#   interface for inference
############################


def endpoint_callback(value: bool):
    if value:
        from pycoder.api.app import main

        main()
        raise Exit()


@app.command()
def main(
    topic: List[str] = Option(
        ..., "--topic", "-t", help="topic[s] for the code to be written."
    ),
    description: str = Option(
        ..., "--description", "-d", help="description of the code to be written."
    ),
    prefix: Optional[str] = Option(
        "", "--prefix", "-p", help="starting of the code for pycoder to follow."
    ),
    max_length: Optional[int] = Option(
        200, "--max-length", "-ml", help="max length of code to generate."
    ),
    cuda: Optional[bool] = Option(
        False,
        "--cuda",
        "-c",
        help="if cuda device is to be used for inference or not. Might not work in case VRAM is <4GB.",
    ),
    execution_time: Optional[bool] = Option(
        False,
        "--execution_time",
        "-et",
        help="get execution time of generating the code.",
    ),
    endpoint: Optional[bool] = Option(
        None,
        "--endpoint",
        "-e",
        callback=endpoint_callback,
        help="specify the port to start the endpoint on.",
    ),
    version: Optional[bool] = Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        help="shows the current version of Pycoder.",
    ),
) -> str:
    """
    CLI command to get Python 🐍 code from set of topic[s] and description.
    Examples:\n
    🔥 pycoder --topic pytorch --description "a trainer for vision"\n
    🔥 pycoder -t pytorch -d "a trainer for vision"\n
    🔥 pycoder --topic pytorch --topic torch --description "a trainer for vision"\n
    🔥 pycoder -t pytorch -t torch -d "a trainer for vision"\n
    🔥 pycoder --topic pytorch --topic torch --description "a trainer for vision" --prefix "class Trainer:"\n
    🔥 pycoder -t pytorch -t torch -d "a trainer for vision" --prefix "class Trainer:"\n
    """
    st = time()
    with spinner():
        code = query(list(topic), description, prefix, max_length, cuda, False)
    et = time()

    echo(highlight(code, PythonLexer(), TerminalFormatter()))

    if execution_time:
        echo(formatter(f"took {(et-st):.2f} seconds to code 😀", color="g", bold=True))


def cli():
    app()
