import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	
	x = [0] * len(A)

	for _ in range(n):

		new_x = []
		for i in range(len(x)):

			sum_part = 0
			for j in range(len(x)):
				if j != i:
					sum_part += A[i][j] * x[j]

			new_x.append((b[i] - sum_part) / A[i][i])

		x = new_x

	return x