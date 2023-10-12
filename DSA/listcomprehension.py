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