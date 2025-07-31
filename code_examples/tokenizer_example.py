from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

# Tokenize text
inputs = tokenizer("This is a test", return_tensors="pt")
outputs = model(**inputs)
print(outputs.logits)

# Batch processing
inputs = tokenizer(["Sentence 1", "Sentence 2"], return_tensors="pt", padding=True)
outputs = model(**inputs)
print(outputs.logits)
