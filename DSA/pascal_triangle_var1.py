def find_term(row,col):
    row -= 1
    col -= 1
    res = 1
    for c in range(col):

        res = res * (row - c)
        res = res // (c+1)
    return res

print(find_term(5,3))
print(find_term(4,3))
print(find_term(2,1))
print(find_term(6,4))