def rotate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[j][cols - 1 - i] = matrix[i][j]

    return result

matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16] ]

print(rotate_matrix(matrix))
