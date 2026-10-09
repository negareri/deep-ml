
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	y = np.array(y)

	classes = np.unique(y)

	sums = 0

	n = len(y)

	for i in classes:
		num = np.sum(y == i)
		p = num/n
		sums += (p**2)

	val = 1 - sums
	
	return round(val,3)

