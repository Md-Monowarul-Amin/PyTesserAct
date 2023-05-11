import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


def get_text_filename(image_src):
    output_str = ""
    text_file_source = "/home/saraj/Desktop/OCR/TextFiles/"
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
    
    output_str += temp_filename
    output_str += ".txt"
    return output_str


# read the image using OpenCV
### Copy Path Must be USED(NOT Relative Path)"""####
##image_src = "/home/saraj/Desktop/OCR/Class3_Math-035.png"
image_src = input("Enter Image Source: ")
image = cv2.imread(image_src)
# or you can use Pillow
# image = Image.open("test.png")
###TextFile Source = ""/home/saraj/Desktop/OCR/TextFiles""
# get the string
string = pytesseract.image_to_string(image, lang='ben')

text_filename = get_text_filename(image_src)
### Copy Relative Path Must be USED"""#####
text_file = open(text_filename, "w")
n = text_file.write(string)
text_file.close()

# print it
print(string)
