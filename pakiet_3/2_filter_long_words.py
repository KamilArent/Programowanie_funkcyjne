def filter_long_words(arr):
    avg = sum(len(word) for word in arr)/len(arr)
    return [word for word in arr if len(word) > avg]

print(filter_long_words(["jeden", "dwa", "pięć", "osiem"]))