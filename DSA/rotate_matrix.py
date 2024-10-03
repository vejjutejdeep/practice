def rotate_matrix(matrix):
    new_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    # print(new_matrix)
    n =len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[j][(n-1) -i] = matrix[i][j]
    return new_matrix

def rotate_inplace(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i +1, n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        for j in range((n // 2)):
            # print(i,j)
            matrix[i][j], matrix[i][(n - 1) - j] = matrix[i][(n - 1) - j],matrix[i][j]
    for j in range(n):
        print(matrix[j])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(matrix)):
#     print(matrix[i],end="\n")
new_matrix = rotate_matrix(matrix)
rotate_inplace(matrix)
for i in range(len(matrix)):
    print(new_matrix[i],end="\n")

matrix =  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# for i in range(len(matrix)):
#     print(matrix[i],end="\n")
new_matrix = rotate_matrix(matrix)
rotate_inplace(matrix)
for i in range(len(matrix)):
    print(new_matrix[i],end="\n")