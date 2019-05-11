# Sample Input 1:
# 7
# 3 4 5 9 10 31 15 2 0

def Selection_Sort_Explain(array):
    for i in range(len(array)-1):
        minIndex=i
        lower_value=array[i]
        for j in range(i+1,len(array)):
            #print(array[j],",",array[i])
            if array[j]<array[minIndex]:
                minIndex=j
        if minIndex!=i:
            array[i],array[minIndex]=array[minIndex],array[i]

array = [int (i) for i in input().split()]
Selection_Sort_Explain(array)
print(array)
