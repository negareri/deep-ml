import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""

	exp_x = np.exp(x)
	s = exp_x / np.sum(exp_x)

	J = np.zeros((len(x), len(x)))

	for i in range(len(x)):
		for j in range(len(x)):
			if i == j:
				J[i][j] = s[i] * (1 - s[i])
			else:
				J[i][j] = -s[i] * s[j]

	return J