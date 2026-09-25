import numpy as np
from typing import Tuple

def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    """Return the (feature_index, threshold) that minimises weighted Gini impurity."""
    
    def G(labels):
        n = len(labels)
        if n == 0:
            return 0.0
        p1 = sum(labels) / n
        p0 = 1 - p1
        return 1 - (p0**2 + p1**2)

    best_g = float('inf')
    best_feature = None
    best_threshold = None
    n_total = len(y)

    for j in range(X.shape[1]):
        col = X[:, j]
        for thr in np.unique(col):
            mask = col <= thr
            y_left  = y[mask]
            y_right = y[~mask]

            g = (len(y_left)/n_total) * G(y_left) \
              + (len(y_right)/n_total) * G(y_right)

            if g < best_g:
                best_g = g
                best_feature = j
                best_threshold = thr

    return best_feature, best_threshold