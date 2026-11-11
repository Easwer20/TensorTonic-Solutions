import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    a = np.array(A,dtype=np.float64)
    return np.transpose(a)