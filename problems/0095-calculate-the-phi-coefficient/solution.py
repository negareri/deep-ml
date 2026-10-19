import numpy as np

def phi_corr(x: list[int], y: list[int]) -> float:
	"""
	Calculate the Phi coefficient between two binary variables.

	Args:
	x (list[int]): A list of binary values (0 or 1).
	y (list[int]): A list of binary values (0 or 1).

	Returns:
	float: The Phi coefficient rounded to 4 decimal places.
	"""
	x = np.array(x)
	y = np.array(y)
	
	x_00 = np.sum((x == 0) & (y == 0))
	x_01 = np.sum((x == 0) & (y == 1))
	x_10 = np.sum((x == 1) & (y == 0))
	x_11 = np.sum((x == 1) & (y == 1))

	a = (x_00 * x_11) - (x_01 * x_10)
	b = ((x_00 + x_01)*(x_10 + x_11)*(x_00 + x_10)*(x_01 + x_11))**0.5

	if b == 0:
		return 0.0

	val = a/b

	return round(val,4)