# Import libraries
from google.cloud import vision
import os
import io

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image from local
source_image = "images/menchies.jpg"
with io.open(source_image, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform logo detection
print("Detecting logos from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.logo_detection(image=image, max_results=5)
logos = response.logo_annotations

# Count logos detected
if logos:
    print("found {} logo{}\n".format(
        len(logos), "" if len(logos) == 1 else "s")) 
else:
    print("no logo detected.")

# Shows logo information
for logo in logos:
    confidence = int(logo.score * 100)
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in logo.bounding_poly.vertices])
    print("{} ({}% confidence)".format(logo.description, confidence))
    print("\tBounds : {}".format(','.join(vertices))) 
