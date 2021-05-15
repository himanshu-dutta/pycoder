from pycoder.model.trainer import get_trainer
from pycoder.model.transformer import (
    get_tokenier,
    get_model,
    save_transformers,
)

from pycoder.data.classes import Code
from pycoder.data.modules import CodeDataset

from pycoder.imports import random_split


def run_training(cfg):
    codes = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_NAME, tokenizer, cfg.SPECIAL_TOKENS)

    ds = CodeDataset(
        codes,
        tokenizer,
        cfg.CONTROL_TOKENS,
        cfg.MAX_LENGTH,
        cfg.NUM_DESCRIPTION_SENTENCES,
    )

    val_sz = int(len(ds) * cfg.VAL_PCT)
    train_sz = len(ds) - val_sz
    train_ds, val_ds = random_split(ds, [train_sz, val_sz])

    trainer = get_trainer(model, tokenizer, train_ds, val_ds, cfg)

    trainer.train()

    save_transformers(
        cfg.MODEL_NAME,
        cfg.MODEL_PATH,
        cfg.TOKENIZER_PATH,
        trainer.model,
        trainer.tokenizer,
    )
