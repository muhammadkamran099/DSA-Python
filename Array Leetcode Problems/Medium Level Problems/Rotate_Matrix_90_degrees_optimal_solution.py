def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i].reverse()

    return matrix
