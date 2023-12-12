def transpose(matrix: list[list[int]]) -> list[list[int]]:
    '''
        input: 2D matrix represented by list of list
        output: returns a matrix where the row and column's indices have been switched
    '''
    result = [[None] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))