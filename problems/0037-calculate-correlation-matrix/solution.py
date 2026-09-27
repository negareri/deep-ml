import numpy as np

def calculate_correlation_matrix(X, Y=None):

	X = np.array(X)

	if Y is None:
		Y = X
	else:
		Y = np.array(Y)

	n = X.shape[0]
	d_x = X.shape[1]
	d_y = Y.shape[1]
	
	X_centered = X - np.mean(X, axis=0)
	Y_centered = Y - np.mean(Y, axis=0)
	
	cov = np.dot(X_centered.T, Y_centered) / n
	
	std_x = np.std(X_centered, axis=0)
	std_y = np.std(Y_centered, axis=0)
	
	corr = cov / np.outer(std_x, std_y)
	
	return corr

