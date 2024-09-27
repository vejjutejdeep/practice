st = "ababbav"
['a','b','v', 'ab','abb', 'av']
sublist = []
for i in range(len(st)):
    if st[i] not in sublist:
        sublist.append(st[i])
        for j in range(1,i + 1):
            if st[:j] not in sublist:
                sublist.append(st[:j])

print(sublist)
matrix = [[0,1,1], [1,1,1], [0,0,1]]
max = 0
pos = 0
for i in range(len(matrix)):
    count = 0
    j = len(matrix[i]) - 1
    while j >= 0:
        if matrix[i][j] == 1:
            print(i,j)
            count +=1
        else:
            print("enter")
            break
        j -= 1
    print("count",count)
    if max < count:
        pos = i
        max = count
print(i) 