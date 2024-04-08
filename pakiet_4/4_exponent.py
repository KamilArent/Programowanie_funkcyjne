def exponent_pow(exp):
    return lambda x: x**exp

f_do_3 = exponent_pow(3)
print(f_do_3(2))