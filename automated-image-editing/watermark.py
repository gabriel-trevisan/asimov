from PIL import Image 
import os

watermark = Image.open('watermark.png')
width_w, height_w = watermark.size

image_path = "watermark_ok"

if image_path not in os.listdir():
    os.mkdir(image_path)

files_path = 'photos'
files = [i for i in os.listdir(files_path) if 'jpg' in i]

for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(image_path, file)

    image = Image.open(file_path)
    w, h = image.size

    base_width = int(0.2 * w )
    w_percent = base_width / float(width_w)
    h_size = int(height_w * w_percent)

    watermark = watermark.resize((base_width, h_size))

    image.paste(watermark, (w - base_width, h - h_size), watermark)
    image.save(new_path)

