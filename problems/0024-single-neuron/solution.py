import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	m = len(features)
	n = len(features[0])

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
	mse = (1/m)*a

	probabilities = [round(p, 4) for p in probabilities]
	mse = round(mse, 4)
	return probabilities, mse