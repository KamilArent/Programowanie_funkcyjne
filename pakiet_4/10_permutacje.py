import itertools

def wszystkie_permutacje(lista):
    return list(itertools.permutations(lista))

print(wszystkie_permutacje([1,2,3]))