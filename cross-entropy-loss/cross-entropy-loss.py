import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    samples=len(y_pred)
    y_pred_clipped = np.clip(y_pred,1e-7,1-1e-7)
    if len(y_true.shape) == 1:
        correct_confidence = y_pred_clipped[range(samples),y_true]
    elif len(y_true.shape) == 2:
        correct_confidence =np.sum(y_pred_clipped * y_true,axis=1)


    neg_likehood = -np.log(correct_confidence)

    return np.mean(neg_likehood)