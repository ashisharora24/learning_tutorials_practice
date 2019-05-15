# Code Binary Search

# Given a sorted integer array (in ascending order) and an element x.
# You need to search this element x in the given input array using binary search.
# Return the index of element in the input.
# Indexing starts from 0.
# Return -1 if x is not present in the input array.
# Input format :
# Line 1 : Integer N, Array Size
# Line 2 : Array elements (separated by space)
# Line 3 : Element to be searched (i.e. x)
# Output Format :
# Index
# Constraints :
# 1 <= N <= 10^6
# Sample Input 1:
# 7
# 1 3 7 9 11 12 45
# 3
# Sample Output 1:
# 1
# Sample Input 2:
# 7
# 1 2 3 4 5 6 7
# 9
# Sample Output 2:
# -1
def code_binary_search(array,n,x):
    start=0
    end=n-1
    while start<end:
        middle=(start+end)//2
        if array[middle]==x:
            return middle
        elif array[middle]<x:
            start=middle+1
        else:
            end=middle-1
    return -1

n=int(input())
array=[int(i) for i in input().split()]
x=int(input())
print(code_binary_search(array,n,x))
