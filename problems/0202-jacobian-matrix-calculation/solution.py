import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	f0 = f(x)
	n = len(x)
	m = len(f0)
	
	J = [[0.0] * n for _ in range(m)]

	for j in range(n):
		x_h = x.copy()
		x_h[j] += h
		f_h = f(x_h)
		
		for i in range(m):
			J[i][j] = (f_h[i] - f0[i]) / h
			
	return J