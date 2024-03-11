from itertools import permutations

literki = ['A', 'B']
literki2 = [ 'C', 'D']

wszystkie_kombinacje = []

permutacje_literki = permutations(literki,len(literki))

for kombinacja in permutacje_literki:
    zipped = zip(kombinacja, literki2)
    wszystkie_kombinacje.append(list(zipped))

print(wszystkie_kombinacje)