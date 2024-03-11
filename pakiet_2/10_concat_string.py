def concat_string(*args):
    result = ""
    for string in args:
        result += string + " "

    return result

print(concat_string("Hej", "Dwa", "world"))
print(concat_string("Hello", "World", "!"))