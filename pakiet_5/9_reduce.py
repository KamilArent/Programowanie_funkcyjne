import functools

lista = [1,6,2,3,4,5]
#max - 6
#avg - 3.5
max_list = lambda a,b: a if a>b else b

print(functools.reduce(max_list, lista))

sum_list = lambda a,b: a+b
print(functools.reduce(sum_list,lista)/len(lista))