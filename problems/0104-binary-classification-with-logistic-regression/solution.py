import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	z = np.sum((weights * X), axis=1) + bias
	z = np.clip(z, -500, 500)

	prediction = 1 / (1 + np.exp(-1 * z))

	binary_prediction = prediction >= 0.5

	return binary_prediction.astype(int)