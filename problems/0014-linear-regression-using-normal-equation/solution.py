import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)

	X_T = X.T
	equation = np.linalg.inv(X_T @ X) @ (X_T @ y)
	theta = np.round(equation, 4).tolist()
	
	return theta