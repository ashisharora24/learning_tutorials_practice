def Sum_of_digits(str,n=0):
    if n>=len(str):
        return 0
    output = Sum_of_digits(str,n+1)
    return output + int(str[n])

str=input()
print(Sum_of_digits(str))
#
#
# def Sum_of_digits(str,n=0):
#     print("len : " , type(len(str))
#     if n>len(str):
#         return 0
#     output = Sum_of_digits(n+1)
#     return output + int(str[n])
