from datasets import load_dataset
from transformers import AutoTokenizer

# Load dataset
dataset = load_dataset("glue", "mrpc")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Preprocess dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True)
tokenized_dataset = dataset.map(tokenize_function, batched=True)

print(tokenized_dataset)
