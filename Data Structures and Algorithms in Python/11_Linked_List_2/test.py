from time import *

t2 = perf_counter()
t1 = perf_counter()

counter = 0
for i in range(10000):
    counter += 1

    print(i, end=" ")
    # r =  req...

    if counter == 61:
        t2 = perf_counter()
        print("\n sleeping \n",10 - t2 + t1)
        sleep(10 - t2 + t1)
        counter = 1
        t1 = perf_counter()
