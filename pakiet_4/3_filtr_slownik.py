def filtr_slownik(dict):
    return {key: value  for key, value in dict.items() if(value % 2 == 0)}

print(filtr_slownik({"jeden": 2, "dwa": 1}))