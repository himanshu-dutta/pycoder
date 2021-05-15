from pycoder.data.classes import Code
from pycoder.imports import Dataset, List, Dict
from pycoder.data.processing import sentence_tokenize_and_select_random


class CodeDataset(Dataset):
    def __init__(
        self,
        codes: List[Code],
        tokenizer: "transformer.PreTrainedTokenizer",
        control_tokens: dict,
        max_length: int,
        num_description_sentences: int,
    ) -> None:
        self.codes = codes
        self.tokenizer = tokenizer
        self.control_tokens = control_tokens
        self.max_length = max_length
        self.num_description_sentences = num_description_sentences

    def get_formatted_code(self, index: int) -> str:
        """
        returns a string with the format:
        <|TOP|>TOPICS<|DES|>DESCRIPTION<|CODE|>CODE<|EOS|>
        """
        code = self.codes[index]
        content = code.content
        description = sentence_tokenize_and_select_random(
            code.readme, self.num_description_sentences
        )
        topics = ",".join(code.topics) if len(code.topics) else ""
        topics = code.category + "," + topics

        return (
            self.control_tokens["topics_token"]
            + topics
            + self.control_tokens["description_token"]
            + description
            + self.control_tokens["code_token"]
            + content
            + self.control_tokens["eos_token"]
        )

    def __len__(self) -> int:
        return len(self.codes)

    def __getitem__(self, index: int) -> Dict[str, "torch.tensor"]:
        formatted_code = self.get_formatted_code(index)

        tokenized = self.tokenizer(
            formatted_code,
            truncation=True,
            max_length=self.max_length,
            padding="max_length",
            return_tensors="pt",
        )

        return {
            "label": tokenized["input_ids"],
            "input_ids": tokenized["input_ids"],
            "attention_mask": tokenized["attention_mask"],
        }

    def get_string(self, index: int) -> str:
        formatted_code = self.get_formatted_code(index)
        return formatted_code
