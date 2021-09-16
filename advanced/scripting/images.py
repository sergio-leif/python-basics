# It is necessary to remove the module PIL and install the module Pillow 'pip install Pillow'

from PIL import Image, ImageFilter

img = Image.open('./files/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
print(img.size) # img.size, format, mode...
filtered_img.rotate(90)

resize = filtered_img.resize((300, 300))
resize.save("./files/grey.png", 'png')

# filtered_img.show()

img = Image.open('./files/astro.jpg')
print(img.size)
img.thumbnail((400, 400)) # Mantain the aspect
print(img.size)
img.save('./files/thumbnail.jpg')
