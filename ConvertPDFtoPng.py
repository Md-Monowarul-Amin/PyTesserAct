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
#images = convert_from_path('/home/saraj/Desktop/TextBooks/PDF_Files/BCS/10th to 44th BCS Math And Mental ability [ exambd.net ]-.pdf', 250)
images = convert_from_path('/home/saraj/Desktop/TextBooks/Online/Math Practice Set 3 - kolom.in.pdf')
for i in range(len(images)):
    print(i)
      # Save pages as images in the pdf
    images[i].save('/home/saraj/Desktop/TextBooks/Online/PNG'+ convert_into_3_digits(str(i)) +'.jpg', 'JPEG')
