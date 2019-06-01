def Count_Zeros(n):
    if n<=0:
        return 0
    q=n//10
    r=n%10
    val=0
    if r==0:
        val=1
    output = Count_Zeros(q)
    return output+val

n=int(input())
print(Count_Zeros(n))
