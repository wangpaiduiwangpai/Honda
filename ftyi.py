import math

def double(x):
    return x * 2

def triple(x):
    return x * 3

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def square_root(x):
    return math.sqrt(x) 

def cube_root(x):
    return x ** (1/3)

def fourth_power(x):
    return x ** 4


if __name__ == '__main__':
    print(double(5))
    print(triple(5))
    print(square(5))
    print(cube(5))
    print(square_root(25))
    print(cube_root(27))
    print(fourth_power(5))
    
    
    
