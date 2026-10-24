import numpy as np

def svm_margin_width(w: np.ndarray) -> float:
    """
    Calculate the margin width of a linear SVM classifier.
    
    Parameters:
    w : np.ndarray - weight vector defining the hyperplane
    
    Returns:
    float - the total margin width
    """
    if w.size == 0:
        return 0.0
        
    l2_norm = np.sqrt(np.sum(np.power(w, 2)))

    return 2 / l2_norm