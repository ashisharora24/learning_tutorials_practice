def mergeSort(arr,start,end):
    if end>1:
        mid=end//2
        mergeSort(arr,start,mid)
        mergeSort(arr,start+mid,end-mid)
        #print("--------------------")
        k=start
        i=start
        j=start+mid
        len1=start+mid
        len2=start+end


        leftArray = arr[i:len1]
        rightArray = arr[j:len2]
        i=j=0

        while i<len(leftArray) and j<len(rightArray):
            if leftArray[i]<rightArray[j]:
                arr[k]=leftArray[i]
                i+=1
            else:
                arr[k]=rightArray[j]
                j+=1
            k+=1
        while i<len(leftArray):
            arr[k]=leftArray[i]
            i+=1
            k+=1
        while j<len(rightArray):
            arr[k]=rightArray[j]
            j+=1
            k+=1

n=8
arr = [2,6,8,5,4,3,1,7]
print(arr)
mergeSort(arr,0,n)
print(arr)
