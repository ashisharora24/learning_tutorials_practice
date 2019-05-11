# Triplet Sum

# Given a random integer array and a number x.
# Find and print the triplets of elements in the array which sum to x.
# While printing a triplet, print the smallest element first.
# That is, if a valid triplet is (6, 5, 10)
# print "5 6 10".
# There is no constraint that out of 5 triplets which have to be printed on 1st line.
# You can print triplets in any order, just be careful about the order of elements in a triplet.
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
def print_sequence(a,b,c):
    if a<=b<=c:
        print(a," ",b," ",c)
    elif b<=a<=c:
        print(b," ",a," ",c)
    elif a<=c<=b:
        print(a," ",c," ",b)
    elif c<=a<=b:
        print(c," ",a," ",b)
    elif b<=c<=a:
        print(b," ",c," ",a)
    elif c<=b<=a:
        print(c," ",b," ",a)

def pair_sum(array,x):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            for k in range(j+1,len(array)):
                if array[k]+array[j]+array[i]==x:
                    print_sequence(array[k],array[j],array[i])

n=int(input())
array = [int(i) for i in input().split()]
x=int(input())
pair_sum(array,x)
