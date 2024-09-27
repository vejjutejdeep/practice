# yeild
def prin_prime(n):
    prime = []
    for i in range(2,n):
        pri = True
        for j in range(2,i):
            # print(i%j)
            if i % j == 0:
                  pri = False
        if pri == True:
            prime.append(i)
    return prime
			
print(yeild(prin_prime(12)))