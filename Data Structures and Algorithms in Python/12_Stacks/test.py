def MissingNumber(li):
    n=len(li)
    for i in range(n-1):
        for j in range(i,n):
            if li[i] == li[j] and i!=j:
              return li[i]
    return 0
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)
