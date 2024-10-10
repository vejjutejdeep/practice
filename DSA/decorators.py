import math
def square(func):
    
    def inner(a):
        return func(a * a)
    
    return inner

def double(func):

    def inner(a):
        return func(2 *a)

    return inner

def cube(func):

    def inner(a):
        return func(a * a * a)
    return inner

@square
@double
@cube
def number(a):
    # float a = 0
    a = round(math.sqrt(a))
    return a

# n = square(number)

# b = double(n)

print(number(19))