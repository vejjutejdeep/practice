# def prime(num):

#     for i in range(2,num):

#         if num % i == 0:

#             return "not a prime"
        
#     return "prime"

# def finacchi_series(num):

#     st_lis = [1,1]
        
#     for i in range(2,num):

#         st_lis.append(st_lis[i - 1] + st_lis[i - 2])

#     return st_lis
def change_string(sentence):

    lis = sentence.split()

    words = len(lis) - 1 

    str = ""

    while(words > -1):
        # print(words)
        if "." in lis[words]:
            # print(lis[words][:-1])
            lis[words] = lis[words][:-1]
        str += lis[words].swapcase() + " "

        words -= 1
    # print(str)
    str = str[:-1]
    str += "."

    return str

a = lambda b,a: a+ b

print(a(2,3))

print(change_string("I am vejju Tejdeep."))