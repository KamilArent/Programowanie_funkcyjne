def infinte_fibonacci():
    fib = [1,1]
    fib_count = 0
    while(True):
        yield fib[fib_count]
        fib_count+=1
        next_fib = fib[fib_count] + fib[fib_count-1]
        fib.append(next_fib)

fib = infinte_fibonacci()

for i in range(10): #wypisanie 10 liczb fibonacciego
    print(next(fib))
print(next(fib)) #wypisanie kolejnej liczby fibonaciego

#czytanie pliku

plik = "przyklad.txt" #nazwa pliku w katalogu programowanie_funkcyjne
with open(plik) as infile:
    for line in infile:
        print(line)