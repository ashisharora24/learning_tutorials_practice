def power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        temp = power(x, n/2)
        return temp*temp
    else:
        n = n-1
        temp = power(x, n/2)
        return temp*temp*x

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x,n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
