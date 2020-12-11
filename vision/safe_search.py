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

# Perform safe search detection
response = client.safe_search_detection(image=image)
safe = response.safe_search_annotation

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ("UNKNOWN", "VERY_UNLIKELY", "UNLIKELY", 
                    "POSSIBLE", "LIKELY", "VERY_LIKELY")

# Shows safe search results
print("Safe Search result of {}".format(os.path.basename(source_image)))
print("Adult    : {}".format(likelihood_name[safe.adult]))
print("Spoof    : {}".format(likelihood_name[safe.spoof]))
print("Medical  : {}".format(likelihood_name[safe.medical]))
print("Violence : {}".format(likelihood_name[safe.violence]))
print("Racy     : {} ".format(likelihood_name[safe.racy]))