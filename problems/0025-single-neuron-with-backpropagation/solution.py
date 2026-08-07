import numpy as np
import math

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):

	weights = initial_weights.copy()
	bias = initial_bias

	m = len(features)
	n = len(features[0])

	mse = []

	for i in range(epochs):

		probabilities = []
		for i in range(m):
			z = bias
			for j in range(n):
				z += features[i][j] * weights[j]
			phi = 1 / (1 + math.exp(-z))
			probabilities.append(phi)

		a = 0
		for i in range(len(probabilities)):
			a += (probabilities[i] - labels[i])**2
		mse.append((1/m)*a)

		delta = []
		for i in range(len(probabilities)):
			delta.append(2 * (probabilities[i] - labels[i]) * (probabilities[i]*(1 - probabilities[i])))

		batch_grad = []
		for i in range(m):
			grad = []
			for j in range(n):
				grad.append(delta[i] * features[i][j])
			batch_grad.append(grad)

		batch_grad = np.mean(batch_grad, axis=0)

		grad_bias = np.mean(delta)

		weights = weights - learning_rate * batch_grad

		bias = bias - learning_rate * grad_bias

	updated_weights = [round(w, 4) for w in weights]

	updated_bias = round(bias, 4)

	mse_values = [round(m, 4) for m in mse]

	return updated_weights, updated_bias, mse_values