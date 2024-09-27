compress = "a3b5c2a2d3d1b5"

temp = []

letter =[]

num = []

str = ""

for iter in range(0,len(compress), 2):

    letter.append(compress[iter])

    num.append(compress[iter+1])

print(letter)

iter2 = 0


while iter2 <= len(letter):

    if letter[iter2] not in temp: 

        temp.append(letter[iter2])
    
    else:

        letter.pop(iter2)

        num.pop(iter2)
    
    iter2 += 1

print(letter)
print(num)

for iter3 in range(0,len(letter)):

    str += letter[iter3] * int(num[iter3])

print(str)