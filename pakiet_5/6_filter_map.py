def filterList(lista):
    filtr = lambda string: string[0].lower() == "a"
    return [item for item in filter(filtr, lista)]

def listaKwadratow(lista):
    kwadratLiczby = lambda x : x*x
    return [item for item in map(kwadratLiczby, lista)]

print(filterList(["Kamil", "Ania", "Asia", "Basia", "Szymon"]))

print(listaKwadratow([1,2,3,4]))
