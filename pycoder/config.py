import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


#################
# secrets
##################
GITHUB_ACCESS_TOKEN = os.environ["GITHUB_ACCESS_TOKEN"]


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
