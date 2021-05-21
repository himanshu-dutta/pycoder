from pycoder.model.inference import CodeInference
from pycoder.imports import Union, Path, List, lru_cache, Path


MODEL_PATH = Path(__file__).parent.parent / "assets" / "model"
TOKENIZER_PATH = Path(__file__).parent.parent / "assets" / "tokenizer"


@lru_cache(1)
def create_inference_instance(
    model_path: Union[Path, str] = MODEL_PATH,
    tokenizer_path: Union[Path, str] = TOKENIZER_PATH,
    max_length: int = 200,
    cuda: bool = False,
    verbose: bool = False,
) -> CodeInference:
    CONTROL_TOKENS = {
        "topics_token": "<|TOP|>",
        "description_token": "<|DESC|>",
        "code_token": "<|CODE|>",
        "eos_token": "<|EOS|>",
    }

    return CodeInference(
        model_path,
        tokenizer_path,
        CONTROL_TOKENS,
        max_length,
        cuda,
        verbose,
    )


def query(
    topics: Union[List[str], str],
    description: str,
    code_prefix: str = "",
    max_length: int = 200,
    cuda: bool = False,
    verbose: bool = False,
) -> str:

    coder = create_inference_instance(max_length=max_length, cuda=cuda, verbose=verbose)

    out = coder(topics, description, code_prefix)

    if len(out) > 0:
        return out[0]

    return None
