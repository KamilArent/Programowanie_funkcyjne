squared = lambda x : x*x

def squared_list(numbers):
    i = 0
    for value in numbers:
        squared_value = value* value
        numbers[i] = squared_value;
        i +=1
    return numbers

print(squared_list([1,2,3,4]))