import numpy as np

def shuffle_data(X, y, seed=None):

	if seed is not None:
		np.random.seed(seed)
	
	random_index = np.random.permutation(len(y))

	return X[random_index], y[random_index]