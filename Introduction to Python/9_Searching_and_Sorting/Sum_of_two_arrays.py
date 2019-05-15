# Sum of two arrays
# Two random integer arrays are given A1 and A2, in which numbers from 0 to 9 are present at every index (i.e. single digit integer is present at every index of both given arrays).
# You need to find sum of both the input arrays (like we add two integers) and put the result in another array i.e. output array (output arrays should also contain only single digits at every index).
# The size A1 & A2 can be different.
# Note : Output array size should be 1 more than the size of bigger array and place 0 at the 0th index if there is no carry. No need to print the elements of output array.
# Input format :
# Line 1 : Integer n1 (A1 Size)
# Line 2 : A1 elements (separated by space)
# Line 3 : Integer n2 (A2 Size)
# Line 4 : A2 elements (separated by space)
# Output Format :
# Output array elements (separated by space)
# Constraints :
# 1 <= n1, n2 <= 10^6
# Sample Input 1:
# 3
# 6 2 4
# 3
# 7 5 6
# Sample Output 1:
# 1 3 8 0
# Sample Input 2:
# 3
# 8 5 2
# 2
# 1 3
# Sample Output 2:
# 0 8 6 5

def sum_array(n_arr,m_arr,n,m):
    # running loop on index on reverse order
	# -1, -2, to the max index avaiable
    i=-1
    arr=[]
    carry=0
    while i>=-m or i>=-n:
        # since the size of the array element may not be same , so assigning 0 to element which do not exist.
        n_val = n_arr[i] if i>=-n else 0
        m_val = m_arr[i] if i>=-m else 0
        sum=(n_val)+(m_val)+carry
        carry=sum//10
        arr.insert(0,sum%10)
        i=i-1
    arr.insert(0,carry)
    return arr



n=int(input())
n_arr=[int(i) for i in input().split()]
m=int(input())
m_arr=[int(i) for i in input().split()]
arr=sum_array(n_arr,m_arr,n,m)
[print(i,end=" ") for i in arr]
