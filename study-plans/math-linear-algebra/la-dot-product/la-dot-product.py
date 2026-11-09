import numpy as np

def dot_product(x: list, y: list) -> float:
    X = np.array(x)
    Y = np.array(y)
    return float(X @ Y)