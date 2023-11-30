def compute_GCD(ope1, ope2):

    smaller = min(ope1,ope2)

    res = 1

    for i in range(2,smaller+1):

        if ope1 % i == 0 and ope2 % i == 0:

            res = i
    

    return res

def computeGCD2(ope1, ope2):

    ope1, ope2 = min(ope1, ope2), max(ope1,ope2)

    while(ope2):

        ope1, ope2 = ope2, ope2 % ope1
    
    return ope1



    return ope2


print(compute_GCD(12,14))
print(computeGCD2(12,14))
print(compute_GCD(300,400))
print(computeGCD2(300,400))
print(compute_GCD(54,24))
print(computeGCD2(54,24))