import numpy as np

def online_simple_regression(xs, ys):
    # return (N, 2) array of (w0, w1) after each point
    result = []
    
    n = 0
    mean_x = 0.0
    mean_y = 0.0
    c_xx = 0.0
    c_xy = 0.0
    
    for i in range(len(xs)):
        n += 1

        dx = xs[i] - mean_x
        dy = ys[i] - mean_y

        mean_x += dx / n
        mean_y += dy / n

        dx2 = xs[i] - mean_x
        dy2 = ys[i] - mean_y

        c_xx = ((n-1) * c_xx + dx * dx2) / n
        c_xy = ((n-1) * c_xy + dx * dy2) / n

        if c_xx == 0:
            w1 = 0.0
            w0 = mean_y
        else:
            w1 = c_xy / c_xx
            w0 = mean_y - w1 * mean_x
        
        result.append([w0, w1])
    
    return np.array(result)
