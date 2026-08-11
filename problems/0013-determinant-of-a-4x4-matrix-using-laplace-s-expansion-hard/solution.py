def determinant_4x4(matrix: list[list[int|float]]) -> float:

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0

    for col in range(len(matrix)):
        minor = []

        for row in range(1, len(matrix)):
            new_row = []

            for j in range(len(matrix)):
                if j != col:
                    new_row.append(matrix[row][j])

            minor.append(new_row)

        sign = (-1) ** col
        determinant += sign * matrix[0][col] * determinant_4x4(minor)

    return determinant