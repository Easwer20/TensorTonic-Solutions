import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    U = np.array(u,dtype=np.float64)
    V = np.array(v,dtype=np.float64)
    return np.outer(U,V)