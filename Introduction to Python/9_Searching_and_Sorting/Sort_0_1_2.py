# Sort 0 1 2
# You are given an integer array containing only 0s, 1s and 2s.
# Write a solution to sort this array using one scan only.
# You need to change in the given array itself. So no need to return or print anything.
# Input format :
# Line 1 : Integer n (Array Size)
# Line 2 : Array elements (separated by space)
# Output Format :
# Updated array elements (separated by space)
# Constraints :
# 1 <= n <= 10^6
# Sample Input:
# 7
# 0 1 2 0 2 0 1
# Sample Output:
# 0 0 0 1 1 2 2
import time
start_time = time.time()



def sorting_0_1_2(arr,n):
    j=0
    k=n-1
    i=0
    while i<=k:
        if arr[i]==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        elif arr[i]==1:
            i+=1
        else:
            arr[i],arr[k]=arr[k],arr[i]
            k-=1

n=int(input())
arr=[int(i) for i in input().split()]
sorting_0_1_2(arr,n)
[print(i,end=" ") for i in arr]
