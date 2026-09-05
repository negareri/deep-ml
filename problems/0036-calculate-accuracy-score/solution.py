import numpy as np

def accuracy_score(y_true, y_pred):

	correct_preds = []

	for i in range(len(y_pred)):
		if y_true[i] == y_pred[i]:
			correct_preds.append(1)

	return len(correct_preds) / len(y_pred)