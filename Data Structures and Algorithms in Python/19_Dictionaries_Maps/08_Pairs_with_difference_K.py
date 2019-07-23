# Pairs with difference K
# Send Feedback
# You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
# Best solution takes O(n) time. And take difference as absolute.
# Input Format :
# Line 1 : Integer n, Size of array
# Line 2 : Array elements (separated by space)
# Line 3 : K
# Output format :
# Print pairs in different lines (pair elements separated by space). In a pair, smaller element should be printed first.
# (Order of different pairs is not important)
# Constraints :
# 1 <= n <= 5000
# Sample Input 1 :
# 4
# 5 1 2 4
# 3
# Sample Output 1 :
# 2 5
# 1 4
# Sample Input 2 :
# 4
# 4 4 4 4
# 0
# Sample Output 2 :
# 4 4
# 4 4
# 4 4
# 4 4
# 4 4
# 4 4
def printPairDiffK(list, k):
    dict = {}

    for i in list:
        dict[i] = dict.get(i, 0) + 1

    print(dict)

    for i in list:
        if k != 0:
            num1 = i + k
            if num1 in dict:
                for j in range(dict[num1]):
                    print(i,num1)
            num2 = i - k
            if num2 in dict:
                for j in range(dict[num2]):
                    print(num1, i)
        else:
            if i in dict:
                for j in range(dict[i]-1):
                    print(i,i)
        dict[i] -= 1

#n = int(input())
# list = list(int(i) for i in input().strip().split(' '))
# k = int(input())
list = [4, 4, 4, 4]
k = 0
printPairDiffK(list, k)
