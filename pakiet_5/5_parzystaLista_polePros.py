def parzystaLista(lista):
    return [item for item in lista if(item% 2== 0)]

poleProstokata = lambda a,b : a*b

print(parzystaLista([1,2,3,4,5,6]))
print(poleProstokata(2,4))