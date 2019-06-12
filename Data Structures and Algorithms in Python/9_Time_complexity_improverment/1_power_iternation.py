def power(x, n):
    if n == 1:
        return x
    elif n == 0:
        return 1
    ans = sq = x * x
    i = 4
    while i <= n:
        ans *= sq
        i += 2
    i -= 2
    if i < n:
        ans *= x
    return ans


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x,n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
