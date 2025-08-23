from PIL import Image

image = Image.open("images/image.jpg")

print(image.format)
print(image.mode)
print(image.size)
print(image.width)
print(image.height)

print(image.info)

image.resize(size=(200, 800)).save("images/image2.jpg")

image.crop((0, 0, 300, 300)).save("images/image3.jpg")
