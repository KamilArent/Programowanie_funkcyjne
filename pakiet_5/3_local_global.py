def printLocGlob():
    global x #wzięcie zmiennej globalnej
    y = 15 #utwaorzneie zmiennej lokalnej
    print(x + y) #wypisanie sumy tych zmiennych

x = 19
printLocGlob()

