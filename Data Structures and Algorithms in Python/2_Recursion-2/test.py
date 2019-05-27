def push(arr):
    li=len(arr)
    i=0
    l=0
    while i<li:
        if arr[i]==0:
            j=i
            while j<li:
                arr[j]=arr[j+1]
                j+=1
            arr.append(l)
        i+=1
    return arr

n=int(input())
arr=list(int(x) for x in input().strip().split())
arr2=push(arr)
print(arr2)
