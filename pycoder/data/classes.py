from pycoder.imports import json, Path, List, Union, dataclass, field


@dataclass(frozen=True)
class Code:
    path: Path
    category: str
    readme_path: Path
    topics: List[str] = field(default_factory=list)
    language: str = "Python"

    @classmethod
    def load_from_json(cls, json_path: Union[Path, str]):
        def to_cls(instance: dict) -> cls:
            return cls(
                Path(instance.get("path")),
                instance.get("category"),
                Path(instance.get("readme_path")),
                instance.get("topics"),
                instance.get("language"),
            )

        with open(json_path, "r") as fl:
            metadata = json.load(fl)

        return list(map(to_cls, metadata))

    @property
    def content(self) -> str:
        with self.path.open() as fl:
            return fl.read()
