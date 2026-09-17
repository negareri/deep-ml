import numpy as np

def compare_softmax(scores: list) -> dict:
    """Compare naive and numerically stable softmax."""

    scores = np.array(scores)

    exp_scores = np.exp(scores)

    if np.any(np.isinf(exp_scores)):
        naive = np.full_like(scores, np.nan, dtype=float)
    else:
        naive = exp_scores / np.sum(exp_scores)
    
    stable_scores = np.exp(scores - np.max(scores))
    stable = stable_scores / np.sum(stable_scores)

    if np.any(np.isnan(naive)):
        max_abs_diff = float('nan')
    else:
        diff = np.abs(naive - stable)
        max_abs_diff = round(float(np.max(diff)), 6)

    return {
        'naive': np.round(naive, 6).tolist(),
        'stable': np.round(stable, 6).tolist(),
        'max_abs_diff': max_abs_diff
    }