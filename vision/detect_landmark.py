# Import libraries
from google.cloud import vision
import io
import os

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image from local
source_image = "path/to/image"
with io.open(source_image, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform landmark detection
print("Detecting landmarks from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.landmark_detection(image=image, max_results=5)
landmarks = response.landmark_annotations

# Count detected landmarks
if landmarks:
    print("found {} landmark{}\n".format(
        len(landmarks), "" if len(landmarks) == 1 else "s")) 
else:
    print("no landmark detected")

# Shows landmarks information
for landmark in landmarks:
    name = landmark.description
    confidence = int(landmark.score * 100)
    vertices = (["({},{})".format(vertex.x, vertex.y) 
        for vertex in landmark.bounding_poly.vertices])
    
    print("{} ({}% confidence)".format(name, confidence))
    print("\tBounds    : {}".format(", ".join(vertices)))
    for location in landmark.locations:
        lat_lng = location.lat_lng
        print("\tLatitude  : {}".format(lat_lng.latitude))
        print("\tLongitude : {}".format(lat_lng.longitude))