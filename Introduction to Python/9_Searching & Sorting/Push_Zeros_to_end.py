# Push Zeros to end

# Given a random integer array, push all the zeros that are present to end of the array.
# The respective order of other elements should remain same.
# Change in the input array itself. You don't need to return or print elements.
# Don't use extra array.
# Note : You need to do this in one scan of array only.
# Input format :
# Line 1 : Integer N, Array Size
# Line 2 : Array elements (separated by space)
# Output Format :
# Array elements (separated by space)
# Constraints :
# 1 <= N <= 10^6
# Sample Input 1:
# 7
# 2 0 4 1 3 0 28
# Sample Output 1:
# 2 4 1 3 28 0 0
# Sample Input 2:
# 5
# 0 3 0 2 0
# Sample Output 2:
# 3 2 0 0 0


def Push_Zeros_to_end(arr):
    zero_pointer=-1
    for i in range(len(arr)):
        #print("--------------------")
        #print("start zero_pointer : ",zero_pointer)
        if arr[i]>0:
            if zero_pointer!=-1:
                arr[zero_pointer],arr[i]=arr[i],arr[zero_pointer]
                zero_pointer=zero_pointer+1
        else:
            if zero_pointer==-1:
                zero_pointer=i
        #print("end zero_pointer : ",zero_pointer)
        #print(arr)


n= int(input())
arr=[int(i) for i in input().split()]
Push_Zeros_to_end(arr)
[print(i,end=" ") for i in arr]
