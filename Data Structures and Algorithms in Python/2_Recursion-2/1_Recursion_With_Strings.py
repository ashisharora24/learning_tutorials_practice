# def replace_char_in_string(str,a,b,n=0):
#     if len(str[n:])==0:
#         return ""
#     output = replace_char_in_string(str,a,b,n+1)
#     if str[n]==a:
#         return b+output
#     else:
#         return str[n]+output
#     return output
# print(replace_char_in_string("ashish","p","t"))

def replace_char_in_string(str,a,b):
    if len(str)==0:
        return str
    output = replace_char_in_string(str[1:],a,b)
    if str[0]==a:
        return b+output
    else:
        return str[0]+output
        
print(replace_char_in_string("ashhhh","h","t"))
