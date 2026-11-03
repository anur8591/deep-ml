def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a:
		return []

	columns = len(a[0])

	if len(b) != columns or any(len(row) != columns for row in a):
		return -1
	return [
		sum(value * b[col] for col, value in enumerate(row))
		for row in a
	]