# PyCoder 🐍

<img alt="Made With Python" src="http://ForTheBadge.com/images/badges/made-with-python.svg">

<!-- <img alt="Medium" src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" height=35/> -->

<!-- [![PyPI version fury.io](https://badge.fury.io/py/torchlit.svg)](https://pypi.org/project/torchlit/)  -->
  
`PyCoder` is a tool to generate python code out of a few given topics and description. It uses GPT-2 language model as its engine. Pycoder poses writing Python code as a conditional-Causal Language Modelling(c-CLM). It has been trained on millions of lines of Python code written by all of us.  At current stage and state of training it produces sensible code with few lines of description, but the scope of improvement for the model is limitless. 

Pycoder has been developed as a Command Line tool (CLI), an API endpoint, as well as a python package (yet to be deployed to PyPI). This repository acts as a framework for anyone who either wants to try to build Pycoder from scratch, or turn Pycoder into maybe a `CPPCoder` or `JSCoder` 😃.  A blogpost about the developement of the project will be released soon.

To use `Pycoder` as a CLI utility, clone the repository as normal, and install the package with:
```console
foo@bar:❯ python setup.py install
```
After this the package could be verified and accessed as either a native CLI tool or a python package with:
```console
foo@bar:❯ python -m pycoder --version
```
Or directly as:
```console
foo@bar:❯ pycoder --version
```

The API endpoint is deployed using FastAPI. Once all the requirements have been installed for the project, the API can be accessed with:
```console
foo@bar:❯ pycoder endpoint
```


### Tech Stack
<p align="center">
<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> <img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" /> <img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" height=28 style="background-color:black;"> <img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg" height=28 style="background-color:teal;">
</p>

### Tested Platforms
<p align="center">
<img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> <img alt="Windows 10" src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
</p>

<hr />

<p align="center">
<img alt="MIT License" src="https://img.shields.io/github/license/himanshu-dutta/pycoder?style=for-the-badge&logo=appveyor">
<img src="https://img.shields.io/badge/Copyright-Himanshu_Dutta-2ea44f?style=for-the-badge&logo=appveyor" >
</p>