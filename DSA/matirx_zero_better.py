
def create_zero(matrix):
    row_matrix = [0] * len(matrix[0])
    col_matrix = [0] * len(matrix)
    for row in range(len(row_matrix)):
        for col in range(len(col_matrix)):
            if matrix[row][col] == 0:
                row_matrix[row] = 1
                col_matrix[col] = 1
    for row in range(len(row_matrix)):
        for col in range(len(col_matrix)):
            if row_matrix[row] or col_matrix[col]:
                matrix[row][col] = 0
    return matrix



matrix = [[1,0,1],[1,1,1],[0,1,1]]
print(create_zero(matrix))
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(create_zero(matrix))