from pycoder.utils import formatter
from pycoder.imports import (
    walk,
    path,
    listdir,
    re,
    json,
    rmtree,
    requests,
    tqdm,
    StringIO,
    Path,
    Markdown,
    Dict,
    List,
    Union,
    choices,
)


def index_repositories(
    json_path: Union[Path, str], save_path: Union[Path, str]
) -> None:
    with Path(json_path).open("r") as fl:
        repositories = json.load(fl)

    repository_dict = dict()
    for repository in repositories:
        owner = repository["owner"].lower()
        name = repository["name"].lower()
        repository_dict[f"{owner}___{name}"] = repository

    with Path(save_path).open("w") as fl:
        json.dump(repository_dict, fl)


def walk_clean(
    root_dir: Union[Path, str],
    must_remove_phrases: List[str],
    keep_extensions: List[str] = ["py"],
) -> None:
    dir_walk = tqdm(walk(root_dir, topdown=False))

    empty_dirs = set()
    total_files = removed_files = 0

    print(f"Walking in the root directory {str(root_dir)}...")

    for root, dirs, files in dir_walk:
        is_file = False

        for file in files:
            if path.splitext(file)[1][1:] not in keep_extensions or any(
                [phrase in str(file) for phrase in must_remove_phrases]
            ):
                (Path(root) / file).unlink()
                removed_files += 1

            else:
                is_file = True

            total_files += 1

        if not is_file:
            is_subdir = False

            for dir in dirs:
                if len(listdir(Path(root) / dir)) > 0:
                    is_subdir = True

            if not is_subdir or any(
                [phrase in str(root) for phrase in must_remove_phrases]
            ):
                empty_dirs.add(Path(root).absolute())

        dir_walk.update()

    print("Removing empty directories...")
    for empty_dir in tqdm(empty_dirs):
        try:
            rmtree(empty_dir)

        except:
            continue

    print(
        f"Total {formatter((total_files-removed_files), color='g', bold=True)}/{formatter(total_files, color='g', bold=True)} belong to {keep_extensions} extensions."
    )


def index_files(
    root_dir: Union[Path, str],
    indexed_repositories: Dict[str, dict],
    readme_save_dir: Union[Path, str],
    extensions: List[str] = ["py"],
) -> None:
    dir_walk = tqdm(walk(Path(root_dir), topdown=False))
    files_to_index = []

    for root, _, files in dir_walk:
        repository = None
        for part in Path(root).parts:
            if re.search("___", part):
                repository = indexed_repositories[part]

        for file in files:
            if path.splitext(file)[1][1:] in extensions:
                files_to_index.append(
                    download_readme(
                        {
                            "name": file,
                            "path": str(Path(root) / file),
                            "category": Path(root_dir).name,
                            "readme_url": repository["readme_url"],
                            "repository_name": repository["name"],
                            "repository_owner": repository["owner"],
                            "topics": repository["topics"],
                        },
                        readme_save_dir,
                    )
                )
            dir_walk.update()

    print(
        formatter(
            f"Indexed files for {formatter(Path(root_dir).name, color='g', bold=True)} ",
            tick=True,
        )
    )

    return files_to_index


def index_files_from_root(
    root_dir: Union[Path, str],
    save_path: Union[Path, str],
    readme_save_dir: Union[Path, str],
    repository_index_path: Union[Path, str],
    keywords: List[str],
) -> None:

    indexed_files = []

    with Path(repository_index_path).open() as fl:
        indexed_repositories = json.load(fl)

    for keyword in keywords:
        indexed_files += index_files(
            Path(root_dir) / keyword, indexed_repositories, readme_save_dir
        )

    # in case the directory to store the index file doesn't exist
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "w") as fl:
        json.dump(indexed_files, fl)

    print(
        formatter(
            f"Saved the file successfully to {formatter(save_path, color='g', bold=True)}",
            tick=True,
        )
    )


class unmark:
    """
    converts markdown string to a text string
    source: https://stackoverflow.com/a/54923798
    """

    def __init__(self):
        Markdown.output_formats["plain"] = self.unmark_element
        self.__md = Markdown(output_format="plain")
        self.__md.stripTopLevelTags = False

    @classmethod
    def unmark_element(cls, element, stream=None):
        if stream is None:
            stream = StringIO()
        if element.text:
            stream.write(element.text)
        for sub in element:
            cls.unmark_element(sub, stream)
        if element.tail:
            stream.write(element.tail)
        return stream.getvalue()

    def __call__(self, text):
        return self.__md.convert(text)


def download_readme(file_json, save_dir: Union[Path, str]) -> dict:
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    owner = file_json["repository_owner"]
    name = file_json["repository_name"]
    readme_path = save_dir / f"{owner}__{name}.txt"

    if not readme_path.exists():

        url = file_json["readme_url"]
        c = requests.get(url).text
        c = str(unmark()(c))

        with readme_path.open("w") as fl:
            fl.write(c)

    file_json["readme_path"] = str(readme_path)
    return file_json


def remove_commments(
    code: str,
) -> str:

    single_line_pattern = r"#(.*?)\n"
    multi_line_pattern = r'"""(.*?)"""'

    match = re.search(single_line_pattern, code)
    while match != None:
        start, end = match.span()
        end -= 1

        code = code[:start:] + code[end::]

        match = re.search(single_line_pattern, code, re.M)

    match = re.search(multi_line_pattern, code, re.M)
    while match != None:
        start, end = match.span()
        end -= 1

        code = code[:start:] + code[end::]

        match = re.search(multi_line_pattern, code, re.M)

    return code


def sentence_tokenize_and_select_random(text: str, num_sentences: int = 2) -> str:

    sentences = list(filter(lambda x: len(x) > 0, text.split(".")))

    if num_sentences < len(sentences):
        return ".".join(sentences)

    return ".".join(choices(sentences, k=num_sentences))
