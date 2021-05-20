from pathlib import Path
from pycoder.version import __version__

MODEL_NAME = "gpt2-medium"
RUN_NAME = f"RUN:{(__version__.split('.'))[-1]}"

PACKAGE_DIR = Path(__file__).parent.absolute()
ARTIFACT_PATH = PACKAGE_DIR / "artifacts"

DATA_DIR = ARTIFACT_PATH / "data"
REPO_DATA_PATH = DATA_DIR / "repositories"
README_DATA_PATH = DATA_DIR / "readmes"

MODEL_DIR = ARTIFACT_PATH / "models"
MODEL_PATH = MODEL_DIR / RUN_NAME / MODEL_NAME / "model"
TOKENIZER_PATH = MODEL_DIR / RUN_NAME / MODEL_NAME / "tokenizer"
