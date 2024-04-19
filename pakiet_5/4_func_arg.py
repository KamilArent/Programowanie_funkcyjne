def funcAsArg(func):
    test = [2,4,4,5]
    return [func(item) for item in test]

def exampleFunc(x):
    return x*x

print(funcAsArg(exampleFunc))