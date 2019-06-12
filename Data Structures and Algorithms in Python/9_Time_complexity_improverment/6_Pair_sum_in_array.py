# Pair sum in array
# Send Feedback
# Given a random integer array A and a number x.
# Find and print the pair of elements in the array which sum to x.
# Array A can contain duplicate elements.
# While printing a pair, print the smaller element first.
# That is, if a valid pair is (6, 5) print "5 6".
# There is no constraint that out of 5 pairs which have to be printed in 1st
# line.
# You can print pairs in any order, just be careful about the order of elements
# in a pair.
# Input format :
# Line 1 : Integer N (Array size)
# Line 2 : Array elements (separated by space)
# Line 3 : Integer x
# Output format :
# Line 1 : Pair 1 elements (separated by space)
# Line 2 : Pair 2 elements (separated by space)
# Line 3 : and so on
# Constraints :
# 1 <= N <= 1000
# 1 <= x <= 100
# Sample Input:
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# Sample Output :
# 1 6
# 3 4
# 3 4
# 2 5
# 2 5
# 3 4
# 3 4
# [1, 3, 6, 2, 5, 4, 3, 2, 4]
# [1, 2, 2, 3, 3, 4, 4, 5, 6]
def pairSum(arr,x):
    # print("sum value : ", x)
    # print("arr : ", arr)
    # print("Sorting the arr")
    arr.sort()
    # print("New sorted arr : ", arr)
    start = 0
    end = len(arr) - 1
    # print("starting pointing :", start)
    # print("ending point : ", end)
    # print("--------starting the main loop------------")
    while start < end:
        #print("starting pointing :", start, ". Value ", arr[start])
        #print("ending point : ", end, ". Value : ", arr[start])
        if arr[start] + arr[end] < x:
            start += 1
            #print("main loop the value start is less than value of end. stop and move to next level")
        elif arr[start] + arr[end] > x:
            #print("main loop the value start is greater than than value of end. iterate on end")
            temp_end = end - 1
            while start<temp_end:
                if arr[start] + arr[temp_end] == x:
                    print(arr[start], arr[temp_end])
                    temp_end -= 1
                elif arr[start] + arr[temp_end] > x:
                    temp_end -= 1
                else:
                    break
            start += 1
        else:
            print(arr[start], arr[end   ])
            temp_end = end - 1
            while start<temp_end:
                if arr[start] + arr[temp_end] == x:
                    print(arr[start] , arr[temp_end])
                    temp_end -= 1
                elif arr[start] + arr[temp_end] > x:
                    temp_end -= 1
                else:
                    break
            start += 1


# Main
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
sum = int(input())
pairSum(arr, sum)
