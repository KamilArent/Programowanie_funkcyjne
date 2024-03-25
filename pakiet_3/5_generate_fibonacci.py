def infinte_fibonacci():
    fib = [1,1]
    fib_count = 0
    while(True):
        yield fib[fib_count]
        fib_count+=1
        next_fib = fib[fib_count] + fib[fib_count-1]
        fib.append(next_fib)

fib = infinte_fibonacci()

for i in range(10):
    print(next(fib))
