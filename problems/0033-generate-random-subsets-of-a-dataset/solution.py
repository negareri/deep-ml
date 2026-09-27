import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):

    n = X.shape[0]

    if replacements:
        subset_size = n
    else:
        subset_size = n // 2

    result = []

    for i in range(n_subsets):

        x_subset = []
        y_subset = []
        
        indexes = np.random.choice(n, size=subset_size, replace=replacements)

        x_subset = X[indexes].tolist()
        y_subset = y[indexes].tolist()
        
        result.append((x_subset, y_subset))

    return result
        

    
