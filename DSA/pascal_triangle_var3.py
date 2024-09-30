def find_row(row):
    row += 1
    col = 1
    ele_row= [1]
    while row > col:
        ele_row.append(ele_row[col - 1] * (row - col) // col)
        col += 1
    return ele_row

def create_trianlge(rows):
    ans = [[1]]
    for i in range(1,rows):
        temp_row = find_row(i)
        ans.append(temp_row)
    return ans

print(create_trianlge(3))
print(create_trianlge(2))
print(create_trianlge(6))