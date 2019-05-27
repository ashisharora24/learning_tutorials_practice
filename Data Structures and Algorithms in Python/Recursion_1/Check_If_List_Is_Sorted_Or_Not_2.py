def Check_If_List_Is_Sorted_Or_Not(list,n=0):
    print(list[n:])
    if len(list[n:])==0 or len(list[n:])==1:
        return True
    else:
        if list[n]>list[n+1]:
            return False
        else:
            return Check_If_List_Is_Sorted_Or_Not(list,n+1)

print(Check_If_List_Is_Sorted_Or_Not([2,2,4,4,5,6]))
