import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:

    H, W, C = x.shape

    result = []

    for c in range(C):
        result.append(np.sum(x[:,:,c]) /(H*W) )

    return result