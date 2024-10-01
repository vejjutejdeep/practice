import sys
def maxSubarraySum(arr, n):
    sum = -sys.maxsize - 1
    max_arr = []
    for i in range(len(arr)):
        temp_sum = 0
        for j in range(i, len(arr)):
            temp_sum += arr[j] 
            if  temp_sum > sum:
                sum = temp_sum
                max_arr = arr[i:j + 1]
    return sum,max_arr
arr = [-2,1,-3,4,-1,2,1,-5,4] 
n = len(arr)
print(maxSubarraySum(arr,n))
arr = [-2,-1] 
n = len(arr)
print(maxSubarraySum(arr,n))