# Import libraries
from google.cloud import vision
import io
import os

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image from local
source_image = "path/to/image"
with io.open(source_image, "rb") as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform label detection
print("Detecting labels from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.label_detection(image=image, max_results=5)
labels = response.label_annotations

# Count labels detected
if labels:
    print("found {} label{}\n".format(
        len(labels), "" if len(labels) == 1 else "s"))
else:
    print("no label detected")

# Shows label information
for label in labels:
    description = label.description
    confidence = int(label.score * 100)
    print("{} ({}% confidence)".format(description, confidence))