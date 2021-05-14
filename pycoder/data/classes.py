from pycoder.imports import json, Path, List, Union, dataclass, field, codecs


@dataclass
class Code:
    path: Path
    category: str
    readme_path: Path
    topics: List[str] = field(default_factory=list)
    language: str = "Python"

    def __post_init__(self):
        self._readme = None
        self._content = None

    @classmethod
    def load_from_raw(cls, instance: dict) -> "Code":
        return cls(
            Path(instance.get("path")),
            instance.get("category"),
            Path(instance.get("readme_path")),
            instance.get("topics"),
            instance.get("language"),
        )

    @classmethod
    def load_from_json(cls, json_path: Union[Path, str]) -> List["Code"]:
        with open(json_path, "r") as fl:
            metadata = json.load(fl)

        return list(filter(lambda x: x.is_valid(), map(cls.load_from_raw, metadata)))

    @property
    def content(self) -> str:
        try:
            if not self._content:
                with codecs.open(
                    self.path, "r", encoding="utf-8", errors="ignore"
                ) as fl:
                    self._content = fl.read()
            return self._content
        except:
            return None

    @property
    def readme(self) -> str:
        try:
            if not self._readme:
                with codecs.open(
                    self.readme_path, "r", encoding="utf-8", errors="ignore"
                ) as fl:
                    self._readme = fl.read()
            return self._readme
        except:
            return None

    def is_valid(self) -> bool:
        return bool(self.content and self.readme)
