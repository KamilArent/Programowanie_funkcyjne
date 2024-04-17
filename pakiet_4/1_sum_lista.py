def func(list):
    res = 0
    for item in list:
        if(item % 2 == 0):
            res += item * item

    return res

print(func([1,2,3,4]))