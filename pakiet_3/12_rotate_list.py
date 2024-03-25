def rotate_list(arr, kroki):
    kroki %= len(arr)
    return arr[-kroki:] + arr[:-kroki]

print(rotate_list([1,2,3,4], 2))
