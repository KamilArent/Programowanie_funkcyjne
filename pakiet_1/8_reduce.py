from functools import reduce

suma_liczb = reduce(lambda x, y: x+y, [1,2,3,4])

print(suma_liczb)