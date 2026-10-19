import numpy as np

def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))

	if tp == 0 and fp == 0:
		return 0.0
	if tp == 0 and fn == 0:
		return 0.0

	precision = tp / (tp + fp)
	
	recall = tp / (tp + fn)

	f1 = 2 * ((precision*recall) / (precision+recall))

	return round(f1,3)