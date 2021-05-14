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
from typing import List, Union, Dict
from dataclasses import dataclass, field
from os import environ, system, path, walk, listdir

import requests
from github import Github
from github.Repository import Repository

from tqdm import tqdm
from typer import Typer
from dotenv import load_dotenv


import torch
from torch.utils.data import DataLoader, Dataset
from transformers import (
    AutoTokenizer,
    AutoConfig,
    AutoModelForPreTraining,
    AdamW,
    TrainingArguments,
    BeamScorer,
    Trainer,
    get_linear_schedule_with_warmup,
)
