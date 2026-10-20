import numpy as np

def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	x = np.array(apples)
	n = len(x)

	unq = np.unique(x)

	sum_part = 0

	for i in unq:
		p = np.sum(x == i) / n
		sum_part += (p**2)

	return 1 - sum_part