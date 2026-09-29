import numpy as np

def rmse(y_true, y_pred):

	if not isinstance(y_true, np.ndarray) or not isinstance(y_pred, np.ndarray):
		return -1

	if y_true.shape != y_pred.shape:
		return -1

	if y_true.size == 0 or y_pred.size == 0:
		return -1

	n = y_true.size

	rmse_res = np.sqrt(np.sum((y_true - y_pred)**2) / n)

	return round(rmse_res, 3)
