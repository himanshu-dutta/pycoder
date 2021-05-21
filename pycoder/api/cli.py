from pycoder.api.main import query
from pycoder.version import __version__
from pycoder.imports import (
    echo,
    List,
    Typer,
    Option,
    Optional,
    spinner,
    highlight,
    PythonLexer,
    TerminalFormatter,
)

app = Typer()

############################
#   interface for inference
############################


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
) -> str:
    """
    CLI command to get Python code from set of topics[multiple] and description.
    Example:\n
        pycoder --topic pytorch --description "a trainer for vision"\n
        pycoder -t pytorch -d "a trainer for vision"\n
        pycoder --topic pytorch --topic torch --description "a trainer for vision"\n
        pycoder -t pytorch -t torch -d "a trainer for vision"\n
        pycoder --topic pytorch --topic torch --description "a trainer for vision" --prefix "class Trainer:"\n
        pycoder -t pytorch -t torch -d "a trainer for vision" --prefix "class Trainer:"\n
    """
    with spinner():
        code = query(list(topic), description, prefix, max_length, cuda, False)

    echo(highlight(code, PythonLexer(), TerminalFormatter()))


def cli():
    app()
