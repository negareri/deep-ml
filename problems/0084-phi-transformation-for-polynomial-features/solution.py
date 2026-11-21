def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    """
    Perform a Phi Transformation to map input features into a higher-dimensional space by generating polynomial features.

    Args:
        data (list[float]): A list of numerical values to transform.
        degree (int): The degree of the polynomial expansion.

    """
    result = []

    for i in data:
        a = []
        for d in range(degree+1):
            a.append(i ** d)
        result.append(a)
    
    return result