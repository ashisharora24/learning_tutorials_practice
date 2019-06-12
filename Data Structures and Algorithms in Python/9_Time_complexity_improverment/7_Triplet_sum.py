# Triplet sum
# ----------------------------------------------------------------------------
# Send Feedback
# Given a random integer array and a number x. Find and print the triplets of
# elements in the array which sum to x.
# ----------------------------------------------------------------------------
# While printing a triplet, print the smallest element first.
# That is, if a valid triplet is (6, 5, 10) print "5 6 10". There is no
# constraint that out of 5 triplets which have to be printed on 1st line. You
# can print triplets in any order, just be careful about the order of elements
# in a triplet.
# Input format :
# Line 1 : Integer N (Array Size)
# Line 2 : Array elements (separated by space)
# Line 3 : Integer x
# Output format :
# Line 1 : Triplet 1 elements (separated by space)
# Line 2 : Triplet 3 elements (separated by space)
# Line 3 : and so on
# Constraints :
# 1 <= N <= 1000
# 1 <= x <= 100
# Sample Input:
# 7
# 1 2 3 4 5 6 7
# 12
# Sample Output ;
# 1 4 7
# 1 5 6
# 2 3 7
# 2 4 6
# 3 4 5
# ----------------------------------------------------------------------------


def pairSum(arr, x, start, first_value):
    # start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] < x:
            start += 1
        elif arr[start] + arr[end] > x:
            temp_end = end - 1
            while start < temp_end:
                if arr[start] + arr[temp_end] == x:
                    print(first_value, arr[start], arr[temp_end])
                    temp_end -= 1
                elif arr[start] + arr[temp_end] > x:
                    temp_end -= 1
                else:
                    break
            start += 1
        else:
            print(first_value, arr[start], arr[end])
            temp_end = end - 1
            while start < temp_end:
                if arr[start] + arr[temp_end] == x:
                    print(first_value, arr[start], arr[temp_end])
                    temp_end -= 1
                elif arr[start] + arr[temp_end] > x:
                    temp_end -= 1
                else:
                    break
            start += 1


def tripletSum(arr, sum):
    # print("arr : ", arr)
    arr.sort()
    # print("arr : ", arr)
    for i in range(len(arr)-3):
        # print("base number : ", i)
        # print("base Value : ", arr[i])
        if sum >= arr[i]:
            x = sum - arr[i]
            pairSum(arr, x, i, arr[i])


n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
sum = int(input())
tripletSum(arr, sum)
