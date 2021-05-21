from pycoder.utils import *
from pycoder.imports import system, time, json, List, Union, tqdm, Path, datetime

try:
    from pycoder.imports import Github, Repository
except:
    pass


def repo_to_dict(repository: Repository, keyword: str) -> dict:
    try:
        return {
            "keyword": keyword,
            "url": repository.clone_url,
            "owner": repository.owner.login,
            "name": repository.name,
            "topics": repository.get_topics(),
            "readme_url": repository.get_readme().download_url,
            "language": repository.language,
        }
    except:
        return None


def collect_repository(
    g: Github,
    keyword: str,
    language: str = "python",
    num_instances: int = 400,
) -> List[dict]:
    end_time = time()
    start_time = end_time - 86400  # a day ago

    repositories = []

    while num_instances > 0:
        print(f"Collecting {formatter(keyword.capitalize(), color='g', bold=True)}...")

        start_time_str = datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%d")
        end_time_str = datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%d")
        not_added = 0

        query = (
            f"{keyword} language:{language} created:{start_time_str}..{end_time_str}"
        )

        results = g.search_repositories(query)

        for repository in tqdm(results, total=results.totalCount):
            repository_json = repo_to_dict(repository, keyword)
            if repository_json:
                repositories.append(repository_json)
            else:
                not_added += 1

        start_time -= 86400
        end_time -= 86400
        num_instances -= results.totalCount
        num_instances += not_added

    return repositories


def download_github_repositories(
    save_path: Union[Path, str],
    github_access_token: str,
    keywords: List[str],
) -> None:
    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    g = Github(github_access_token)

    repositories = []
    for keyword in keywords:
        repositories += collect_repository(g, keyword)

    print(f"Saving to {formatter(str(save_path), color='g', bold=True)}...")
    with open(str(save_path), "w") as fl:
        json.dump(repositories, fl)


def clone_repository(repository_dict: dict, save_path: Union[Path, str]) -> None:
    save_path = Path(save_path) / repository_dict["keyword"]
    save_path.mkdir(exist_ok=True, parents=True)

    url = repository_dict["url"]
    owner = repository_dict["owner"].lower()
    name = repository_dict["name"].lower()

    cmd = f"git clone {url} {save_path /(owner+'___'+name)}"

    system(cmd)


def clone_repositories(
    json_path: Union[Path, str], save_path: Union[Path, str]
) -> None:
    with open(json_path, "r") as fl:
        repositories = json.load(fl)

    repositories = tqdm(repositories)
    for repository in repositories:
        repositories.set_description(f"Cloning {repository['name']}")
        clone_repository(repository, save_path)
