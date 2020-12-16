# Import libraries
from google.cloud import vision
import io
import os

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image from local
source_image = "images/reog.jpg"
with io.open(source_image, "rb") as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform web detection
print("Detecting webs from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.web_detection(image=image, max_results=5)
annotations = response.web_detection

# Best label
if annotations.best_guess_labels:
    for label in annotations.best_guess_labels:
        print("best guess label: {}".format(label.label))

# Web Entities
if annotations.web_entities:
    print("\nWeb entities found:")
    for entity in annotations.web_entities:
        if entity.description:
            print("\t{} (Score: {:.2f})".format(
                entity.description, entity.score))

# Full matching images
if annotations.full_matching_images:
    print("\nFull Matches found:")
    for image in annotations.full_matching_images:
        print("\tUrl: {}".format(image.url))

# Partial matching images
if annotations.partial_matching_images:
    print("\nPartial Matches found:")
    for image in annotations.partial_matching_images:
        print("\tUrl: {}".format(image.url))

# Pages with matching images
if annotations.pages_with_matching_images:
    print("\nPages with matching images:")
    for page in annotations.pages_with_matching_images:
        print("\tUrl: {}".format(page.url))

# Similiar images
if annotations.visually_similar_images:
    print("\nSimilar images found:")
    for image in annotations.visually_similar_images:
        print("\tUrl: {}".format(image.url))