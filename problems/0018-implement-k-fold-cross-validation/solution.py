import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """

    indices = np.arange(n_samples)

    if shuffle:
        np.random.shuffle(indices)

    base = n_samples // k
    remain = n_samples % k

    fold_sizes = [base] * k
    for i in range(remain):
        fold_sizes[i] += 1

    folds = []
    start = 0

    for fold_size in fold_sizes:
        end_index = start + fold_size
        folds.append(indices[start:end_index].tolist())
        start = end_index

    splits = []

    for test_fold_index in range(k):
        test_indices = folds[test_fold_index]

        train_indices = []

        for fold_index in range(k):
            if fold_index != test_fold_index:
                train_indices.extend(folds[fold_index])

        splits.append((train_indices, test_indices))

    return splits