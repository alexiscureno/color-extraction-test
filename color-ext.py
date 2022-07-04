import extcolors
import PIL

images = PIL.Image.open('../Clock.jpg')
colors, pixel_count = extcolors.extract_from_image(images)

print(colors)