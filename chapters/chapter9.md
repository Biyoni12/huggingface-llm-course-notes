# Chapter 9: Building and Sharing Demos 🌐

## Overview 🌟
Learn to create and share interactive demos using Gradio and Hugging Face Spaces. Show off your models! 🚀

## Key Concepts 💡
- **Gradio** 🖥️:
  - Build web-based interfaces for models.
  - Example: Text input/output interface.
- **Hugging Face Spaces** 🌍:
  - Host demos on the Hub.
  - Share public links.

## Practical Steps ✅
1. **Create a Gradio Demo** 🧑‍💻:
   ```python
   import gradio as gr
   from transformers import pipeline
   classifier = pipeline("sentiment-analysis")
   def predict(text):
       return classifier(text)[0]
   gr.Interface(fn=predict, inputs="text", outputs="text").launch()
   ```
   See `code_examples/gradio_example.py` 🐍.
2. **Deploy to Spaces** 🌐:
   - Create a Space on [huggingface.co](https://huggingface.co).
   - Upload code and `requirements.txt`.
   - Share the link.

## Tips for Beginners 💡
- Start with simple Gradio interfaces ✅.
- Explore existing Spaces for inspiration 📚.
- Use lightweight models for faster demos 🚀.

## Resources 📚
- [Gradio Documentation](https://gradio.app/docs)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Code Example](../code_examples/gradio_example.py)
