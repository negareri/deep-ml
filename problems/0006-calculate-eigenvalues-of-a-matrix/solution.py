def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	tr = a + d 
	det = (a*d) - (b*c)

	eigenvalues = []
	eigenvalues.append((tr + (tr**2 - 4*det)**0.5 )/2)
	eigenvalues.append((tr - (tr**2 - 4*det)**0.5 )/2)
	return eigenvalues