import numpy as np 

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

	rows_shape = data.shape[0]
	cols_shape = data.shape[1]
	
	miu = []
	std = []
	for i in range(cols_shape):
		column = data[:,i]
		miu.append(np.mean(column))
		std.append(np.std(column))

	standardized_data = np.zeros([rows_shape, cols_shape])
	for i in range(rows_shape):
		for j in range(cols_shape):
			standardized_data[i, j] = ((data[i,j] - miu[j])/std[j])


	x_min = []
	x_max = []

	for i in range(cols_shape):
		column = data[:,i]
		x_min.append(np.min(column))
		x_max.append(np.max(column))

	normalized_data = np.zeros([rows_shape, cols_shape])
	for i in range(rows_shape):
		for j in range(cols_shape):
			normalized_data[i, j] = ((data[i,j] - x_min[j])/(x_max[j] - x_min[j]))

	standardized_data = np.round(standardized_data, 4)
	normalized_data = np.round(normalized_data, 4)
	return standardized_data, normalized_data
