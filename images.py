from PIL import Image, ImageFilter

# img = Image.open('./pokedex/203 bulbasaur.jpg')
# filtered_image = img.filter(ImageFilter.SHARPEN)
# box  = (100,100,300,300)
# crop_im  = filtered_image.crop(box)
# filtered_image.save("blured_bulb.png" , 'png')
# crop_im.show()

img = Image.open('./pokedex/205 astro.jpg')

re = img.resize((400,400))
re.show()
re = re.filter(ImageFilter.SHARPEN)
re.show()