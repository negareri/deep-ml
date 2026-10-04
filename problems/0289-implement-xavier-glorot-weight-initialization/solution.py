import numpy as np

def xavier_initialization(shape: tuple, mode: str = 'uniform', seed: int = None) -> np.ndarray:
    """
    Implement Xavier/Glorot weight initialization.
    
    Args:
        shape: Tuple of (fan_in, fan_out) representing weight matrix dimensions
        mode: 'uniform' or 'normal' initialization
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Initialized weight matrix as numpy array
    """
    
    np.random.seed(seed)

    if mode == 'normal':
        mean = 0
        std = (2/(shape[0]+shape[1])) ** 0.5

        result = np.random.normal(mean, std, size=shape)


    elif mode == 'uniform':
        low = -1 * (6/(shape[0]+shape[1])) ** 0.5
        high = (6/(shape[0]+shape[1])) ** 0.5

        result = np.random.uniform(low, high, size=shape)

    return result