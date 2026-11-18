import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    mu = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    x = (data - mu)/std

    A = np.cov(x, rowvar=False, ddof=0)

    eigenvalues, eigenvectors = np.linalg.eigh(A)

    components = eigenvectors[:, -k:]

    for i in range(components.shape[1]):
        v = components[:, i]
        mask = np.abs(v) > 1e-10
        idx = np.argmax(mask)
        if v[idx] < 0:
            v *= -1
        components[:, i] = v

    return np.round(components, 4)