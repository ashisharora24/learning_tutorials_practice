import sys
sys.setrecursionlimit(2000)

def fact(n):
    if n==0:
        return 1
    else:
        output=n*fact(n-1)
    return output

print(fact(int(input("Enter the number who's factorial you want to get : "))))
