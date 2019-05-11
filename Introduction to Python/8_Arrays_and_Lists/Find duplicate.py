# Find Unique

# Given an integer array of size 2N + 1. In this given array, N numbers are present twice and one number is present only once in the array.
# You need to find and return that number which is unique in the array.
# Note : Given array will always contain odd number of elements.
# Input format :
# Line 1 : Array size i.e. 2N+1
# Line 2 : Array elements (separated by space)
# Output Format :
# Unique element present in the array
# Constraints :
# 1 <= N <= 10^3
# Sample Input :
# 7
# 2 3 1 6 3 6 2
# Sample Output :
# 1
def find_unique(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if i!=j:
                if li[i]==li[j]:
                    break
        else:
            return li[i]

n = int(input())
li = [int(i) for i in input().split()]
print(find_unique(li))
