import pycoder.config as cfg
from pycoder.model.transformer import (
    get_tokenier,
    get_model,
    save_transformers,
    load_transformers,
)


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
