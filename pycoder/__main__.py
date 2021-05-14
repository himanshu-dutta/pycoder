import pycoder.config as cfg
from pycoder.imports import List, Typer
from pycoder.data import download, processing

app = Typer()


###################
#   data commands
###################


@app.command()
def download_github_repositories(
    save_path: str = cfg.REPO_JSON_PATH,
    github_accesss_token: str = cfg.GITHUB_ACCESS_TOKEN,
    keywords: List[str] = cfg.KEYWORDS,
):
    download.download_github_repositories(save_path, github_accesss_token, keywords)


@app.command()
def clone_repositories(
    json_path: str = cfg.REPO_JSON_PATH, save_path: str = cfg.REPO_DATA_PATH
):
    download.clone_repositories(json_path, save_path)


@app.command()
def index_repositories(
    json_path: str = cfg.REPO_JSON_PATH, save_path: str = cfg.REPO_INDEX_JSON_PATH
):
    processing.index_repositories(json_path, save_path)


@app.command()
def clean_repositories(
    root_dir: str = cfg.REPO_DATA_PATH,
    must_remove_phrases: List[str] = cfg.GITIGNORES,
):
    processing.walk_clean(root_dir, must_remove_phrases)


@app.command()
def index_files(
    root_dir: str = cfg.REPO_DATA_PATH,
    save_path: str = cfg.FILE_INDEX_JSON_PATH,
    readme_save_path: str = cfg.README_DATA_PATH,
    repository_index: str = cfg.REPO_INDEX_JSON_PATH,
    keywords: List[str] = cfg.KEYWORDS,
):
    processing.index_files_from_root(
        root_dir,
        save_path,
        readme_save_path,
        repository_index,
        keywords,
    )


@app.command()
def get_data(
    repository_json_path: str = cfg.REPO_JSON_PATH,
    github_accesss_token: str = cfg.GITHUB_ACCESS_TOKEN,
    search_keywords: List[str] = cfg.KEYWORDS,
    must_remove_phrases: List[str] = cfg.GITIGNORES,
    repository_data_path: str = cfg.REPO_DATA_PATH,
    repository_index_json_path: str = cfg.REPO_INDEX_JSON_PATH,
    file_index_json_path: str = cfg.FILE_INDEX_JSON_PATH,
    readme_save_path: str = cfg.README_DATA_PATH,
):
    # download github repository data to a json file
    download.download_github_repositories(
        repository_json_path,
        github_accesss_token,
        search_keywords,
    )

    # clone the repository to a local folder
    download.clone_repositories(
        repository_json_path,
        repository_data_path,
    )

    # index the repositories to a json file
    processing.index_repositories(repository_json_path, repository_index_json_path)

    # clean the repositories for any unwanted file
    processing.walk_clean(repository_data_path, must_remove_phrases)

    # index the required files and download the readme for them
    processing.index_files_from_root(
        repository_data_path,
        file_index_json_path,
        readme_save_path,
        repository_index_json_path,
        search_keywords,
    )


if __name__ == "__main__":
    app()
