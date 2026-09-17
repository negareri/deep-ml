import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:

    if len(predicted_probs) != len(true_labels):
        return -1

    loss = []
    for i in range(len(true_labels)):
        probs = np.clip(predicted_probs[i], epsilon, 1)
        loss.append(np.sum(true_labels[i] * np.log(probs)))
    
    return np.sum(loss) / len(predicted_probs) * -1
