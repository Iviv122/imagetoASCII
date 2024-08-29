from PIL import Image

RawImage = Image.open("test.jpg")


image = RawImage.resize((100,60)) ## target size 

width = image.width
height = image.height

print(width, " ", height);

ASCII_CHARS = "@%#*+=-:. "


for y in range(0,height):
	for x in range(0,width):
		colors = image.getpixel((x,y))
		LumianceLevel = int((0.2126*colors[0] + 0.7152*colors[1] + 0.0722*colors[2])) 
		index = min(LumianceLevel // (255//len(ASCII_CHARS)), len(ASCII_CHARS)-1)
		print(ASCII_CHARS[index],end="")
	print()
