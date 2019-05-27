def fab(n):
    if n==1 or n==2:
        return 1
    else:
        out=fab(n-1)+fab(n-2)
    return out

for i in range(1,20):
    print(i,"\t",fab(i))
