
def First_Index_Of_Number(arr,x):
    if len(arr)==0:
        return -1
    else:
        if arr[0]==x:
            return 0
        else:
            output = First_Index_Of_Number(arr[1:],x)
            if output==-1:
                return -1
            else:
                output+=1
            return output

from sys import setrecursionlimit
setrecursionlimit(11000)
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(First_Index_Of_Number(arr,x))
print(First_Index_Of_Number([1,2,3,4,4,6],6))
