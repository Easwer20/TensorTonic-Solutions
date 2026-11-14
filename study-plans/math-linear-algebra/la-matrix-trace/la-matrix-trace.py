import numpy as np

def matrix_trace(A: list) -> float:
    x = np.array(A,dtype=np.float64)
    total=0
    for i in range(len(x)):
        for j in range(len(x[0])):
            if i == j:
                total+=float(x[i][j])
    return total