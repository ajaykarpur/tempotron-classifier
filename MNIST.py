import os
from PIL import Image

from classes import MNISTImage

# returns a list of MNISTImage files for a given input image
def imagelist(digit, filename, save=True):
	images = []
	dataset = Image.open(filename) # image containing all test images
	m, n = dataset.size

	if (save == True):
		dirname = filename.split(".")[0]

		if "data/" not in dirname:
			dirname = "data/" + dirname

		if not os.path.exists(dirname):
			os.makedirs(dirname)

	# returns a list of values for a 28x28 image starting at the input
	def makeimage(i, j):
		values = []

		for y in range(i,i+28):
			for x in range(j,j+28):
				values.append(dataset.getpixel((x,y)))

		return values

	for i in range(0, n, 28):
		for j in range(0, m, 28):
			image = Image.new('L',(28,28))
			data = makeimage(i,j)
			if (data != ([0] * 784)):
				image.putdata(data)
				images.append(MNISTImage(digit,image,data))
				if (save == True):
					# if not os.listdir(dirname):
					image.save(dirname + "/" + str(i/28) + ", " + str(j/28) + ".jpg",'JPEG')

	return images
