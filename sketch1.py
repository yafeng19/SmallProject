from PIL import Image
from sys import argv

image_path = argv[1]
original_image = Image.open(image_path)
new_image = Image.new('L', original_image.size, 255)
length, width = original_image.size

original_image = original_image.convert('L')

PEN_SIZE = 2
COLOR_DIFF = 6

for i in range(PEN_SIZE+1, length-PEN_SIZE-1):
	for j in range(PEN_SIZE+1, width-PEN_SIZE-1):
		originalcolor = 255
		left_color = sum([original_image.getpixel((i-r, j))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		right_color = sum([original_image.getpixel((i+r, j))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(left_color-right_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 2
			new_image.putpixel((i, j), originalcolor)

		up_color = sum([original_image.getpixel((i, j-r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		down_color = sum([original_image.getpixel((i, j+r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(up_color-down_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 2
			new_image.putpixel((i, j), originalcolor)
new_image.save('pencil_drawing1.jpg')

#https://mp.weixin.qq.com/s/puC5vnbxu-YJo3yEjVMZ1Q