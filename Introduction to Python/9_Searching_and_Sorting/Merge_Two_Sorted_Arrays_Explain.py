# Code Merge Two Sorted Arrays
#
# Given two sorted arrays of Size M and N respectively, merge them into a third array such that the third array is also sorted.
# Input Format :
#  Line 1 : Size of first array i.e. M
#  Line 2 : M elements of first array separated by space
#  Line 3 : Size of second array i.e. N
#  Line 2 : N elements of second array separated by space
# Output Format :
# M + N integers i.e. elements of third sorted array separated by spaces.
# Constraints :
# 1 <= M, N <= 10^6
# Sample Input :
# 5
# 1 3 4 7 11
# 4
# 2 4 6 13
# Sample Output :
# 1 2 3 4 4 6 7 11 13


def merge_sort(n_arr,m_arr,n,m):
    arr=[]
    indexM=0
    indexN=0
    while (indexM<m and indexN<n):
        if n_arr[indexN]<m_arr[indexM]:
            arr.append(n_arr[indexN])
            indexN+=1
        else:
            arr.append(m_arr[indexM])
            indexM+=1
    if indexN==n:
        arr.extend(m_arr[indexM:])
    else:
        arr.extend(n_arr[indexN:])
    return arr



n=int(input())
n_arr = [int(i) for i in input().split()]
m=int(input())
m_arr = [int(i) for i in input().split()]
arr=merge_sort(n_arr,m_arr,n,m)
[print(i,end=" ") for i in arr]
