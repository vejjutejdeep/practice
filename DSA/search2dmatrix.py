def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return False


def search(matrix, target):
    for i in range(len(matrix)):
        if matrix[i][0] <= target and matrix[i][len(matrix[i]) -1] >= target:
            col = binary_search(matrix[i],target)
            if col:
                return (i,col)
    return False


def search_optim(martrix, target):

    n = len(matrix)
    m = len(matrix[0])
    low = 0
    high = n * m

    while low <= high:

        mid = (low + high) // 2
        mid_ele = martrix[mid // m][mid % m]
        # print("middle", mid)
        # print("mid element", mid_ele, mid // m, mid % m)
        if mid_ele == target:
            return (mid // m , mid % m)
        elif mid_ele < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(search(matrix, 8))
print(search_optim(matrix, 8))
matrix = [[1,2,4],[6,7,8],[9,10,34]]
print(search(matrix, 34))
print(search_optim(matrix, 34))