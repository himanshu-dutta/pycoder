from pycoder.utils import *
from pycoder.imports import (
    json,
    AutoConfig,
    AutoModelForPreTraining,
    AutoTokenizer,
    Union,
    Path,
    Tuple,
)


def get_tokenier(
    model_name_or_path: Union[Path, str] = None,
    special_tokens: dict = None,
) -> "transformer.PreTrainedTokenizer":

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    if special_tokens:
        tokenizer.add_special_tokens(special_tokens)

    return tokenizer


def get_model(
    model_name_or_path: Union[Path, str],
    tokenizer: "transformer.PreTrainedTokenizer",
    special_tokens=None,
) -> "nn.Module":

    if special_tokens:
        config = AutoConfig.from_pretrained(
            model_name_or_path,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            sep_token_id=tokenizer.sep_token_id,
            pad_token_id=tokenizer.pad_token_id,
            output_hidden_states=False,
        )
    else:
        config = AutoConfig.from_pretrained(
            model_name_or_path,
            pad_token_id=tokenizer.eos_token_id,
            output_hidden_states=False,
        )

    model = AutoModelForPreTraining.from_pretrained(model_name_or_path, config=config)

    if special_tokens:
        model.resize_token_embeddings(len(tokenizer))

    return model


def save_transformers(
    model_path: Union[Path, str],
    tokenizer_path: Union[Path, str],
    model: "nn.Module",
    tokenizer: "transformer.PreTrainedTokenizer",
    verbose: bool = True,
) -> None:
    model_path, tokenizer_path = Path(model_path), Path(tokenizer_path)

    model_path.mkdir(parents=True, exist_ok=True)
    tokenizer_path.mkdir(parents=True, exist_ok=True)

    with (tokenizer_path / "config.json").open("w") as fl:
        json.dump({"model_type": "gpt2"}, fl)

    model.save_pretrained(model_path)
    tokenizer.save_pretrained(tokenizer_path)

    if verbose:
        print(
            "Saved the model to ",
            formatter(str(model_path), color="g", bold=True, tick=True),
        )
        print(
            "Saved the tokenizer to ",
            formatter(str(tokenizer_path), color="g", bold=True, tick=True),
        )


def load_transformers(
    model_path: Union[Path, str] = None,
    tokenizer_path: Union[Path, str] = None,
    verbose: bool = False,
) -> Tuple["nn.Module", "transformer.PreTrainedTokenizer"]:

    model_path, tokenizer_path = Path(model_path), Path(tokenizer_path)

    assert (
        model_path.exists() and tokenizer_path.exists()
    ), "Both model and tokenizer path must exist."

    tokenizer = get_tokenier(tokenizer_path)
    model = get_model(model_path, tokenizer)

    if verbose:
        print(
            "Loaded the model from ",
            formatter(str(model_path), color="g", bold=True, tick=True),
        )
        print(
            "Loaded the tokenizer from ",
            formatter(str(tokenizer_path), color="g", bold=True, tick=True),
        )

    return model, tokenizer
