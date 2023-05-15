import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os


def get_text_filename(image_src):
    output_str = ""
    text_file_source = "/home/saraj/Desktop/TextBooks/TextFiles/class3/"
    output_str += text_file_source
    ok = 0
    temp_filename = ""
    for i in reversed(range(0, len(image_src))):
        if image_src[i] == ".":
            ok = 1
            continue
        if image_src[i] == "-":
            break
        else:
            if ok:
                temp_filename = image_src[i] + temp_filename
            else:
                continue
    
    output_str += temp_filename
    output_str += ".txt"
    return output_str



# read the image using OpenCV
### Copy Path Must be USED(NOT Relative Path)"""####

#image = cv2.imread(image_src)
png_directory = '/home/saraj/Desktop/TextBooks/PDF_Files/class3/'
for filename in os.listdir(png_directory):
    if filename.endswith('.png'):
        image_src = png_directory + filename
        image = cv2.imread(image_src)
        string = pytesseract.image_to_string(image, lang='ben') ##Generate string form PNG

        text_filename = get_text_filename(image_src)
        text_file = open(text_filename, "w")
        n = text_file.write(string)
        text_file.close()


