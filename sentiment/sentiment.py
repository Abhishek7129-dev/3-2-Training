from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = "you wear a average dress today"
result = classifier(text)

print("Text:", text)
print("Sentiment:", result[0]['label'])
print("Score:", result[0]['score']) 