from pycoder.utils import formatter
from pycoder.model.transformer import load_transformers, save_transformers
from pycoder.imports import (
    pipeline,
    Union,
    Path,
    List,
    GPT2LMHeadModel,
    AutoTokenizer,
    rmtree,
)


class CodeInference:
    def __init__(
        self,
        model_path: Union[Path, str],
        tokenizer_path: Union[Path, str],
        control_tokens: dict,
        max_length: int,
        cuda: bool = False,
        verbose: bool = False,
    ):
        check_load_from_model_hub(model_path, tokenizer_path)
        model, tokenizer = load_transformers(model_path, tokenizer_path, verbose)
        model.config.task_specific_params["text-generation"]["max_length"] = max_length

        self.coder = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            config={"max_length": max_length},
            device=0 if cuda else -1,
        )

        self.control_tokens = control_tokens

    def __call__(
        self, topics: Union[List[str], str], description: str, code_prefix: str = ""
    ):
        """
        sends in input:
        <|TOP|>TOPICS<|DES|>DESCRIPTION<|CODE|>

        hopes for the output as:
        <|TOP|>TOPICS<|DES|>DESCRIPTION<|CODE|>CODE<|EOS|>
        """

        if isinstance(topics, list):
            topics = ",".join(topics)

        inp = (
            self.control_tokens["topics_token"]
            + topics
            + self.control_tokens["description_token"]
            + description
            + self.control_tokens["code_token"]
            + code_prefix
        )

        out = self.coder(inp)
        out = list(
            map(
                lambda x: x["generated_text"].split(self.control_tokens["code_token"])[
                    1
                ],
                out,
            )
        )

        return out


def check_load_from_model_hub(
    model_path: Union[Path, str], tokenizer_path: Union[Path, str]
):
    from pycoder.config import HF_HUB_NAME, CACHE_DIR

    model_path = Path(model_path)
    tokenizer_path = Path(tokenizer_path)

    if not model_path.exists() or not tokenizer_path.exists():
        print(
            formatter(
                "\nModel and Tokenizer being downloaded and saved from ModelHub (once only)...\n",
                color="g",
            )
        )

        model = GPT2LMHeadModel.from_pretrained(
            HF_HUB_NAME, cache_dir=CACHE_DIR / "tokenizer"
        )
        tokenizer = AutoTokenizer.from_pretrained(
            HF_HUB_NAME, cache_dir=CACHE_DIR / "model"
        )

        save_transformers(model_path, tokenizer_path, model, tokenizer, verbose=False)

        print(
            formatter("\nModel and Tokenizer saved.", color="g", bold=True, tick=True)
            + "\n"
        )

        rmtree(CACHE_DIR)
