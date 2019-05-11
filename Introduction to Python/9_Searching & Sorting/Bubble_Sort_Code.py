# Code Bubble Sort

# Given a random integer array. Sort this array using bubble sort.
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

def bubble_method(array,n):
    end=n-1
    while 0<end:
        for i in range(end):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
        end=end-1
n=int(input())
array = [int(i) for i in input().split()]
bubble_method(array,n)
print(array)
