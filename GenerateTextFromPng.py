import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import os

class_ = "4"

def get_text_filename(image_src):
    output_str = ""
    text_file_source = "/home/saraj/Desktop/TextBooks/Online/TEXT/"
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



# read the image using OpenCV
### Copy Path Must be USED(NOT Relative Path)"""####

#image = cv2.imread(image_src)
i = 0
png_directory = '/home/saraj/Desktop/TextBooks/Online/PNG/'  
for filename in os.listdir(png_directory):
    if filename.endswith('.jpg'):
        print("IIIIII", i)
        i += 1
        print("filename- ", filename)
        image_src = png_directory + '/' + filename
        print("imageSrc, " + image_src + "   filename " + filename )
        image = cv2.imread(image_src)
        string = pytesseract.image_to_string(image, lang='ben') ##Generate string form PNG

        text_filename = get_text_filename(image_src)
        #text_filename = '/home/saraj/Desktop/TextBooks/Online/Math Practice Set 3 - kolom.in.txt'  
        print("Text Files Name:", text_filename)
        text_file = open(text_filename, "w")
        n = text_file.write(string)
        text_file.close()





"""Resources:
https://builtin.com/data-science/python-ocr
https://askubuntu.com/questions/793634/how-do-i-install-a-new-language-pack-for-tesseract-on-16-04
https://www.w3schools.com/python/python_file_write.asp
"""