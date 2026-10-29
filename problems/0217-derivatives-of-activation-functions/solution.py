import numpy as np

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	sigmoid = 1 / (1 + np.exp(-1 * x))
	s = sigmoid * (1 - sigmoid)

	tanh = (np.exp(x) - np.exp(-1 * x)) / (np.exp(x) + np.exp(-1 * x))
	t = 1 - tanh**2

	relu = np.maximum(0, x)
	r = int(x > 0)

	return {'sigmoid': s, 'tanh': t, 'relu': r}
	