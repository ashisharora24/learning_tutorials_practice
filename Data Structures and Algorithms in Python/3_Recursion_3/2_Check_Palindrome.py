def Check_Palindrome(str,n=0):
    # print("---------------------------")
    # print("n : ", n)
    if n>len(str)//2:
        # print("if condition true")
        return True

    if str[n]==str[-1-n]:
        # print("TRUE")
        return Check_Palindrome(str,n+1)
    else:
        return False

str = input()
print(Check_Palindrome(str))
