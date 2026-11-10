import numpy as np

def vector_norms(v: list) -> np.ndarray:
    a = np.array(v,dtype=np.float64)
    l1 = np.sum(np.abs(a))
    l2 = np.sqrt(np.sum(a**2))
    l3 = np.max(np.abs(a))
    return np.array([l1,l2,l3],dtype=np.float64)