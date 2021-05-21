from setuptools import setup, find_packages
from pycoder.version import __version__
from pathlib import Path
import sys

PACKAGE_DIR = Path("pycoder").absolute()
MODEL_PATH = PACKAGE_DIR / "assets" / "model"
TOKENIZER_PATH = PACKAGE_DIR / "assets" / "tokenizer"


if not MODEL_PATH.exists():
    # dev will be in argv if we do e.g. `pip install -e .`
    if "dev" not in sys.argv:
        raise FileNotFoundError(MODEL_PATH)

if not TOKENIZER_PATH.exists():
    # dev will be in argv if we do e.g. `pip install -e .`
    if "dev" not in sys.argv:
        raise FileNotFoundError(TOKENIZER_PATH)

with open("README.md") as f:
    long_description = f.read()

setup(
    name="pycoder",
    version=__version__,
    packages=find_packages(),
    description="A package to generate Python code from given topics and description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Himanshu Dutta",
    author_email="meet.himanshu.dutta@gmail.com",
    url="https://github.com/himanshu-dutta/pycoder",
    license="MIT License",
    install_requires=[
        "torch==1.8.1",
        "typer==0.3.2",
        "transformers==4.6.1",
        "markdown==3.3.4",
        "fastapi==0.65.1",
        "uvicorn==0.13.4",
        "pygments==2.9.0",
        "click-spinner==0.1.10",
    ],
    extras_require={"dev": ["pytest", "black", "wandb", "pygithub"]},
    entry_points={
        "console_scripts": [
            "pycoder=pycoder.api.cli:cli",
        ],
    },
    platforms=["linux", "unix"],
    include_package_data=True,
    package_data={
        "pycoder": [
            str(MODEL_PATH.relative_to(PACKAGE_DIR) / "*"),
            str(TOKENIZER_PATH.relative_to(PACKAGE_DIR) / "*"),
        ]
    },
    python_requires=">3.6.8",
)
