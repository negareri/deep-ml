import numpy as np

def batch_iterator(X, y=None, batch_size=64):

	answer = []

	i = 0

	while i < len(X):

		X_batch = X[i : i+batch_size]

		if y is not None:
			y_batch = y[i: i+batch_size]
			answer.append([X_batch, y_batch])
		else:
			answer.append(X_batch)
		
		i += batch_size
	
	return answer

