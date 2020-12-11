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

# Perform text detection
print("Detecting texts from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.text_detection(image=image, max_results=5)
annotation = response.full_text_annotation

# Count detected characters
texts = annotation.text.rstrip()
if texts:
    print("found {} character{}\n".format(
        len(texts), "" if len(texts) == 1 else "s")) 
    print("Detected text : {}".format(repr(texts)))
else:
    print("no text detected")