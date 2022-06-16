import extcolors
import PIL

img = PIL.Image.open('../Clock.jpg')
colors, pixel_count = extcolors.extract_from_image(img)
print(colors)