# Certificate Generator
import csv
from PIL import Image,ImageFont, ImageDraw
import os

save_path = r"C:\vivek\code\certificate-generator\generated_certificates"

def get_header(csv_file, column_names):

	header = next(csv_file).split(",")
	header_indices = {}

	for column in column_names:
		header_indices[column] = header.index(column)

	return header_indices

def get_certificate(student_detail, coordinates_list, FONT_SIZE, img):

	length_of_list = len(coordinates_list)

	for k in range(length_of_list):
		
		start = coordinates_list[k][0]
		end = coordinates_list[k][1]

		CURSOR_SIZE = 0.52 * FONT_SIZE
		WIDTH =  end[0]- start[0]

		WRITE_TEXT = student_detail[k]

		i = 1

		while (len(WRITE_TEXT)*CURSOR_SIZE) > WIDTH:
			WRITE_TEXT = WRITE_TEXT[:-i] 
			print(i, WRITE_TEXT)
			i+=1 
		
		TEXT_WIDTH =  len(WRITE_TEXT)*CURSOR_SIZE
		PADX = (WIDTH - TEXT_WIDTH) // 2

		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype('OpenSans-Bold.ttf', FONT_SIZE)

		x = draw.multiline_text((start[0] + PADX, start[1]) , WRITE_TEXT, (0, 0, 0), font=font)

	img.save(f"{save_path}\{student_detail[0]}.png")


def get_student_details(csv_file, column_names, coordinates, font_size, img):

	with open(csv_file, "r") as file:
		
		header_indices = get_header(file, column_names)
		csv_reader = csv.reader(file)

		for row in csv_reader:
			student_detail = []

			for column_index in header_indices.values():
				student_detail.append(row[column_index])

			get_certificate(student_detail, coordinates, font_size, img)


img = Image.open("1.jpg")
get_student_details("SJBIT.csv", ["Name", "Course Name"],[[(185,160),(380, 160)],[(140,208),(430,208)]],20, img)

# get_student_details(csv_file_name, list_of_column_name, list_of_tuples_of_coordinates, font_size, image_object)




# start = (185,160)
# end = (380, 160)

# FONT_SIZE = 60
# CURSOR_SIZE = 0.52 * FONT_SIZE
# WIDTH =  end[0]- start[0]
# WRITE_TEXT = "Vidyadhar"

# i = 1
# while (len(WRITE_TEXT)*CURSOR_SIZE) > WIDTH:
# 	WRITE_TEXT = WRITE_TEXT[:-i] 
# 	print(i, WRITE_TEXT)
# 	i+=1 

# TEXT_WIDTH =  len(WRITE_TEXT)*CURSOR_SIZE
# PADX = (WIDTH - TEXT_WIDTH) // 2

# img = Image.open("1.jpg")
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('OpenSans-Bold.ttf', FONT_SIZE)


# x = draw.multiline_text((start[0] + PADX, start[1]) , WRITE_TEXT, (0, 0, 0), font=font)
# print(x)
# img.save("my-image.png")

