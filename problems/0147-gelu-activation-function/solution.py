import numpy as np

def GeLU(x: np.ndarray) -> np.ndarray:
	
	return 0.5 * x * (1 + np.tanh((2/np.pi)**0.5 * (x + (0.044715 * x**3))))