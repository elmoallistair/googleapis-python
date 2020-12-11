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

# Perform properties detection
print("Detecting colors from {}...\n".format(
    os.path.basename(source_image)))
response = client.image_properties(image=image, max_results=5)
properties = response.image_properties_annotation

# Display color information
print("Detected colors:")
sum_frac = 0
for color in properties.dominant_colors.colors:
    coverage = color.pixel_fraction * 100
    col = color.color
    rgb = tuple(map(int, (col.red, col.green, col.blue)))
    hex = '#%02x%02x%02x' % rgb
    print("{} ({:.2f}% coverage)".format(hex, coverage))
    sum_frac += coverage

if 1-sum_frac/100 > 0:
    print("Other ({:.2f}% coverage)".format(1-sum_frac/100))