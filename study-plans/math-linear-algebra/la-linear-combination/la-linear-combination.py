import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    a = np.array(vectors,dtype=np.float64)
    b = np.array(coefficients,dtype=np.float64)
    return np.array(b @ a,dtype=np.float64)