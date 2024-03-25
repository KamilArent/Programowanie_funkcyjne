def remove_duplicates(arr):
    duplicate = []
    result = []
    for element in arr:
        if element in result:
            duplicate.append(element)
        else:
            result.append(element)
    return result

print(remove_duplicates([1,2,2,3,4,1,5,2]))