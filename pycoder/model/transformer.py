from transformers import AutoTokenizer

# from pycoder.config import SPECIAL_TOKENS

tokenizer = AutoTokenizer.from_pretrained("gpt2-medium")
print(type(tokenizer))
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# print(tokenizer.all_special_tokens)
# tokenizer.add_special_tokens(SPECIAL_TOKENS)
# print(tokenizer.all_special_tokens)
# print(type(tokenizer))

# tokens = tokenizer.encode("Apple doesn't fall far away from tree.")

# # print(tokens)
# tokenizer(return_tensors="pt")
