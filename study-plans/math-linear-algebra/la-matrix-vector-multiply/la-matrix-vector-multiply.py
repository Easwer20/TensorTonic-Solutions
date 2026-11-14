import numpy as np

def matrix_vector_multiply(A: list, x: list) -> np.ndarray:
    a = np.array(A,dtype=np.float64)
    X = np.array(x,dtype=np.float64)
    return a @ X