def check_consequtive(arr):

    count_dic = {}

    for element in arr:

        if element - 1 not in arr:

            count_dic[element] = 1
        
    # print(count_dic)
    count = []
    for i in count_dic:

        num_co = 1

        while(True):
        
            if (i + 1) in arr:

                num_co += 1
            
            else:

                count.append(num_co)

                break
            
            i += 1
    
    print(count)

    maxcount = sorted(count)[-1]

    return maxcount

def check_consequtive(arr):

    arr = set(arr)

    if len(arr) == 0:

        return 0

    count_dic = {}


    for element in arr:

        if element - 1 not in arr:

            count_dic[element] = 1

    count = []
    for i in count_dic:

        num_co = 1

        while(True):
        
            if (i + 1) in arr:

                num_co += 1
            
            else:

                count.append(num_co)

                break
            
            i += 1
    
    # print(count)

    maxcount = sorted(count)[-1]

    return maxcount

def count_return(arr):

    count  = 0

    arr = set(arr)

    for i in arr:

        if (i-1) not in arr:

            temp_count = 1
        
            while(True):

                if i + 1 in arr:

                    temp_count +=1
                else:

                    count = max(count,temp_count)

                    break

                i += 1
    
    return count

nums = [100,4,200,1,3,2]
print(check_consequtive(nums))
print(count_return(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(check_consequtive(nums))
print(count_return(nums))