# Created as part of my personal learning process using the course "Course Name" as a resource.
# This project demonstrates my ability to manipulate images with Python using the Pillow library.

import sys  # Import the sys module to handle command line arguments
import os
from PIL import Image

# Get the input folder and output folder paths from the command line arguments
inputFolder, outputFolder = sys.argv[1], sys.argv[2]
print(inputFolder, outputFolder)

# Check if the output folder exists; if not, create it
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Loop through each image file in the input folder
for image in os.listdir(inputFolder): 
    # Open each image and convert it to PNG format
    img = Image.open(f'{inputFolder}{image}')

    # Split the image filename and extension, keeping only the base name (no extension)
    clean_name = os.path.splitext(image)[0] 

    # Save the converted image to the output folder with a .png extension
    img.save(f'{outputFolder}{clean_name}.png', 'png')
