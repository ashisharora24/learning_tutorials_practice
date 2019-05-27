def power(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return x*power(x,n-1)

x,n=[int(i) for i in input().split()]
print(power(x,n))
