
def spiralPrint(arr):
    row_start=0
    col_start=0
    row_end=len(arr)
    col_end=len(arr[0])
    type="ascending"
    side="row"
    n=row_end+col_end-1


    for i in range (n):
        #print("-----------------------------")
        #print("i : ",i)
        check=True
        if i%2==0:
            if side=="row" and type=="ascending":
                for j in range(col_start,col_end):
                    #print("row : ",row_start," column : ",j)
                    print(arr[row_start][j],end=" ")
                    check=False
                side="column"
                row_start+=1
            if side=="row" and type=="descending":
                for j in range(col_end-1,col_start-1,-1):
                    #print("row : ",row_end-1," column : ",j)
                    print(arr[row_end-1][j],end=" ")
                    check=False
                side="column"
                row_end-=1
        else:
            if side=="column" and type=="ascending":
                for j in range(row_start,row_end):
                    #print("row : ", j," column : ",col_end-1)
                    print(arr[j][col_end-1],end=" ")
                    check=False
                side="row"
                type="descending"
                col_end-=1
            if side=="column" and type=="descending":
                for j in range(row_end-1,row_start-1,-1):
                    #print("row : ", j," column : ",col_start)
                    print(arr[j][col_start],end=" ")
                    check=False
                side="row"
                type="ascending"
                col_start+=1
        if check==True:
            break

l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)


        #3 6 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11 10 9 8
# 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
