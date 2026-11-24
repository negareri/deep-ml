import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    if len(p) != len(q):
        return 0.0
    elif len(p) == 0 or len(q) == 0:
        return 0.0
    
    p = np.array(p)
    q = np.array(q)

    bc = np.sum(np.sqrt(p * q))
    bd = np.log(bc) * -1

    return bd