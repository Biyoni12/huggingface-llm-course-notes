# Setup Guide ⚙️

## Overview 🌟
Set up your environment for the Hugging Face LLM Course with ease! 🚀

## Option 1: Google Colab ☁️
- Open [Google Colab](https://colab.research.google.com) 🖥️.
- Create a new notebook 📝.
- Install Transformers:
  ```python
  !pip install transformers
  ```
- Start coding with examples in `code_examples/` 🐍.

## Option 2: Local Environment 💻
1. **Install Python** 🐍:
   - Download Python 3.8+ from [python.org](https://www.python.org).
2. **Create a Virtual Environment** ⚙️:
   ```bash
   python -m venv transformers-course
   source transformers-course/bin/activate  # Windows: transformers-course\Scripts\activate
   ```
3. **Install Dependencies** 📦:
   ```bash
   pip install transformers datasets tokenizers torch gradio
   ```
4. **Verify Installation** ✅:
   ```python
   from transformers import pipeline
   print(pipeline("sentiment-analysis")("Hello, world!"))
   ```

## Tips 💡
- Use Colab for quick setup ☁️.
- Ensure a GPU for faster training (optional) 🚀.
- Check [Hugging Face Documentation](https://huggingface.co/docs) for help 📚.
