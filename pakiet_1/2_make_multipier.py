def make_multipier(x):

    def multiplier(n):
        return x*n
    return multiplier

result = make_multipier(2)
print(result(5))