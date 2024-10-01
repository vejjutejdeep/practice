import math
def square(func):
    
    def inner(a):
        return func(a * a)
    
    return inner

def double(func):

    def inner(a):
        return func(2 *a)

    return inner

@square
@double
def number(a):
    a = round(math.sqrt(a))
    return a

# n = square(number)

# b = double(n)

print(number(19))