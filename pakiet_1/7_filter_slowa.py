def filtr_slow(slowo):
    if len(slowo) > 5:
        return True
    else:
        return False

print(list(filter(filtr_slow, ["jeden", "osiem", "dwadziescia"])))