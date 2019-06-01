def partation(arr,start,end):
    if start>=end:
        return
    pivot=arr[start]
    count=0
    for i in range(start,end+1):
        if arr[i]<pivot:
            count+=1
    arr[start],arr[start+count]=arr[start+count],arr[start]
    pivot_index=start+count
    i=start
    j=end
    while i<j:
        if arr[i]<pivot:
            i=i+1
        elif arr[j]>=pivot:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
    return pivot_index



def quick_sorting(arr,start,end):
    if start>=end:
        return
    pivot = partation(arr,start,end)
    quick_sorting(arr,start,pivot-1)
    quick_sorting(arr,pivot+1,end)


arr=[3,5,1,2,15,2,8,7]
print(arr)
quick_sorting(arr,0,len(arr)-1)
print(arr)
