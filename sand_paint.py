from PIL import Image
from random import randint
from sys import argv

image_path = argv[1]
original_image = Image.open(image_path)
new_image = Image.new('L', original_image.size, 255)
length, width = original_image.size

original_image = original_image.convert('L')

PEN_SIZE = 5
COLOR_DIFF = 15
LINE_LEN = 3
S_COLOR_LIGHT = 5
S_COLOR_DARK = 75

for i in range(PEN_SIZE+1, length-PEN_SIZE-1):
	for j in range(PEN_SIZE+1, width-PEN_SIZE-1):
		originalcolor = 255 - randint(S_COLOR_LIGHT, S_COLOR_DARK)
		new_image.putpixel((i, j), originalcolor)
		#左右
		left_color = sum([original_image.getpixel((i-r, j))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		right_color = sum([original_image.getpixel((i+r, j))
						   for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(left_color-right_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for p in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i, j+p), originalcolor)
		#上下
		up_color = sum([original_image.getpixel((i, j-r))
						for r in range(PEN_SIZE)]) // PEN_SIZE
		down_color = sum([original_image.getpixel((i, j+r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(up_color-down_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for p in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i+p, j), originalcolor)
		#左上和右下
		leftup_color = sum([original_image.getpixel((i-r, j-r))
						  	for r in range(PEN_SIZE)]) // PEN_SIZE
		rightdown_color = sum([original_image.getpixel((i+r, j+r))
						  	   for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(leftup_color-rightdown_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for p in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i-p, j+p), originalcolor)
		#左下和右上
		rightup_color = sum([original_image.getpixel((i+r, j-r))
						  	 for r in range(PEN_SIZE)]) // PEN_SIZE
		leftdown_color = sum([original_image.getpixel((i-r, j+r))
						for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(rightup_color-leftdown_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for p in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i+p, j+p), originalcolor)

new_image.save('sand_pand.jpg')