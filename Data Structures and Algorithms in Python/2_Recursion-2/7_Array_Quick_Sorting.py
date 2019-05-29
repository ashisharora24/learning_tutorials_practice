def quick_sorting(arr,start,len):
    end=start+len-1
    if start>=end:
        # print("existing now. base case meet")
        return
    i=start
    j=i+1
    # print("-----while loop starts-------")
    while j<=end:
        # print ("if arr[i]>arr[j]")
        # print ("arr[i] : ",arr[i] )
        # print ("arr[J] : ",arr[j] )

        if arr[i]>arr[j]:
            #print ("---True----")
            temp_val=arr[j]
            t=j
            while t>i:
                arr[t]=arr[t-1]
                t-=1
            arr[i]=temp_val
            i+=1
            #print(arr)
        j+=1
    # len=(((i-1)-start)+1)
    quick_sorting(arr,start,(((i-1)-start)+1))
    #start=i+1
    #len=((end-(i+1))+1)
    quick_sorting(arr,i+1,((end-(i+1))+1))

arr=[3,5,1,2,15,2,8,7]
print(arr)
quick_sorting(arr,0,len(arr))
print(arr)
