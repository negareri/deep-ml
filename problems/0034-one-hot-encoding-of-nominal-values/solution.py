import numpy as np

def to_categorical(x, n_col=None):

    if n_col is None:
        n_col = len(np.unique(x))

    result = []

    for i in range(len(x)):
        row = np.zeros(n_col)
        row[x[i]] = 1
        result.append(row)

    return np.array(result)