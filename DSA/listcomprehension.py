def newstring(st, pos):

    # for i in range(pos,len(st) - 1):

    #     st[i] = st[i+1]

    temp = list(st)
    # temp.pop(pos)
    # temp.remove(temp[pos])
    st1 = ""
    new  = st[:pos] + st[pos+1:]
    # fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'yak']
    # newlist = [i for i in fruits if 'y' in i]
    # newlis = [st1 += i for i in temp]
    # print(newlis)
    newlis = [i for i in temp if i !=temp[pos]]
    # print(newlis)
    for i in newlis:
        st1 += i
    print(st1)
    return new

st ="hello world"
pos = 6
newstring(st,pos)

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

dic = {}

for iter1 in range(len(list2)):
    
    dic [list1[iter1]] = list2[iter1]

sorted_lis = sorted(dic.items(), key = lambda x:x[1])


newlist = []
for i in sorted_lis:
    
    newlist.append(i[0])

print(newlist)