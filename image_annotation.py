import os
import csv

# fake dataset
images = [
    {"filename": "cat_01.jpg", "label": "cat"},
    {"filename": "cat_02.jpg", "label": "cat"},
    {"filename": "dog_01.jpg", "label": "dog"},
    {"filename": "dog_02.jpg", "label": "dog"}
]

with open("image_labels.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["filename", "label"])
    writer.writeheader()
    for img in images:
        writer.writerow(img)

print("Created image_labels.csv with sample annotations.")
