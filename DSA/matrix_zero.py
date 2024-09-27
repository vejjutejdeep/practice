def recreate_col(matrix,col):
    for j in range(len(matrix)):
        if matrix[j][col] != 0:
            matrix[j][col] = -1
    return matrix

def recreate_row(matrix,row):
    for i  in range(len(matrix[row])):
        if matrix[row][i] != 0:
            matrix[row][i] = -1
    return matrix

def replace_zero(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

def create_zero(matrix):
    row = len(matrix[0])
    col = len(matrix)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                matrix = recreate_row(matrix, i)
                matrix = recreate_col(matrix, j)
    matrix = replace_zero(matrix)
    return(matrix)

matrix = [[1,0,1],[1,1,1],[0,1,1]]
print(create_zero(matrix))
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(create_zero(matrix))