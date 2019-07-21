# Maximum Frequency
# Send Feedback
# You are given with an array of integers that contain numbers in random order. Write a program to find and return the number which occurs maximum times in the given input.
# If more than one element occurs same number of times in the input, return the element which is present in the input first.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# Most frequent element
# Constraints :
# 1 <= N <= 10^5
# Sample Input 1 :
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6
# Sample Output 1 :
# 2
# Sample Input 2 :
# 3
# 1 4 5
# Sample Output 2 :
# 1
def maxFreq(l):
    max_k = 0
    max_v = 0

    dict = {}
    for ls in l:
        dict[ls] = dict.get(ls, 0) + 1
    max_k = 0
    max_v = 0
    for ls in l:
        if dict[ls] > max_v:
            max_v = dict[ls]
            max_k = ls
    return max_k

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
