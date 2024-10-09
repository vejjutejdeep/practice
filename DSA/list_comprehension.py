import pandas as pd
even = [i for i in range(100) if i % 2 == 0]
odd = [i for i in range(100) if i %2 != 0]
arr = [1,3,5,7,9,2,1,5]
map = {}
# remove = [i for i in arr for j in range(0,i - 1) if i == j: pop(i)]
# df = pd.DataFrame(arr, columns=['data'])
# df = df.drop_duplicates()
# for i in range(len(arr)):
# i = 0
# while i < len(arr):
#     if arr[i] not in map:
#         map[arr[i]] = 1
#         i += 1
#     else:
#         arr.remove(arr[i])
#     print(map)
# print(arr)
b = []
[b.append(item) for item in arr if item not in b]
print(b)
# print(df) 
# print(even, odd)