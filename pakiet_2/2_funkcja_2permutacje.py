from itertools import combinations

def kombinacje_2(tablica):
    return (list(combinations(tablica,2)))


print(kombinacje_2([3,5,6,7]))