from PIL import Image

#Lesson 01
image = Image.open("images/image.jpg")

print(image.format)
print(image.mode)
print(image.size)
print(image.width)
print(image.height)

print(image.info)

image.resize(size=(200, 800)).save("images/image2.jpg")

image.crop((0, 0, 300, 300)).save("images/image3.jpg")

#Lesson 02
image = Image.open("images/maca.jpg")
r, g, b = image.split()

Image.merge("RGB", (b, g, r)).save("images/maca2.jpg")

image = Image.open("images/maca.jpg")
image2 = Image.open("images/image.jpg")

image.paste(image2)
image.save("images/merge.jpg")