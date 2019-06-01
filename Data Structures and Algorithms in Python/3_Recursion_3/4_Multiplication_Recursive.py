def Multiplication_Recursive(m,n):
    if n==0:
        return 0
    output = Multiplication_Recursive(m,n-1)
    return output+m

m=int(input())
n=int(input())
print(Multiplication_Recursive(m,n))
