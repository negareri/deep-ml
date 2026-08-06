def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	means = []
	
	if mode == "row":
		for row in matrix:
			means.append(sum(row) / len(row))
			
	elif mode == "column":
		cols = len(matrix[0])
		rows = len(matrix)
		
		for j in range(cols):
			col_sum = 0
			for i in range(rows):
				col_sum += matrix[i][j]
			means.append(col_sum / rows)
	return means