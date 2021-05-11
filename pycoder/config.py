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
DATA_PATH = Path("./data")
REPO_PATH = DATA_PATH / "repositories"
REPO_DATA_PATH = DATA_PATH / "repositories.json"
INDEXED_FILE_PATH = DATA_PATH / "indexed_files.json"

KEYWORDS = ["tensorflow", "pytorch", "django",
            "flask", "algorithms", "fastapi"]
