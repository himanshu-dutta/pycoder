from setuptools import setup, find_packages
from pycoder.version import __version__
from pathlib import Path

PACKAGE_DIR = Path("pycoder").absolute()
HTML_PATH = PACKAGE_DIR / "api" / "index.html"

if not HTML_PATH.exists():
    raise FileNotFoundError(HTML_PATH)

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
    install_requires=[
        "torch>=1.8.1",
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
    include_package_data=True,
    package_data={
        "pycoder": [
            str(HTML_PATH.relative_to(PACKAGE_DIR)),
        ]
    },
    python_requires=">3.7",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    platforms=["linux", "unix"],
)
