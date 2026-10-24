def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    a = 0
    b = 0

    for i in range(len(data)):
      if data[i][0] == x:
        b += 1

        if data[i][1] == y:
          a += 1

    if a == 0 or b == 0:
      return 0.0

    return (round(a/b, 4))