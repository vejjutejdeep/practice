def sum_array(arr):
    sum1 = 0
    sum2 = 0
    for i in arr:
        sq = i * i
        sum1 += i
        sum2 +=  sq
    return sum1,sum2

def num_sum(n):
    return n * (n + 1) // 2,n * (n + 1) * (2 * n + 1) // 6

def repeating(arr):
    n = len(arr)
    s,s2 = sum_array(arr)
    sn, s2n = num_sum(n)
    val1 = s - sn
    val2 = s2 - s2n
    val2 = val2 // val1
    repeating = (val1 + val2) // 2
    missing = (repeating - val1)
    return repeating,missing


array = [3,1,2,5,3]
print(repeating(array))
array = [3,1,2,5,4,6,7,5]
print(repeating(array))
