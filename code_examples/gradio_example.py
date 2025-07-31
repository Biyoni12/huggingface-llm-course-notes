import gradio as gr
from transformers import pipeline

# Initialize pipeline
classifier = pipeline("sentiment-analysis")

# Define prediction function
def predict(text):
    return classifier(text)[0]

# Create Gradio interface
interface = gr.Interface(fn=predict, inputs="text", outputs="text")
interface.launch()
