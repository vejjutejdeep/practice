def majourity_ele(arr):
    freq = {}
    n = len(arr) // 2
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    # print(freq)
    ans = [j for j  in freq if freq[j] > n]
    return ans

arr = [2, 2, 1, 1, 1, 2, 2]
print(majourity_ele(arr))
arr = [4,4,2,4,3,4,4,3,2,4]
print(majourity_ele(arr))