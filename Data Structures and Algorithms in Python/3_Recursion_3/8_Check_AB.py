# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'

def Check_AB(str,n=0):
#    print("--------------")
#    print("str : ", str)
    output="true"
    if n>=len(str):
        output="true"
    if n==0:
        if str[0]!="a":
            output = "false"
    if output=="true":
        if str[n:n+2]=="aa":
            if n+2<len(str):
                output = Check_AB(str,n+1)
        elif str[n:n+3]=="abb":
            if n+3<len(str):
                output = Check_AB(str,n+1)
        elif str[n:n+3]=="bba":
            if n+3<len(str):
                output = Check_AB(str,n+2)
        else:
            output = "false"
    return output
str=input()
print(Check_AB(str))
