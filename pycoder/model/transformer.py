from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

tokens = tokenizer.encode("Apple doesn't fall far away from tree.")

print(tokens)
