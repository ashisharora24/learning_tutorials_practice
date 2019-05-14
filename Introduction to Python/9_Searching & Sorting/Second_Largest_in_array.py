# Second Largest in array
# Given a random integer array of size n, find and return the second largest element present in the array.
# If n <= 1 or all elements are same in the array, return -2147483648 i.e. -2^31.
# Input format :
# Line 1 : Integer n (Array Size)
# Line 2 : Array elements (separated by space)
# Output Format :
# Second largest element
# Constraints :
# 1 <= N <= 10^6
# Sample Input 1:
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 13
# Sample Input 2:
# 5
# 9 3 6 2 9
# Sample Output 2:
# 6
# Sample Input 3:
# 2
# 6 6
# Sample Output 3:
# -2147483648

def Second_Largest_in_arrary(arr,n):
    largest=0
    sec_largest=0
    if arr[0]>arr[1]:
        largest=arr[0]
    else:
        sec_largest=arr[1]
    for i in range(2,n):
        if arr[i]>largest:
            largest=arr[i]
        elif arr[i]>sec_largest:
            sec_largest=arr[i]
        else:
            pass
    return sec_largest

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(Second_Largest_in_arrary(arr,n))
