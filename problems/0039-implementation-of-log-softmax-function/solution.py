import numpy as np

def log_softmax(scores: list) -> np.ndarray:

	x = scores
	
	m = np.max(x)

	return x - m - np.log(np.sum(np.exp(x - m), axis=0))