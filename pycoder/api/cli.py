import pycoder.config as cfg
from pycoder.api.main import query
from pycoder.imports import (
    List,
    Typer,
    Optional,
    Option,
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
    topic: List[str] = Option(..., help="topic[s] for the code to be written."),
    description: str = Option(..., help="description of the code to be written."),
    prefix: Optional[str] = Option("", help="[optional] starter code to be filled in."),
) -> str:
    """
    CLI command to get Python code from set of topics[multiple] and description.
    Ex:\n
        pycoder --topic pytorch --description "a trainer for vision"\n
        pycoder --topic pytorch --topic torch --description "a trainer for vision"\n
        pycoder --topic pytorch --topic torch --description "a trainer for vision" --prefix "class Trainer:"\n
    """
    code = query(cfg, list(topic), description, prefix)
    print(highlight(code, PythonLexer(), TerminalFormatter()))


if __name__ == "__main__":
    app()
