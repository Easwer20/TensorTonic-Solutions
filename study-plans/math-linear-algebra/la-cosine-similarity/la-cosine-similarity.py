import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    X=np.array(a)
    Y=np.array(b)
    Z = np.dot(X,Y)
    if np.linalg.norm(X) * np.linalg.norm(Y) == 0.0:
        return 0.0
    return float(Z / (np.linalg.norm(X) * np.linalg.norm(Y)))
    