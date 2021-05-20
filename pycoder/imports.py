import re
import json
import codecs
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
from os import environ, system, path, walk, listdir

import requests
from github import Github
from github.Repository import Repository

from tqdm import tqdm
from typer import Typer, Option
from dotenv import load_dotenv


import torch
from torch.utils.data import DataLoader, Dataset, random_split
from transformers import (
    AutoTokenizer,
    AutoConfig,
    AutoModelForPreTraining,
    AdamW,
    TrainingArguments,
    BeamScorer,
    Trainer,
    get_linear_schedule_with_warmup,
    pipeline,
)

from fastapi import FastAPI
from asyncio import create_task
from click_spinner import spinner

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter
