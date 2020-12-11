# Import libraries
from google.cloud import vision
import io
import os

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image from local
source_image = "path/to/image"
with open(source_image, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform object detection
print("Detecting objects from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.object_localization(image=image, max_results=5)
objects = response.localized_object_annotations

# Count detected objects
if objects:
    print("found {} object{}\n".format(
        len(objects), "" if len(objects) == 1 else "s"))
else:
    print("no object detected")

# Shows faces information
for object in objects:
    confidence = int(object.score * 100)
    # vertices = (["({:.4f},{:.4f})".format(vertex.x, vertex.y) 
    #             for vertex in object.bounding_poly.normalized_vertices])
    print("{} ({}% confidence)".format(object.name, confidence))
    # print("\tNormalized bounds: {}".format(", ".join(vertices)))