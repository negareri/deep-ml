def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """

    def minor_matrix(a, i, j):
        return [
            [a[r][c] for c in range(len(a)) if c != j]
            for r in range(len(a)) if r != i
        ]

    def det(a):
        n = len(a)

        if n == 1:
            return a[0][0]

        if n == 2:
            return a[0][0] * a[1][1] - a[0][1] * a[1][0]

        result = 0

        for j in range(n):
            result += (
                (-1) ** j
                * a[0][j]
                * det(minor_matrix(a, 0, j))
            )

        return result

    determinant = det(matrix)

    trace = sum(matrix[i][i] for i in range(len(matrix)))

    return determinant, trace