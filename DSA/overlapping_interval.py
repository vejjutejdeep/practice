def combine_overlapping(arr):
    arr.sort()
    i = 0
    while i < len(arr) -1:
        if arr[i][1] > arr[i + 1] [0] and arr[i][1] < arr[i + 1][1]:
            arr[i][1] = arr[i + 1][1]
            arr.pop(i + 1)
        elif arr[i][1] > arr[i + 1] [0] and arr[i][1] > arr[i + 1][1]:
            arr.pop(i + 1)
        elif arr[i][1] < arr[i + 1][0]:
            i += 1
    return arr 

arr = [[1,3],[8,10],[15,18],[2,6],[2,5]]
print(combine_overlapping(arr=arr))

arr = [[1,3],[8,9],[9,11],[8,10],[15,18],[2,6],[2,5]]
print(combine_overlapping(arr=arr))


arr = [[1,2],[1,3],[1,6],[3,4]]
print(combine_overlapping(arr=arr))
