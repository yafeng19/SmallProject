from PIL import Image 
from sys import argv
from random import randint

image_path = argv[1]
original_image = Image.open(image_path)
new_image = Image.new('L', original_image.size, 255)
length, width = original_image.size

original_image = original_image.convert('L')

PEN_SIZE = 3
COLOR_DIFF = 7
LINE_LEN = 2

for i in range(PEN_SIZE+1, length-PEN_SIZE-1):
	for j in range(PEN_SIZE+1, width-PEN_SIZE-1):
		originalcolor = 255
		#左右
		left_color = sum([original_image.getpixel((i-r, j))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		right_color = sum([original_image.getpixel((i+r, j))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(left_color-right_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for k in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i, j+k), originalcolor)
		
		#上下
		up_color = sum([original_image.getpixel((i, j-r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		down_color = sum([original_image.getpixel((i, j+r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(up_color-down_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for k in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i+k, j), originalcolor)
		
		#左上和右下
		leftup_color = sum([original_image.getpixel((i-r, j-r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		rightdown_color = sum([original_image.getpixel((i+r, j+r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(leftup_color-rightdown_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for k in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i-k, j+k), originalcolor)
		
		#左下和右上
		rightup_color = sum([original_image.getpixel((i+r, j-r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		leftdown_color = sum([original_image.getpixel((i-r, j+r))
						  for r in range(PEN_SIZE)]) // PEN_SIZE
		if abs(rightup_color-leftdown_color) > COLOR_DIFF:
			originalcolor -= (255-original_image.getpixel((i, j))) // 4
			for k in range(-LINE_LEN+randint(-1, 1), LINE_LEN+randint(-1, 1)):
				new_image.putpixel((i+k, j+k), originalcolor)
new_image.save('pencil_drawing2.jpg')