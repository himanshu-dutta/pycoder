from torch.utils.data import random_split

import pycoder.config as cfg

from pycoder.data.classes import Code
from pycoder.data.modules import CodeDataset

from pycoder.model.transformer import (
    get_tokenier,
    get_model,
    save_transformers,
    load_transformers,
)
from pycoder.model.trainer import get_trainer


def test_method_get_tokenizer():
    tokenizer = get_tokenier(cfg.MODEL_TYPE, cfg.SPECIAL_TOKENS)
    assert hasattr(
        tokenizer, "__len__"
    ), "The tokenizer object must have a __len__ property."


def test_method_get_model():
    tokenizer = get_tokenier(cfg.MODEL_TYPE, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_TYPE, tokenizer, cfg.SPECIAL_TOKENS)
    assert hasattr(
        tokenizer, "__len__"
    ), "The tokenizer object must have a __len__ property."
    assert hasattr(
        model, "forward"
    ), "The model is a subclass of pytorch.nn.module, hence must have a forward method."


def test_method_load_save_model():
    tokenizer = get_tokenier(cfg.MODEL_TYPE, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_TYPE, tokenizer, cfg.SPECIAL_TOKENS)

    save_transformers(
        cfg.MODEL_TYPE, cfg.MODEL_PATH, cfg.TOKENIZER_PATH, model, tokenizer
    )

    model, tokenizer = load_transformers(
        cfg.MODEL_TYPE, cfg.MODEL_PATH, cfg.TOKENIZER_PATH
    )

    assert hasattr(
        tokenizer, "__len__"
    ), "The tokenizer object must have a __len__ property."
    assert hasattr(
        model, "forward"
    ), "The model is a subclass of pytorch.nn.module, hence must have a forward method."


def test_method_get_trainer():
    codes = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    tokenizer = get_tokenier(cfg.MODEL_TYPE, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_TYPE, tokenizer, cfg.SPECIAL_TOKENS)
    ds = CodeDataset(
        codes=codes,
        tokenizer=tokenizer,
        control_tokens=cfg.CONTROL_TOKENS,
        max_length=cfg.MAX_LENGTH,
        num_description_sentences=cfg.NUM_DESCRIPTION_SENTENCES,
    )

    val_sz = int(0.2 * len(ds))
    train_sz = len(ds) - val_sz
    train_ds, val_ds = random_split(ds, [train_sz, val_sz])

    trainer = get_trainer(model, tokenizer, train_ds, val_ds, cfg)

    assert hasattr(trainer, "model"), "Trainer object must have a model attribute."
    assert hasattr(
        trainer, "tokenizer"
    ), "Trainer object must have a tokenizer attribute."
    assert hasattr(trainer, "train"), "Trainer object must have a train method."
    assert hasattr(
        trainer.model, "save_pretrained"
    ), "Trainer.model object must have a save_pretrained method."
    assert hasattr(
        trainer.tokenizer, "save_pretrained"
    ), "Trainer.tokenizer object must have a save_pretrained method."
