import extcolors
import PIL

image = PIL.Image.open('../Clock.jpg')
colors, pixel_count = extcolors.extract_from_image(image)
print(colors)