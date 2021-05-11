import os
from dotenv import load_dotenv
load_dotenv()


#################
# secrets
##################
GITHUB_ACCESS_TOKEN = os.environ["GITHUB_ACCESS_TOKEN"]


####################
# configuration
####################
DATA_PATH = "./data"
REPO_PATH = "./data/repositories"
REPO_DATA_PATH = "./data/repositories.json"
KEYWORDS = ["tensorflow", "pytorch", "django",
            "flask", "algorithms", "fastapi"]
