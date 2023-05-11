import pytesseract
import cv2
import matplotlib.pyplot as plt
from PIL import Image


# read the image using OpenCV
image = cv2.imread("/home/saraj/Desktop/OCR/Class3_Math-035.png")
# or you can use Pillow
# image = Image.open("test.png")

# get the string
string = pytesseract.image_to_string(image, lang='ben')

text_file = open("/home/saraj/Desktop/OCR/new.txt", "w")
n = text_file.write(string)
text_file.close()

# print it
print(string)
