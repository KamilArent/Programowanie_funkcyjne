dodaj5 = lambda x: 5+x
kwadrat = lambda x: x*x

def obieFuncLista(lista):
    listaPlus5 = map(dodaj5, lista)
    return [item for item in map(kwadrat, listaPlus5)]

print(obieFuncLista([1,2,3]))