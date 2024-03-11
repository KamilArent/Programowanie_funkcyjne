from functools import partial

def add_5(a, b):
    return a + b

add_5_partial = partial(add_5, b=5)
print(add_5_partial(2))