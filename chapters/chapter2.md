# Chapter 2: Using Pretrained Models and Tokenizers 🛠️

## Overview 🌟
Learn to use pretrained models and tokenizers from the Hugging Face Transformers library. This chapter covers loading models, tokenizing text, and running NLP tasks. 🚀

## Key Concepts 💡
- **Pretrained Models** 🤖:
  - Models like BERT or GPT, ready for tasks like classification.
  - Access via `AutoModel` and `AutoTokenizer`.
- **Tokenization** ✂️:
  - Converts text to numerical tokens (e.g., "Hello, world!" → [101, 7592, 1010, 2088, 999, 102]).
- **Pipeline API** 🎮:
  - Simplifies tasks like text generation or classification.
- **Tokenizer API** 📝:
  - Handles text preprocessing and batch processing.

## Practical Steps ✅
1. **Load a Model and Tokenizer** ⚙️:
   ```python
   from transformers import AutoModelForSequenceClassification, AutoTokenizer
   model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
   tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
   ```
2. **Tokenize Text** 🧑‍💻:
   ```python
   inputs = tokenizer("This is a test", return_tensors="pt")
   outputs = model(**inputs)
   print(outputs.logits)
   ```
3. **Batch Processing** 📚:
   ```python
   inputs = tokenizer(["Sentence 1", "Sentence 2"], return_tensors="pt", padding=True)
   outputs = model(**inputs)
   print(outputs.logits)
   ```
   See `code_examples/tokenizer_example.py` 🐍.

## Tips for Beginners 💡
- Try different models from the Hub 🌐.
- Use `padding=True` for varying input lengths ✅.
- Check model cards for task details 📖.

## Resources 📚
- [Transformers Documentation](https://huggingface.co/docs/transformers)
- [Code Example](../code_examples/tokenizer_example.py)
