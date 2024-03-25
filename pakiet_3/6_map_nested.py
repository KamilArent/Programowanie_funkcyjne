
def map_nested(arr):
    def funkcja(a):
        return a*2

    return [list(map(funkcja, sublist)) for sublist in arr]

print(map_nested([[2,3,5],[1,2,3]]))