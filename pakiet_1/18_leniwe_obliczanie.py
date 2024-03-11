def lazy_fibonacci(count):
    fib = [1,1]
    fib_count = 0
    while(len(fib) <=count):
        yield fib[fib_count]
        fib_count+=1
        next_fib = fib[fib_count] + fib[fib_count-1]
        fib.append(next_fib)

lazy_fib = lazy_fibonacci(10)

print(next(lazy_fib))
print(next(lazy_fib))
print(next(lazy_fib))
print(next(lazy_fib))
print(next(lazy_fib))
print(next(lazy_fib))