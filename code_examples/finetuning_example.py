from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset and model
dataset = load_dataset("glue", "mrpc")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

# Tokenize dataset
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True)
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Set up training
training_args = TrainingArguments(
    output_dir="my_model",
    per_device_train_batch_size=16,
    num_train_epochs=3
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"]
)

# Train model
trainer.train()
