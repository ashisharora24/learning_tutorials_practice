# 4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
def spiralPrint(arr):
    row_start=0
    col_start=0
    row_end=len(arr)-1
    col_end=len(arr[0])-1
    type="ascending"
    current_col=-1
    n=row_end+col_end-1
    for i in range (n):
        print ("***********************************","i : ",i," **********************")
        if i%2==0:
            if type=="ascending":
                print("----------------------------")
                print ("row ascending")
                print ("row_start : ",row_start,"\ncol_start : ",col_start,"\nrow_end : ",row_end,"\ncol_end : ",col_end,"\ncurrent_col : ",current_col)
                for j in range(col_start,col_end+1):
                    print (row_start,j)
#                type="decending"
                row_start+=1
                current_col=col_end
            if type=="decending":
                print("----------------------------")
                print("row descending")
                print ("row_start : ",row_start,"\ncol_start : ",col_start,"\nrow_end : ",row_end,"\ncol_end : ",col_end,"\ncurrent_col : ",current_col)
                for j in range(col_end,col_start-1,-1):
                    print (row_end,j)
                current_col=col_start
                row_end-=1
        else:
            if type=="ascending":
                print("----------------------------")
                print("column ascending")
                print ("row_start : ",row_start,"\ncol_start : ",col_start,"\nrow_end : ",row_end,"\ncol_end : ",col_end,"\ncurrent_col : ",current_col)
                for j in range(row_start,row_end+1):
                    print(j,current_col)
                    type="decending"
                    #col_start+=1
                col_end-=1
            if type=="decending":
                print("----------------------------")
                print("column descending")
                print ("row_start : ",row_start,"\ncol_start : ",col_start,"\nrow_end : ",row_end,"\ncol_end : ",col_end,"\ncurrent_col : ",current_col)
                for j in range(row_end,row_start,-1):
                    print(j,current_col)
                    type="ascending"
                    col_end-=1


#Main
str="4 4 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16"
l=[int(i) for i in str.strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
spiralPrint(arr)
