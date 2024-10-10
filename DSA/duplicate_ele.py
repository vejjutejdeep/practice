def find_dup(arr):
    dup = []
    b = []
    [b.append(i) if i not in b else dup.append(i) for i in arr ]
    print(b)
    return dup

arr = [1,3,4,2,2]
print(find_dup(arr))
arr = [3,1,3,4,2]
print(find_dup(arr))