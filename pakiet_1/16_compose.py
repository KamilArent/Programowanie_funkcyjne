def squared(x):
    return x*x

def add(a,b):
    return a+b

def composite_function(f,g):
    return lambda x : g(f(x), f(x))

add_squared_numbers = composite_function(squared, add)
print(add_squared_numbers(4))
