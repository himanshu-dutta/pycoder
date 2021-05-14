from pycoder.imports import environ, Path, load_dotenv

load_dotenv()

#################
# secrets
##################
GITHUB_ACCESS_TOKEN = environ["GITHUB_ACCESS_TOKEN"]


####################
# configuration
####################
PACKAGE_DIR = Path(__file__).parent.absolute()
DATA_PATH = PACKAGE_DIR.parent / "data"
REPO_DATA_PATH = DATA_PATH / "repositories"
README_DATA_PATH = DATA_PATH / "readmes"

REPO_JSON_PATH = DATA_PATH / "repositories.json"
REPO_INDEX_JSON_PATH = DATA_PATH / "indexed_repos.json"
FILE_INDEX_JSON_PATH = DATA_PATH / "indexed_files.json"

KEYWORDS = ["tensorflow", "pytorch", "django", "flask", "algorithms", "fastapi"]


#############
# constants
#############

TICK = "✅"
CROSS = "❌"

BOLD = "\033[1m"
GREEN = "\033[32m"
RED = "\033[91m"
END = "\033[0;0m"

GITIGNORES = [
    "__pycache__/",
    "build/",
    "develop-eggs/",
    "dist/",
    "downloads/",
    "eggs/",
    ".eggs/",
    "lib/",
    "lib64/",
    "parts/",
    "sdist/",
    "var/",
    "wheels/",
    "share/python-wheels/",
    ".egg-info/",
    "htmlcov/",
    ".tox/",
    ".nox/",
    ".hypothesis/",
    ".pytest_cache/",
    "cover/",
    "instance/",
    "docs/_build/",
    ".pybuilder/",
    "target/",
    ".ipynb_checkpoints",
    "profile_default/",
    "ipython_config.py",
    "__pypackages__/",
    ".sage.py",
    ".env",
    ".venv",
    "env/",
    "venv/",
    "ENV/",
    "env.bak/",
    "venv.bak/",
    ".spyderproject",
    ".spyproject",
    ".ropeproject",
    "/site",
    ".mypy_cache/",
    ".dmypy.json",
    "dmypy.json",
    ".pyre/",
    ".pytype/",
    "cython_debug/",
]
