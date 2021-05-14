from pycoder.data.classes import Code
from pycoder.imports import Dataset, List, Dict
from pycoder.data.processing import sentence_tokenize_and_select_random


class CodeDataset(Dataset):
    def __init__(
        self,
        codes: List[Code],
        tokenizer: "transformer.PreTrainedTokenizer",
        special_tokens: dict,
        max_length: int,
        num_description_sentences: int,
    ) -> None:
        self.codes = codes
        self.tokenizer = tokenizer
        self.special_tokens = special_tokens
        self.max_length = max_length
        self.num_description_sentences = num_description_sentences

        self.tokenizer.add_special_tokens(self.special_tokens)

    def get_formatted_code(self, index: int) -> str:
        """
        returns a string with the format:
        <|SOS|>TOPICS<|SEP|>DESCRIPTION<|SEP|>CODE<|EOS|>
        """
        code = self.codes[index]
        content = code.content
        description = sentence_tokenize_and_select_random(
            code.readme, self.num_description_sentences
        )
        topics = ",".join(code.topics) if len(code.topics) else ""

        return (
            self.special_tokens["bos_token"]
            + topics
            + self.special_tokens["sep_token"]
            + description
            + self.special_tokens["sep_token"]
            + content
            + self.special_tokens["eos_token"]
        )

    def __len__(self) -> int:
        return len(self.codes)

    def __getitem__(self, index) -> Dict[str, "torch.tensor"]:
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
