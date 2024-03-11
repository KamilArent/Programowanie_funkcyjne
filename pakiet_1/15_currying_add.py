def curried_add(a):
    def final(b):
        return a + b
    return final 

print(curried_add(5)(3))