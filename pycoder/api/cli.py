from pycoder.api.main import query
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
        "", "--prefix", "-p", help="[optional] starter code to be filled in."
    ),
    max_length: Optional[int] = Option(
        200, "--max-length", "-ml", help="max length of code to get."
    ),
) -> str:
    """
    CLI command to get Python code from set of topics[multiple] and description.
    Ex:\n
        pycoder --topic pytorch --description "a trainer for vision"\n
        pycoder -t pytorch -d "a trainer for vision"\n
        pycoder --topic pytorch --topic torch --description "a trainer for vision"\n
        pycoder -t pytorch -t torch -d "a trainer for vision"\n
        pycoder --topic pytorch --topic torch --description "a trainer for vision" --prefix "class Trainer:"\n
        pycoder -t pytorch -t torch -d "a trainer for vision" --prefix "class Trainer:"\n
    """
    with spinner():
        code = query(list(topic), description, prefix, max_length, False)

    echo(highlight(code, PythonLexer(), TerminalFormatter()))


def cli():
    app()
