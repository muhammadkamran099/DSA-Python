def mark_infinity(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        if matrix[i][col] != 0:
            matrix[i][col] = float("inf")

    for j in range(cols):
        if matrix[row][j] != 0:
            matrix[row][j] = float("inf")


def set_zeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                mark_infinity(matrix, i, j)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

    return matrix


matrix = [
    [7, 9, 2, 3],
    [20, 8, 0, 10],
    [29, 0, -10, 5],
    [4, 14, 6, 7]
]

result = set_zeros(matrix)
print(result)
