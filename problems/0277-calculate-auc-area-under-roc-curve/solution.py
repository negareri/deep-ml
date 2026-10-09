import numpy as np

def calculate_auc(y_true, y_scores):
    """
    Calculate the Area Under the ROC Curve (AUC).
    
    Args:
        y_true: List or array of binary ground truth labels (0 or 1)
        y_scores: List or array of predicted probabilities or confidence scores
        
    Returns:
        AUC value as a float
    """
    tpr = []
    fpr = []

    thrs = np.unique(y_scores)
    thrs = np.sort(thrs)[::-1]
    thrs = np.insert(thrs, 0, np.inf)

    for thr in thrs:
        y_pred = []

        for i in range(len(y_scores)):
            if y_scores[i] >= thr:
                y_pred.append(1)
            else:
                y_pred.append(0)

        tp = 0
        fp = 0
        tn = 0
        fn = 0

        for i in range(len(y_true)):

            if y_true[i] == 1:
                if y_pred[i] == 1:
                    tp += 1
                else:
                    fn += 1

            elif y_true[i] == 0:
                if y_pred[i] == 1:
                    fp += 1
                else:
                    tn += 1
        if (tp + fn) == 0:
            tpr.append(0)
        else:
            tpr.append(tp / (tp + fn))

        if (fp + tn) == 0:
            fpr.append(0)
        else:
            fpr.append(fp / (fp + tn))
            
    auc = 0.0

    for i in range(1, len(fpr)):
        auc += (tpr[i-1] + tpr[i])/2 * (fpr[i] - fpr[i-1])
    
    return auc