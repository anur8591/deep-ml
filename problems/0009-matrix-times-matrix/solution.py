def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    
    a_columns = len(a[0])
    b_row = len(b)
    b_columns = len(b[0])

    if (
        any(len(row) != a_columns for row in a)
        or any(len(row) != b_columns for row in b)
        or a_columns != b_row
    ):
        return -1
    
    return [
        [
            sum(a[row][k] * b[k][col] for k in range(a_columns))
            for col in range(b_columns)
        ]
        for row in range(len(a))
    ]