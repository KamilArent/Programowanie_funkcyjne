def partition_list(lst):
    def condition(x):
        return x > 2
    return [item for item in lst if condition(item)], [item for item in lst if not condition(item)]

print(partition_list([1,2,3,4,5]))
