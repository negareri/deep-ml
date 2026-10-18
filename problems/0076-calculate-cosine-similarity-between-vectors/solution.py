import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	if len(v1) != len(v2):
		return -1
	
	dot_product = np.dot(v1, v2)

	a = (np.sum(v1**2))**0.5
	b = (np.sum(v2**2))**0.5

	return dot_product / (a * b)