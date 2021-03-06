# Rotate array
# Given a random integer array of size n, write a function that rotates the given array by d elements (towards left)
# Change in the input array itself. You don't need to return or print elements.
# Input format :
# Line 1 : Integer n (Array Size)
# Line 2 : Array elements (separated by space)
# Line 3 : Integer d
# Output Format :
# Updated array elements (separated by space)
# Constraints :
# 1 <= N <= 1000
# 1 <= d <= N
# Sample Input :
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output :
# 3 4 5 6 7 1 2

def Rotate(arr, d):
    for i in range(d):
        element=arr.pop(0)
        arr.append(element)

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)
print(*arr)
