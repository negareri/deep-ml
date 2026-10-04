import numpy as np

def he_initialize(layer_dims: list, method: str = 'normal', seed: int = 42) -> list:
    """
    Initialize weight matrices for a neural network using He initialization.
    
    Args:
        layer_dims: List of integers representing neurons per layer
        method: 'normal' or 'uniform' sampling distribution
        seed: Random seed for reproducibility
    
    Returns:
        List of numpy arrays, one weight matrix per adjacent layer pair
    """

    np.random.seed(seed)

    n_weights = len(layer_dims) -1

    result = []

    if method == 'normal':
        for i in range(n_weights):
            mean = 0
            std = (2/layer_dims[i]) ** 0.5
            shape = layer_dims[i], layer_dims[i+1]

            matrix = np.random.normal(mean, std, size=shape)
            result.append(matrix)

    elif method == 'uniform':
        for i in range(n_weights):
            low = -1 * (6/layer_dims[i]) ** 0.5
            high = (6/layer_dims[i]) ** 0.5
            shape = layer_dims[i], layer_dims[i+1]

            matrix = np.random.uniform(low, high, size=shape)
            result.append(matrix)

    return result