def create_zero(matrix):
    col1 = 1
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if j == 0 and matrix[i][j] == 0:
                col1 = 0
                continue
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(len(matrix) -1, 0,-1):
        for j in range(len(matrix[0]) - 1, 0, -1):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(0,len(matrix[0])):
            matrix[0][j] = 0
    if col1 == 0:
        for i in range(0,len(matrix)):
            matrix[i][0] = 0
    return matrix

matrix = [[1,1,1],[1,0,1],[0,1,1]]
print("Before")
for i in matrix:
    print(i,end="\n")
res_matrix = create_zero(matrix)
print("AFTER")
for i in res_matrix:
    print(i,end="\n")
matrix = [[1,1,1,1],[1,0,1,1],[1,1,1,1],[1,1,1,1]]
print("Before")
for i in matrix:
    print(i,end="\n")
print("AFTER")
res_matrix = create_zero(matrix)
for i in res_matrix:
    print(i,end="\n")