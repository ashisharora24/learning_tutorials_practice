def Binary_Search_Using_Recursion(list,start,end,var):
    if start>end:
        return -1
    middle=(start+end)//2
    if list[middle]==var:
        return middle
    elif list[middle]>var:
        end=middle-1
    else:
        start=middle+1
    return Binary_Search_Using_Recursion(list,start,end,var)

li=list(range(1,10000,4))
#print(len(li))
var=6002
start=0
end=len(li)

output=Binary_Search_Using_Recursion(li,start,end,var)
print("output : ", output)
if output!=-1:
    print(li[output])
