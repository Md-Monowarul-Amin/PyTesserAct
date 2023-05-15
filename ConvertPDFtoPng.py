# import module
from pdf2image import convert_from_path
 

def convert_into_3_digits(i):
  if len(i) == 3:
     return i
  else:
     for j in range(3- len(i)):
      i = "0" + i 
      return i
 
# Store Pdf with convert_from_path function
images = convert_from_path('/home/saraj/Desktop/TextBooks/PDF_Files/class4/Class-4 Mathematics Final OPT.pdf', 200)
 
for i in range(len(images)):
   
      # Save pages as images in the pdf
    images[i].save('/home/saraj/Desktop/TextBooks/PNG_Files/class4/'+ convert_into_3_digits(str(i)) +'.png', 'JPEG')
