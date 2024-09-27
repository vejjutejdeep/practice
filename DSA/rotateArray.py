def rotateArray(arr,val):

    print(arr[-1])

    while val >= 1:

        num = arr.pop(0)

        arr.append(num)
        
        # print(arr)

        val -= 1

    return arr

print(rotateArray([7,5,2, 11, 2, 43, 1, 1], 2))
print(rotateArray([5, 6, 7, 8],2))
