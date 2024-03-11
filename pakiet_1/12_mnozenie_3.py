from functools import partial

def multiply(liczba, mnoznik):
    return liczba * mnoznik

partial_muliply = partial(multiply, mnoznik=3)

print(partial_muliply(10))