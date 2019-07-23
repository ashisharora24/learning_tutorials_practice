# Longest subset zero sum
# Send Feedback
# Given an array consisting of positive and negative integers, find the length
# of the longest continuous subset whose sum is zero.
# NOTE: You have to return the length of longest subset .
# Input Format :
# Line 1 : Contains an integer N i.e. size of array
#
# Line 2 : Contains N elements of the array, separated by spaces
# Output Format
#  Line 1 : Length of longest continuous subset
# Sample Input :
# 10
#  95 -97 -387 -435 -5 -70 897 127 23 284
# Sample Output :
# 5

def subsetSum(l):
    max_counter = 0
    dict = {}
    counter = 0
    sum = 0
    for i in l:
        sum += i
        if sum in dict:
            if (counter-dict[sum]) > max_counter:
                max_counter = counter-dict[sum]
        else:
            dict[sum] = counter
        counter += 1
    return max_counter


n = int(input())
l = list(int(i) for i in input().strip().split(' '))
finalLen = subsetSum(l)
print(finalLen)
