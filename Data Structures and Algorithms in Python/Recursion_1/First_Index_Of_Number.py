def First_Index_Of_Number(arr,x,n=0):
    if len(arr[n:])==0:
        return False
    else:
        if arr[n]==x:
            return n
        else:
            return First_Index_Of_Number(arr,x,n+1)

from sys import setrecursionlimit
setrecursionlimit(11000)
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(First_Index_Of_Number(arr,x))
print(First_Index_Of_Number([],3))
