import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:

	y = np.sum((np.multiply(X, w)), axis=1)

	mse = np.mean((y_true - y)**2)

	regularization = alpha * np.sum(w**2)

	return mse + regularization
	
