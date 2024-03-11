import time
def timeit():
    start = time.time()
    ###
    #tutaj wstawić funkcje do mierzenia

    i = 0
    while(i < 50000000):
        i +=1

    ###
    end = time.time()
    return (end-start)

#print(timeit(func))
print(timeit())