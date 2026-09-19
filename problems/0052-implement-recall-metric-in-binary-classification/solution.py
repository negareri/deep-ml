import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """

    TP = 0
    FN = 0 

    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            TP +=1 
        elif y_true[i] == 1 and y_pred[i] == 0:
            FN += 1

    if TP + FN == 0:
        return 0.0

    return TP / (TP + FN)
