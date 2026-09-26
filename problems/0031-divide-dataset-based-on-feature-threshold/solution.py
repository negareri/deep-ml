import numpy as np

def divide_on_feature(X, feature_i, threshold):

	true = []
	false = []

	for i in range(len(X)):
		if X[i][feature_i] >= threshold:
			true.append(X[i])
		else:
			false.append(X[i])

	return [true, false]