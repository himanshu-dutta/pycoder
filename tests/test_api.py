from pycoder.api.main import query


def test_method_query():
    result = query(
        "pytorch",
        "a trainer class for vision model",
        "class Trainer:",
        max_length=100,
        verbose=True,
    )
    assert (
        isinstance(result, str) or result == None
    ), "query should return either a str or None instance"
