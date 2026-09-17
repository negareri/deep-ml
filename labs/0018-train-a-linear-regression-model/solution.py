import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """

    ones = np.ones((X.shape[0], 1))
    X_aug = np.concatenate([X, ones], axis=1)

    theta = np.linalg.lstsq(X_aug, y, rcond=None)[0]

    W = theta[:-1]
    b = theta[-1]

    return W, b

