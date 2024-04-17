def odwracator(string):
    res = ""
    for item in string:
        res += item.upper() if item.islower() else item.lower()
        
    return res
print(odwracator("Tak sobie"))