import pycoder.config as cfg
from pycoder.api.main import query
from pycoder.imports import (
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
        code = query(cfg, list(topic), description, prefix, False)

    print(highlight(code, PythonLexer(), TerminalFormatter()))


if __name__ == "__main__":
    app()
