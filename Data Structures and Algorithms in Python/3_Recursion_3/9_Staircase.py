import sys

def staircase(n):
    output=0
    if n<=0:
        return 1
    if n-1>=0:
        output = output + staircase(n-1)
    if n-2>=0:
        output = output + staircase(n-2)
    if n-3>=0:
        output = output + staircase(n-3)
    return output

n=int(input())
sys.setrecursionlimit(11000)
print(staircase(n))
