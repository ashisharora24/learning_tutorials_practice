def Geometric_Sum(n):
    if n<0:
        return
    if n==0:
        return 1
    output = Geometric_Sum(n-1)
    return output + 1/(2**n)

n=int(input())
print("%.5f" %Geometric_Sum(n))
