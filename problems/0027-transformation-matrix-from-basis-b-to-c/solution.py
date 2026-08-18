def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:

    def minor(matrix, row, col):
        return [
            [
                matrix[i][j]
                for j in range(len(matrix))
                if j != col
            ]
            for i in range(len(matrix))
            if i != row
        ]

    def determinant(matrix):
        n = len(matrix)

        if n == 1:
            return matrix[0][0]

        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det = 0

        for j in range(n):
            sign = (-1) ** j
            det += sign * matrix[0][j] * determinant(
                minor(matrix, 0, j)
            )

        return det

    det = determinant(C)

    if det == 0:
        raise ValueError("C is not invertible")

    # Cofactor matrix
    cofactors = []

    for i in range(len(C)):
        row = []

        for j in range(len(C)):
            cofactor = (
                (-1) ** (i + j)
                * determinant(minor(C, i, j))
            )

            row.append(cofactor)

        cofactors.append(row)

    # Adjugate = transpose of cofactor matrix
    inverse = [
        [
            cofactors[j][i] / det
            for j in range(len(C))
        ]
        for i in range(len(C))
    ]

    # P = C^-1 B
    result = []

    for i in range(len(inverse)):
        row = []

        for j in range(len(B[0])):
            value = 0

            for k in range(len(inverse[0])):
                value += inverse[i][k] * B[k][j]

            row.append(value)

        result.append(row)

    return result