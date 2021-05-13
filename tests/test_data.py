from pycoder.data.classes import Code
import pycoder.config as cfg


def test_class_code():
    code = Code.load_from_json(cfg.FILE_INDEX_JSON_PATH)
    assert hasattr(
        code, "__len__"
    ), "load_from_json method must return a list of Code instances."
    assert isinstance(
        code[0], Code
    ), "load_from_json method must return a list of Code instances."
    assert isinstance(
        code[0].content, str
    ), "content attribute of a Code instance must be an instance of <str> class."
