from pycoder.utils import *
from pycoder.data.classes import Code
from pycoder.data.modules import CodeDataset
from pycoder.model.trainer import get_trainer
from pycoder.model.transformer import get_tokenier, get_model, save_transformers

from pycoder.imports import random_split


def run_training(cfg):
    codes = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    print("loaded code instances from", formatter(cfg.FILE_INDEX_JSON_PATH, "g", True))
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_NAME, tokenizer, cfg.SPECIAL_TOKENS)
    print(
        f"loaded tokenizer and model  for {formatter(cfg.MODEL_NAME, 'g', True)} model"
    )

    ds = CodeDataset(
        codes,
        tokenizer,
        cfg.CONTROL_TOKENS,
        cfg.MAX_LENGTH,
        cfg.NUM_DESCRIPTION_SENTENCES,
    )

    print("dataset loaded successfully")

    val_sz = int(len(ds) * cfg.VAL_PCT)
    train_sz = len(ds) - val_sz
    train_ds, val_ds = random_split(ds, [train_sz, val_sz])

    trainer = get_trainer(model, tokenizer, train_ds, val_ds, cfg)

    print(formatter("initializing training", "g", True))
    trainer.train()

    save_transformers(
        cfg.MODEL_NAME,
        cfg.MODEL_PATH,
        cfg.TOKENIZER_PATH,
        trainer.model,
        trainer.tokenizer,
    )
