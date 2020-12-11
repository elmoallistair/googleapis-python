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

# Perform face detection
print("Detecting faces from {}...".format(
    os.path.basename(source_image)), end=" ")
response = client.face_detection(image=image, max_results=5)
faces = response.face_annotations

# Count detected faces
if faces:
    print("found {} face{}\n".format(
        len(faces), "" if len(faces) == 1 else "s")) 
else:
    print("no face detected")

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ("UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", 
                    "POSSIBLE", "LIKELY", "VERY_LIKELY")

# Shows faces information
for counter, face in enumerate(faces):
    confidence = int(face.detection_confidence * 100)
    vertices = (["({},{})".format(vertex.x, vertex.y) 
        for vertex in face.bounding_poly.vertices])
    print("Face {} ({}% confidence)".format(counter+1, confidence))
    print("\tBounds   : {}".format(",".join(vertices)))
    print("\tAnger    : {}".format(likelihood_name[face.anger_likelihood]))
    print("\tJoy      : {}".format(likelihood_name[face.joy_likelihood]))
    print("\tSurprise : {}".format(likelihood_name[face.surprise_likelihood]))
