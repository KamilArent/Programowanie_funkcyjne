def function_to_list(list, func):
    return [func(item) for item in list]

def swap_case(string):
    return string.swapcase()

print(function_to_list(["jeden", "DWA", "tRZY"], swap_case))