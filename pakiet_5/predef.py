import itertools

def poleKwadratu(bok):
    return bok*bok

def parzysteLiczbyListy(lista):
    return [item for item in lista if(item%2 == 0)]

def divide_list(list, max_len):
    return [list[i:i+max_len] for i in range(0, len(list), max_len)]

def wszystkie_permutacje(lista):
    return list(itertools.permutations(lista))

def buildSentence(*args):
    return " ".join(item for item in args)
