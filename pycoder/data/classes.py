from dataclasses import dataclass
from pathlib import Path
from typing import Union


@dataclass(frozen=True)
class Code:
    text: str
    category: str
    language: str = "Python"

    @classmethod
    def load_from_path(cls, path: Union[Path, str], category, language="python"):
        path = Path(path)

        with open(path, "r") as fl:
            text = fl.read()

        return cls(text, category, language)
