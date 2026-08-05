import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	def cov(X, Y):
		m = len(X)
		i = 0
		for k in range(m):
			i += (X[k]- np.mean(X)) * (Y[k] - np.mean(Y))
		
		return i / (m-1)

	n_features = len(vectors)

	result = np.zeros((n_features, n_features))
	for i in range(n_features):
		for j in range(n_features):
			result[i, j] = cov(vectors[i], vectors[j])

	return result
        
			