# JPG-to-PNG-Converter
Converts .jpg files to .png 

## Image Converter
Ran as a script from the command line, it takes the folder arguments (inputFolder, outputFolder) and will convert the images in the inputFolder to .png and place them in the outputFolder.

### Credit
This project was created as part of my learning journey through the Udemy/ZTM Python Development course. I learned how to use the Pillow (PIL Fork) library to manipulate images, and completed the exercise based on course material. Initially, I encountered an issue where images were being saved with a .jpg.png extension, but after reviewing the course solution, I learned how to resolve this by using the os.path.splitext() method.
