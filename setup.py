from setuptools import setup, find_packages
from pycoder.version import __version__
from pycoder.production import (
    MODEL_PATH,
    TOKENIZER_PATH,
    PACKAGE_DIR,
)
import sys


if not MODEL_PATH.exists():
    # develop will be in argv if we do e.g. `pip install -e .`
    if "dev" not in sys.argv:
        raise FileNotFoundError(MODEL_PATH)

if not TOKENIZER_PATH.exists():
    # develop will be in argv if we do e.g. `pip install -e .`
    if "dev" not in sys.argv:
        raise FileNotFoundError(TOKENIZER_PATH)

setup(
    name="pycoder",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "torch",
        "typer",
        "transformers",
        "Markdown",
        "fastapi",
        "uvicorn",
        "Pygments",
        "click-spinner",
    ],
    extras_require={"dev": ["pytest", "black", "wandb", "pygithub"]},
    entry_points={
        "console_scripts": [
            "pycoder=pycoder.api.cli:cli",
        ],
    },
    package_data={
        "pycoder": [
            str(MODEL_PATH.relative_to(PACKAGE_DIR) / "*"),
            str(TOKENIZER_PATH.relative_to(PACKAGE_DIR) / "*"),
        ]
    },
)
