import numpy as np

def r_squared(y_true, y_pred):
	
	ssr = 0
	sst = 0

	y_mean = np.mean(y_true)

	ssr = np.sum((np.subtract(y_true, y_pred))**2)
	sst = np.sum((np.subtract(y_true, y_mean))**2)
	
	return 1 - ssr/sst
