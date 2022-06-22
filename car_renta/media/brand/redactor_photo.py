from PIL import Image

img1 = Image.open('audo.png')
print(img1.size)
new_size = (290, 174)
img1.thumbnail(new_size)
img1.save('Ауди.png')


