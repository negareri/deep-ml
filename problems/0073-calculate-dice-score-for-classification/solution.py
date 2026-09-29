import numpy as np

def dice_score(y_true, y_pred):

    if not isinstance(y_true, np.ndarray) or not isinstance(y_pred, np.ndarray):
        return -1
    if y_true.shape != y_pred.shape:
        return -1
    if y_true.size == 0:
        return -1

    TP = np.sum(y_true & y_pred)
    FP = np.sum(~y_true & y_pred)
    FN = np.sum(y_true & ~y_pred)

	if TP == 0 and FP == 0 and FN == 0:
		return 0.0

    res = (2 * TP) / (2 * TP + FP + FN)

    return round(float(res), 3)