import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data = np.array(data)
    n = len(data)

    if n == 0:
        raise ValueError("Data must not be empty.")

    mean = np.sum(data) / n

    data_sort = np.sort(data)

    if n % 2 == 0:
        median = (data_sort[n // 2 - 1] + data_sort[n // 2]) / 2
    else:
        median = data_sort[n // 2]

    unique_values, counts = np.unique(data, return_counts=True)
    mode = unique_values[np.argmax(counts)]

    variance = np.sum((data - mean) ** 2) / n
    standard_deviation = np.sqrt(variance)

    q1, q2, q3 = np.percentile(data, [25, 50, 75])

    iqr = q3 - q1

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": standard_deviation,
        "25th_percentile": q1,
        "50th_percentile": q2,
        "75th_percentile": q3,
        "interquartile_range": iqr
    }
 