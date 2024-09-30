def find_row(row):
    col = 1
    ele_row= [1]
    while row > col:
        ele_row.append(ele_row[col - 1] * (row - col) // col)
        col += 1
    return ele_row

print(find_row(5))
print(find_row(4))
print(find_row(2))
print(find_row(6))