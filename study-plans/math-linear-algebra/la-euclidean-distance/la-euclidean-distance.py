import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    X = np.array(x)
    Y = np.array(y)
    difference = X - Y
    return float(np.sqrt(np.sum(difference**2)))