def concat_dict(*dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) +value
    return result

print(concat_dict({"jeden": 1, "dwa": 2}, {"jeden": 1, "dwa": 2}))
print(concat_dict({"jeden": 1, "dwa": 2},{"jeden": 1, "dwa": 2},{"jeden": 1, "dwa": 2}))