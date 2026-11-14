import numpy as np

def matrix_multiply(A: list, B: list) -> np.ndarray:
    a = np.array(A,dtype=np.float64)
    b = np.array(B,dtype=np.float64)
    return a @ b