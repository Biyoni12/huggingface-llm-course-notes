from transformers import pipeline

# Initialize a sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Test the pipeline
text = "I love learning about AI!"
result = classifier(text)
print(result)  # Expected output: [{'label': 'POSITIVE', 'score': 0.999}]
