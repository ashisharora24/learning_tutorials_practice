# Array intersection

# Given two random integer arrays of size m and n, print their intersection. That is, print all the elements that are present in both the given arrays.
# Input arrays can contain duplicate elements.
# Note : Order of elements are not important
# Input format :
# Line 1 : Array 1 Size
# Line 2 : Array 1 elements (separated by space)
# Line 3 : Array 2 Size
# Line 4 : Array 2 elements (separated by space)
# Output format :
# Print intersection elements in different lines
# Constraints :
# 1 <= m, n <= 10^3
# Sample Input 1 :
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7
# Sample Output 1 :
# 2
# 4
# 3
# Sample Input 2 :
# 4
# 2 6 1 2
# 5
# 1 2 3 4 2
# Sample Output 2 :
# 2
# 2
# 1
def arrayIntersection(m_array,n_array):
    for i in m_array:
        for j in range(len(n_array)):
            if i==n_array[j]:
                print(i)
                n_array.pop(j)
                break

m = int(input())
m_array = [int(i) for i in input().split()]
n = int(input())
n_array = [int(i) for i in input().split()]
arrayIntersection(m_array,n_array)
