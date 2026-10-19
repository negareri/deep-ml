def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	values = []
	row_idx = []
	col_ptr = [0]

	n_cols = len(dense_matrix[0])
	n_row = len(dense_matrix)

	for i in range(n_cols):
		for j in range(n_row):
			if dense_matrix[j][i] != 0:
				values.append(dense_matrix[j][i])
				row_idx.append(j)
		col_ptr.append(len(values))

	return (values, row_idx, col_ptr)
			


