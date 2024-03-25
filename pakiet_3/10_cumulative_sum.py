def cumulative_sum(arr):
    result = []
    sum = 0
    for liczba in arr:
        sum += liczba
        result.append(sum)
    return result

print(cumulative_sum([1,2,3,4]))