def flatten_list(arr):
    result = []
    for element in arr:
        if isinstance(element, list):
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result

print(flatten_list([[1,2,3], [4,4,6], [1,1,1]]))