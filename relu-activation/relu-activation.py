import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x=np.array(x)
    ReLU = np.maximum(0,x)
    return ReLU
    