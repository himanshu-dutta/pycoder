from pycoder.imports import Union, Path, List, lru_cache
from pycoder.model.inference import CodeInference


@lru_cache(1)
def create_inference_instance(
    model_path: Union[Path, str],
    tokenizer_path: Union[Path, str],
    max_length: int,
) -> CodeInference:
    CONTROL_TOKENS = {
        "topics_token": "<|TOP|>",
        "description_token": "<|DESC|>",
        "code_token": "<|CODE|>",
        "eos_token": "<|EOS|>",
    }

    return CodeInference(model_path, tokenizer_path, CONTROL_TOKENS, max_length)


def query(
    cfg,
    topics: Union[List[str], str],
    description: str,
    code_prefix: str = "",
) -> str:
    coder = create_inference_instance(cfg.MODEL_PATH, cfg.TOKENIZER_PATH, 200)

    out = coder(topics, description, code_prefix)

    if len(out) > 0:
        return out[0]

    return None
