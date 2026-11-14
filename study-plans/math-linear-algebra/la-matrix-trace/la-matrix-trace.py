import numpy as np

def matrix_trace(A: list) -> float:
    x = np.array(A,dtype=np.float64)
    total=0
    for index in range(len(x[0])):
        total+=float(x[index,index])
    return total