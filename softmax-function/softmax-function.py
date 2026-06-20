import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x=np.array(x)
    softmax_func = np.exp(x - np.max(x,axis=-1,keepdims=True))
    softmax_function = softmax_func / np.sum(softmax_func,axis=-1,keepdims=True)
    return softmax_function