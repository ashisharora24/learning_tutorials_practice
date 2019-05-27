def sum(n):
    if n==0:
        return 0
    else:
        output=n+sum(n-1)
    return output

print(sum(int(input("Enter the number"))))
