def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    x_min = min(x)
    x_max = max(x)

    dif = x_max - x_min

    result = []

    for i in range(len(x)):
        a = (x[i] - x_min)/dif
        result.append(round(a, 4))
    
    return result