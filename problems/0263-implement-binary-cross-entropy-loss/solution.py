import numpy as np

def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
    """
    Compute binary cross-entropy loss.
    
    Args:
        y_true: True binary labels (0 or 1)
        y_pred: Predicted probabilities (between 0 and 1)
        epsilon: Small value for numerical stability
    
    Returns:
        Mean binary cross-entropy loss
    """
    y = np.array(y_true)
    p = np.array(y_pred)

    bce = -1 * (y * np.log(p) + (1-y) * np.log(1-p))

    return np.mean(bce)
    
