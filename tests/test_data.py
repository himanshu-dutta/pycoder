import pycoder.config as cfg

from pycoder.data.classes import Code
from pycoder.data.modules import CodeDataset
from pycoder.model.transformer import get_tokenier


def test_class_code():
    codes = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    assert isinstance(
        codes, list
    ), "load_from_json method must return a list of Code instances."
    assert isinstance(
        codes[0], Code
    ), "load_from_json method must return a list of Code instances."
    assert isinstance(
        codes[0].content, str
    ), "content attribute of a Code instance must be an instance of <str> class."


def test_module_code_dataset():
    codes = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    tokenizer = get_tokenier(cfg.MODEL_NAME, cfg.SPECIAL_TOKENS)
    ds = CodeDataset(
        codes=codes,
        tokenizer=tokenizer,
        control_tokens=cfg.CONTROL_TOKENS,
        max_length=cfg.MAX_LENGTH,
        num_description_sentences=cfg.NUM_DESCRIPTION_SENTENCES,
    )

    assert hasattr(ds, "__len__"), "Dataset must have a __len__ attribute."
    assert hasattr(ds, "__getitem__"), "Dataset must have a __getitem__ attribute."
    assert isinstance(
        ds[0], dict
    ), "CodeDataset should return a dictionary object when indexed."
    assert isinstance(
        ds.get_string(0), str
    ), "CodeDataset.get_string must return the string format text."
