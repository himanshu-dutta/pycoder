from torch.utils.data import random_split

import pycoder.config as cfg

from pycoder.data.classes import Code
from pycoder.imports import Path, rmtree
from pycoder.data.modules import CodeDataset

from pycoder.model.transformer import (
    get_tokenier,
    get_model,
    save_transformers,
    load_transformers,
)
from pycoder.model.trainer import get_trainer
from pycoder.model.inference import CodeInference


def test_method_get_tokenizer():
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    assert hasattr(
        tokenizer, "__len__"
    ), "The tokenizer object must have a __len__ property."


def test_method_get_model():
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_NAME, tokenizer, cfg.SPECIAL_TOKENS)
    assert hasattr(
        tokenizer, "__len__"
    ), "The tokenizer object must have a __len__ property."
    assert hasattr(
        model, "forward"
    ), "The model is a subclass of pytorch.nn.module, hence must have a forward method."


def test_method_load_save_model():
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_NAME, tokenizer, cfg.SPECIAL_TOKENS)

    model_path = Path(str(cfg.MODEL_PATH) + "__test")
    tokenizer_path = Path(str(cfg.TOKENIZER_PATH) + "__test")

    save_transformers(model_path, tokenizer_path, model, tokenizer)

    model, tokenizer = load_transformers(model_path, tokenizer_path)

    rmtree(model_path)
    rmtree(tokenizer_path)

    assert hasattr(
        tokenizer, "__len__"
    ), "The tokenizer object must have a __len__ property."
    assert hasattr(
        model, "forward"
    ), "The model is a subclass of pytorch.nn.module, hence must have a forward method."


def test_method_get_trainer():
    codes = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    model = get_model(cfg.MODEL_NAME, tokenizer, cfg.SPECIAL_TOKENS)
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


def test_class_CodeInference():

    inferer = CodeInference(
        cfg.MODEL_PATH,
        cfg.TOKENIZER_PATH,
        cfg.CONTROL_TOKENS,
        cfg.MAX_LENGTH,
    )

    results = inferer("tensorflow,ml", "a tensorflow training loop")

    assert isinstance(results, list), "inference of CodeInference call must be a list"
