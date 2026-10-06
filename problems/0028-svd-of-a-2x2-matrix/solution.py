import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    y1 = A[1, 0] + A[0, 1]
    x1 = A[0, 0] - A[1, 1]

    y2 = A[1, 0] - A[0, 1]
    x2 = A[0, 0] + A[1, 1]

    h1 = np.sqrt(y1**2 + x1**2)
    h2 = np.sqrt(y2**2 + x2**2)

    sigma1 = (h1 + h2) / 2
    sigma2 = abs(h1 - h2) / 2

    s = np.array([sigma1, sigma2])

    theta_u = 0.5 * np.arctan2(y1, x1)
    theta_v = 0.5 * np.arctan2(y2, x2)

    U = np.array([
        [np.cos(theta_u), -np.sin(theta_u)],
        [np.sin(theta_u),  np.cos(theta_u)]
    ])

    S = np.diag(s)

    V = np.linalg.solve(S, U.T @ A)

    return U, s, V
