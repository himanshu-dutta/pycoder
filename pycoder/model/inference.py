from pycoder.imports import pipeline, Union, Path, List
from pycoder.model.transformer import load_transformers


class CodeInference:
    def __init__(
        self,
        model_name: str,
        model_path: Union[Path, str],
        tokenizer_path: Union[Path, str],
        control_tokens: dict,
        max_length: int,
    ):
        model, tokenizer = load_transformers(model_name, model_path, tokenizer_path)

        self.coder = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            config={"max_length": max_length},
        )

        self.control_tokens = control_tokens

    def __call__(self, topics: Union[List[str], str], description: str):
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
