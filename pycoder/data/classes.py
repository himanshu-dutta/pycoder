import json
from pathlib import Path
from typing import Union
from dataclasses import dataclass


@dataclass(frozen=True)
class Code:
    path: Path
    category: str
    language: str = "Python"

    @classmethod
    def load_from_json(cls, json_path: Union[Path, str]):
        def to_cls(instance: dict) -> cls:
            return cls(
                Path(instance.get("path")),
                instance.get("category"),
                instance.get("language"),
            )

        with open(json_path, "r") as fl:
            metadata = json.load(fl)

        return list(map(to_cls, metadata))

    @property
    def content(self) -> str:
        with self.path.open() as fl:
            return fl.read()
