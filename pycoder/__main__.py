import typer

from .data import download, preprocess

app = typer.Typer()


###################
#   data commands
###################

@app.command()
def download_github_repositories(save_path: str):
    download.download_github_repositories(save_path)


@app.command()
def clone_repositories(json_path: str):
    download.clone_repositories(json_path)


@app.command()
def clean_repositories(root_dir: str):
    preprocess.walk_clean(root_dir)


@app.command()
def index_files(root_dir: str, save_path: str):
    preprocess.index_files_from_root(root_dir, save_path)


if __name__ == "__main__":
    app()
