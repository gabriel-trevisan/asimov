from PIL import Image 
import os 

reduct_fact = 0.5
compressed_path = "compressed_images"

if compressed_path not in os.listdir():
    os.mkdir(compressed_path)

files_path = 'photos'
files = [i for i in os.listdir(files_path) if 'jpg' in i]

size_before = 0
size_after = 0

for file in files:
    file_path = os.path.join(files_path, file)
    new_path = os.path.join(compressed_path, file)

    size_before += os.stat(file_path).st_size
    img = Image.open(file_path)

    new_w = int(reduct_fact * img.size[0])
    new_h = int(reduct_fact * img.size[1])

    img = img.resize((new_w, new_h), Image.ANTIALIAS)

    img.save(new_path, 'JPEG', optime=True, quality=90)
    file_stats = os.stat(new_path)
    size_after += file_stats.st_size

dif = (size_before - size_after) / (1024 * 1024)
percent = 100 * dif / size_before * (1024 * 1024)

print(f"Diferença de {round(dif,2)} Megabytes")
print(f"Reduzindo o tamanho das files em {round(percent,2)}%")