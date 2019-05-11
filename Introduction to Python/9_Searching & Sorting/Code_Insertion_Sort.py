# Code Insertion Sort
# Given a random integer array. Sort this array using insertion sort.
# Change in the input array itself. You don't need to return or print elements.
# Input format :
# Line 1 : Integer N, Array Size
# Line 2 : Array elements (separated by space)
# Constraints :
# 1 <= N <= 10^3
# Sample Input 1:
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 1 2 3 4 6 13 28
# Sample Input 2:
# 5
# 9 3 6 2 0
# Sample Output 2:
# 0 2 3 6 9

def insertionSort(array,n):
    for i in range(1,n):
        j=i-1
        temp = array[i]
        while (j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

n=int(input())
arr=[int(i) for i in input().split()]
insertionSort(arr,n)
[print(i,end=" ") for i in arr]
