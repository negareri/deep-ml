import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    X = np.asarray(X, dtype=float)
    n, d = X.shape

    feature_indices = range(d)

    all_combos = []
    for k in range(1, degree + 1):
        for combo in combinations_with_replacement(feature_indices, k):
            all_combos.append(combo)

    result = np.zeros((n, len(all_combos) + 1))
    result[:, 0] = 1.0

    for j, combo in enumerate(all_combos, start=1):
        val = np.ones(n)
        for idx in combo:
            val *= X[:, idx]
        result[:, j] = val

    result = np.sort(result, axis=1)

    return result