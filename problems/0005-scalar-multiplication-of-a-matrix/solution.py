def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	result = []

	for i in range(len(matrix)):
		row = []
		for j in range(len(matrix[0])):
			row.append(matrix[i][j] * scalar)
		result.append(row)

	return result