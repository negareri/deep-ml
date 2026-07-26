import numpy as np

def cross_product(a, b):
    i = a[1] * b[2] - a[2] * b[1]
    j = - a[0] * b[2] + a[2] * b[0]
    k = a[0] * b[1] - a[1] * b[0]
    return [i, j, k]