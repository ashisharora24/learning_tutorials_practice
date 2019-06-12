# Find the Unique Element
# Send Feedback
# Given an integer array of size 2N + 1. In this given array, N numbers are
# present twice and one number is present only once in the array.
# You need to find and return that number which is unique in the array.
# Note : Given array will always contain odd number of elements.
# Input format :
# Line 1 : Array size i.e. 2N+1
# Line 2 : Array elements (separated by space)
# Output Format :
# Unique element present in the array
# Constraints :
# 1 <= N <= 10^6
# Sample Input :
# 7
# 2 3 1 6 3 6 2
# Sample Output :
# 1


def FindUnique(arr):
    arr.sort()
    str1 = ""
    i = 0
    condition = "not_match"
    while i < len(arr)-1:
        if arr[i] != arr[i+1]:
            if condition == "not_match":
                str1 = str1 + " " + str(arr[i])
            if condition == "matched":
                condition = "not_match"
            if i == len(arr)-2:
                str1 = str1 + " " + str(arr[i+1])
        else:
            condition = "matched"
        i += 1
    return str1[1:]


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
unique = FindUnique(arr)
print(unique)
