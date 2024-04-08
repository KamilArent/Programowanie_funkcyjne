def tuplet_list_func(tuplets, func):
    result =[]
    for tuplet in tuplets:
        for item in tuplet:
            result.append(func(item))

    return result

print(tuplet_list_func([(1,2,3), (2,3,1)], lambda x: x+1))

