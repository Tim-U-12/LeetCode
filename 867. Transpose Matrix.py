def transpose(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose(matrix)