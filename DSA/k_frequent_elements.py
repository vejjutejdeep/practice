def frequent_element(nums,k):
    
    lis = []

    dic = {}

    for i in nums:

        if i in dic:

            dic[i] += 1
        
        else:

            dic[i] = 1
    
    sort_item = sorted(dic.items(), key= lambda x:x[1], reverse=True)

    # print("sorted dictionary")
    # print(sort_item)
    
    for i in range(k):

        # print(sort_item[i][0])

        lis.append(sort_item[i][0])

    return lis

nums = [1,2,1,2,3,1,2]
k = 2
print(frequent_element(nums,k))

nums = [5,5,1,2,3,1,2,3]
k = 4
print(frequent_element(nums,k))

nums = [1]
k = 1
print(frequent_element(nums,k))
# print(frequent_element(nums,k))