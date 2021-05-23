<br />
<div align="center">
<img src="https://raw.githubusercontent.com/himanshu-dutta/pycoder/master/docs/pycoder-logo-p.png">


<br/>
<img alt="Made With Python" src="http://ForTheBadge.com/images/badges/made-with-python.svg" height=28 style="display:inline; height:28px;" />

<img alt="Medium" src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" height=28 style="display:inline; height:28px;"/>

<a href="https://wandb.ai/himanshu-dutta/pycoder">
<img alt="WandB Dashboard" src="https://raw.githubusercontent.com/wandb/assets/04cfa58cc59fb7807e0423187a18db0c7430bab5/wandb-github-badge-28.svg" height=28 style="display:inline; height:28px;" />
</a>

[![PyPI version fury.io](https://badge.fury.io/py/pycoder.svg)](https://pypi.org/project/pycoder/) 
</div>
  
<div align="justify">

`PyCoder` is a tool to generate python code out of a few given topics and a description. It uses GPT-2 language model as its engine. Pycoder poses writing Python code as a conditional-Causal Language Modelling(c-CLM). It has been trained on millions of lines of Python code written by all of us.  At the current stage and state of training, it produces sensible code with few lines of description, but the scope of improvement for the model is limitless. 

Pycoder has been developed as a Command-Line tool (CLI), an API endpoint, as well as a python package (yet to be deployed to PyPI). This repository acts as a framework for anyone who either wants to try to build Pycoder from scratch or turn Pycoder into maybe a `CPPCoder` or `JSCoder` 😃.  A blog post about the development of the project will be released soon.

To use `Pycoder` as a CLI utility, clone the repository as normal, and install the package with:
```console
foo@bar:❯ pip install pycoder
```
After this the package could be verified and accessed as either a native CLI tool or a python package with:
```console
foo@bar:❯ python -m pycoder --version

Or directly as:

foo@bar:❯ pycoder --version
```

On installation the CLI can be used directly, such as:

```console
foo@bar:❯ pycoder -t pytorch -t torch -d "a trainer class to train vision model" -ml 120
```

The API endpoint is deployed using FastAPI. Once all the requirements have been installed for the project, the API can be accessed with:
```console
foo@bar:❯ pycoder --endpoint PORT_NUMBER

Or

foo@bar:❯ pycoder -e PORT_NUMBER
```
</div>

## Tech Stack
<div align="center">
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white" style="display:inline;" />
<img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" style="display:inline;" />
<img alt="Transformers" src="https://raw.githubusercontent.com/huggingface/transformers/master/docs/source/imgs/transformers_logo_name.png" height=28 width=120 style="display:inline; background-color:white; height:28px; width:120px"/>
<img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" style="display:inline;" />
<img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" height=28 style="display:inline; background-color:black; height:28px;" /> 
<img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg" height=28 style="display:inline; background-color:teal; height:28px;" />
</div>

## Tested Platforms
<div align="center">
<img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" style="display:inline;" />
<img alt="Windows 10" src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" style="display:inline;" />
</div>


## BibTeX
If you want to cite the framework feel free to use this:

```bibtex
@article{dutta2021pycoder,
  title={Pycoder},
  author={Dutta, H},
  journal={GitHub. Note: https://github.com/himanshu-dutta/pycoder},
  year={2021}
}
```
<hr />

<div align="center">
<img alt="MIT License" src="https://img.shields.io/github/license/himanshu-dutta/pycoder?style=for-the-badge&logo=appveyor" style="display:inline;" /> 
<img src="https://img.shields.io/badge/Copyright-Himanshu_Dutta-2ea44f?style=for-the-badge&logo=appveyor" style="display:inline;" />
</div>