import numpy as np

def hadamard_product(A: list, B: list) -> np.ndarray:
    a = np.array(A,dtype = np.float64)
    b = np.array(B,dtype = np.float64)
    r,c = a.shape
    x = np.empty((r,c))
    for i in range(r):
        for j in range(c):
            x[i,j] = a[i,j] * b[i,j]
    return x