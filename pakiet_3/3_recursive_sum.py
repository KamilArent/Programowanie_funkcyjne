def recursive_sum(arr):
    suma = 0
    for element in arr:
        if(isinstance(element,list)):
            suma += recursive_sum(element)
        else:
            suma += element
    return suma

print(recursive_sum([[1,2,3,],[2,3]]))