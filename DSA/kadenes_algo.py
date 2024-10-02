import sys

def find_sum_arr(arr):
    max = -sys.maxsize - 1
    sum = 0
    for i in arr:
        sum += i
        
        if max < sum: 
            max = sum
        if sum < 0:
            sum = 0
        # print("sum",sum,"max", max,"ele", i)   
    return max
arr = [-2,-3,4,-1,-2,1,5,-3] 
n = len(arr)
print(find_sum_arr(arr))
arr = [-2,-1] 
n = len(arr)
print(find_sum_arr(arr))
arr = [-2,1,-3,4,-1,2,1,-5,4] 
print(find_sum_arr(arr))