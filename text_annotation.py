# text_annotation_example.py
# Simple rule-based text annotation example
import csv

samples = [
    {"id": 1, "text": "I love this product!"},
    {"id": 2, "text": "This is terrible, very disappointed."},
    {"id": 3, "text": "It's okay, not bad."},
    {"id": 4, "text": "Excellent service and fast delivery."}
]

def annotate(text):
    t = text.lower()
    if any(w in t for w in ["love", "great", "excellent", "good", "awesome", "perfect"]):
        return "positive"
    if any(w in t for w in ["terrible", "disappointed", "bad", "worst", "awful"]):
        return "negative"
    return "neutral"

with open("annotated_texts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "text", "label"])
    writer.writeheader()
    for s in samples:
        writer.writerow({"id": s["id"], "text": s["text"], "label": annotate(s["text"])})

print("Created annotated_texts.csv with sample labels.")
