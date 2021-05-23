from pycoder.version import __version__
from pycoder.imports import getenv, Path

try:
    from pycoder.imports import load_dotenv

    load_dotenv()
except:
    pass

#################
# secrets
##################
GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN")
WANDB_API_KEY = getenv("WANDB_API_KEY")


####################
# configuration
####################

# model config
GPT_CONFIGS = {
    "S": {"MODEL_NAME": "gpt2", "MAX_LENGTH": 768},
    "M": {"MODEL_NAME": "gpt2-medium", "MAX_LENGTH": 1024},
    "L": {"MODEL_NAME": "gpt2-large", "MAX_LENGTH": 1280},
    "XL": {"MODEL_NAME": "gpt2-xl", "MAX_LENGTH": 1600},
}

HF_HUB_NAME = "himanshu-dutta/pycoder-gpt2"
MODEL_NAME = GPT_CONFIGS["M"]["MODEL_NAME"]
MAX_LENGTH = GPT_CONFIGS["M"]["MAX_LENGTH"]
NUM_DESCRIPTION_SENTENCES = 2

SPECIAL_TOKENS = {
    "bos_token": "<|BOS|>",
    "eos_token": "<|EOS|>",
    "unk_token": "<|UNK|>",
    "pad_token": "<|PAD|>",
    "sep_token": "<|SEP|>",
}
CONTROL_TOKENS = {
    "topics_token": "<|TOP|>",
    "description_token": "<|DESC|>",
    "code_token": "<|CODE|>",
    "eos_token": SPECIAL_TOKENS["eos_token"],
}

# training parameters
EPOCHS = 10
TRAIN_BATCHSIZE = 1
BATCH_UPDATE = 16
LR = 5e-4
EPS = 1e-8
WARMUP_STEPS = 1e2
APEX_OPT_LEVEL = "01"
FP16 = True
VAL_PCT = 0.1
RUN_NAME = f"RUN:{(__version__.split('.'))[-1]}"

# paths and directories
PACKAGE_DIR = Path(__file__).parent.absolute()
ARTIFACT_PATH = PACKAGE_DIR / "artifacts"

CACHE_DIR = PACKAGE_DIR / "cache"

ASSETS_DIR = PACKAGE_DIR / "assets"
CONFIG_PATH = Path(__file__)

DATA_DIR = ARTIFACT_PATH / "data"
REPO_DATA_PATH = DATA_DIR / "repositories"
README_DATA_PATH = DATA_DIR / "readmes"

MODEL_DIR = ARTIFACT_PATH / "models"
MODEL_PATH = MODEL_DIR / RUN_NAME / MODEL_NAME / "model"
TOKENIZER_PATH = MODEL_DIR / RUN_NAME / MODEL_NAME / "tokenizer"

CHECKPOINT_PATH = ARTIFACT_PATH / "checkpoints" / RUN_NAME / MODEL_NAME

REPO_JSON_PATH = DATA_DIR / "repositories.json"
REPO_INDEX_JSON_PATH = DATA_DIR / "indexed_repos.json"
FILE_INDEX_JSON_PATH = DATA_DIR / "indexed_files.json"

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
