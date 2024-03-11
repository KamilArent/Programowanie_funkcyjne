from itertools import groupby

def grupowanie_liczb(lista):
    sorted_list = sorted(lista, key=lambda x: x %2)
    grouped_list = {key: list(group) for key, group in groupby(sorted_list, key=lambda x:x %2==0)}
    return  grouped_list

liczby = [1,2,3,4,5,6,7]

result =grupowanie_liczb(liczby)
print(result[True])
print(result[False])
