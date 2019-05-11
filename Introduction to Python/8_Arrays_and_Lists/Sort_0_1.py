# Sort 0 1

# You are given an integer array A that contains only integers 0 and 1.
# Write a function to sort this array.
# Find a solution which scans the array only once.
# Don't use extra array.
# You need to change in the given array itself. So no need to return or print anything.
# Input format :
# Line 1 : Integer N (Array Size)
# Line 2 : Array elements (separated by space)
# Output format :
# Sorted array elements
# Constraints :
# 1 <= N <= 10^6
# Sample Input :
# 7
# 0 1 1 0 1 0 1
# Sample Output :
# 0 0 0 1 1 1 1

# def sort(array):
#     print("array : ", array)
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i]>array[j]:
#                 array[i],array[j]=array[j],array[i]
#
# n = int(input())
# array = [int(i) for i in input().split()]
# sort(array)
# print(array)

def sort(a, n):
    j = -1
    for i in range(n):
        if a[i] < 1:
            j = j + 1
            a[i], a[j] = a[j], a[i]


n = int(input())
array = [int(i) for i in input().split()]
sort(array)
for i in array(n):
        print(array[i], end = " ")
