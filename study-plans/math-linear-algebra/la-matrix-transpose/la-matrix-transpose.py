import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    a = np.array(A,dtype=np.float64)
    r,c = a.shape
    x = np.empty((c,r))
    for i in range(r):
        for j in range(c):
            x[j,i] = a[i,j]
    return x  