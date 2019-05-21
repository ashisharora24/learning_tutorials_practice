# Largest Row or Column

# Given an NxM 2D array, you need to find out which row or column has largest sum (sum of its elements) overall amongst all rows and columns.
# Input Format :
#  Line 1 : 2 integers N and M respectively, separated by space
#  Line 2: Single line having N*M elements entered in row wise manner, each separated by space.
# Output Format :
#  If row sum is maximum then - "row" row_num max_sum
#  If column sum is maximum then - "column" col_num max_sum
# Note : If there are more than one rows/columns with maximum sum consider the row/column that comes first.
# And if ith row and jth column has same sum (which is largest), consider the ith row as answer.
# Sample Input 1 :
# 2 2
# 1 1 1 1
# Sample Output 1 :
# row 0 2
# Sample Input 2 :
# 3 3
# 3 6 9 1 4 7 2 8 9
# Sample Output 2 :
# column 2 25

def Largest_Row_or_Column(arr):
    id=-1
    type=""
    sum_all=0
    n,m=len(arr),len(arr[0])

    for i in range(n):
        sum_row=0
        for j in arr[i]:
            sum_row+=j
        if sum_row>sum_all:
            type="row"
            id=i
            sum_all=sum_row
    for i in range(m):
        sum_col=0
        for j in range(n):
            sum_col+=arr[j][i]
        if sum_col>sum_all:
            type="column"
            id=i
            sum_all=sum_col

    return [type,id,sum_all]

n,m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
d_arr = [[arr[(i*m)+j] for j in range(m)] for i in range(n)]
type,id,sum = Largest_Row_or_Column(d_arr)
print(type,id,sum)
