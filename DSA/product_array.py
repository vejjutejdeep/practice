def product_array(arr):

    lef_arr=[1]

    for lef_pointer in range(len(arr) - 1):

        lef_arr.append(arr[lef_pointer] * lef_arr[lef_pointer])
    
    right_pointer = len(arr) - 1

    right_arr = [1]

    while(right_pointer >=1):

        product = arr[right_pointer] * right_arr[0]

        right_arr.insert(0, product)

        right_pointer -= 1
    
    # print(lef_arr)
    # print(right_arr)

    product_arr = []
    
    for i in range(len(lef_arr)):

        product_arr.append(lef_arr[i] * right_arr[i])

    return product_arr
    
arr=[1,2,3,4]
print(product_array(arr))

arr=[-1,1,0,-3,3]
print(product_array(arr))

arr=[1,3,4,12,6]
print(product_array(arr))