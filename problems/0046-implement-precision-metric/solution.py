import numpy as np
def precision(y_true, y_pred):

	TP = 0
	FP = 0

	for i in range(len(y_true)):
		if y_true[i] == 1 and y_pred[i] == 1:
			TP += 1
		elif y_true[i] == 0 and y_pred[i] ==1:
			FP += 1

	if TP + FP == 0:
		return 0.0

	return TP / (TP+FP)
