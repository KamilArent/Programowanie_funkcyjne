def divide_list(list, max_len):
    return [list[i:i+max_len] for i in range(0, len(list), max_len)]


print(divide_list([1,2,3,4], 3))