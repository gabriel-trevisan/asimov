from PIL import Image 
import os 

image_path = "greyscale_images"

if image_path not in os.listdir():
    os.mkdir(image_path)

files_path = 'photos'
files = [i for i in os.listdir(files_path) if '.jpg' in i]

for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(image_path, file)

    image = Image.open(file_path).convert('L')

    image.save(new_path)