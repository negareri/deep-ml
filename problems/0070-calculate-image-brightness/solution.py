
def calculate_brightness(img):

	if not img:
		return -1

	row = len(img[0])
	for i in range(len(img)):
		if len(img[i]) != row:
			return -1

	for column in range(len(img)):
		for row in range(len(img[0])):
			if img[column][row] < 0 or img[column][row] > 255:
				return -1

	sums = 0
	pixels = len(img) * len(img[0])

	for colmun in range(len(img)):
		for row in range(len(img[0])):
			sums += img[colmun][row]
	
	return sums / pixels

