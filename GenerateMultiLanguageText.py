import easyocr
import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os


def get_text_filename(image_src):
    output_str = ""
    text_file_source = "/home/saraj/Desktop/TextBooks/TextFiles/Class9-10_New/"
    output_str += text_file_source
    ok = 0
    temp_filename = ""
    for i in reversed(range(0, len(image_src))):
        if image_src[i] == ".":
            ok = 1
            continue
        if image_src[i] == "/":
            break
        else:
            if ok:
                temp_filename = image_src[i] + temp_filename
            else:
                continue
    
    output_str =  output_str + temp_filename
    output_str = output_str + ".txt"
    return output_str




i=0
png_directory = '/home/saraj/Desktop/TextBooks/PNG_Files/class9-10' 
for filename in os.listdir(png_directory):
    if filename.endswith('.png'):

        #print("filename- ", filename)
        print("IIIIII", i)
        i += 1
        filename_ = png_directory + '/' + filename
        reader = easyocr.Reader(['bn','en']) # this needs to run only once to load the model into memory
        result = reader.readtext(filename_, detail=0)
        image_src = png_directory + '/' + filename
        #print("imageSrc, " + image_src + "   filename " + filename )
        print(str(result))
        text_filename = get_text_filename(image_src)
        #print("Text Files Name:", text_filename)
        output_str = ""
        for line in result:
            output_str = output_str + line + " "
        #print(output_str)
        text_file = open(text_filename, "w")
        n = text_file.write(output_str)
        text_file.close()
 
"""Resource: https://github.com/JaidedAI/EasyOCR"""

