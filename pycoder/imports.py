######################
#   python imports
######################

import re
import json
import codecs
import requests
from time import time
from io import StringIO
from pathlib import Path
from shutil import rmtree
from random import choices
from markdown import Markdown
from datetime import datetime
from functools import lru_cache
from dataclasses import dataclass, field
from typing import List, Union, Dict, Tuple, Optional
from os import getenv, system, path, walk, listdir


######################
#   model imports
######################

import torch
from torch.utils.data import DataLoader, Dataset, random_split
from transformers import (
    AutoTokenizer,
    AutoConfig,
    GPT2LMHeadModel,
    AutoModelForPreTraining,
    AdamW,
    TrainingArguments,
    BeamScorer,
    Trainer,
    get_linear_schedule_with_warmup,
    pipeline,
)


######################
#   api imports
######################

from tqdm import tqdm
from typer import Typer, Option, Exit, echo

from uvicorn import run
from fastapi import FastAPI
from asyncio import create_task
from click_spinner import spinner
from fastapi.responses import HTMLResponse

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter, HtmlFormatter


######################
#   dev imports
######################

try:
    from github import Github
    from github.Repository import Repository
    from dotenv import load_dotenv
except:
    pass
