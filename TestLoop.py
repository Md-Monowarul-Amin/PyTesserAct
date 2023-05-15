import os

directory = '/home/saraj/Desktop/OCR/TextFiles'
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename)) as f:
            print(f.read())
