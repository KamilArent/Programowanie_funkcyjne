def most_item(list):
    return max(set(list), key=list.count)

print(most_item([1,2,3,2]))
print(most_item(["pies", "kot", "kot"]))