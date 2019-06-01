def string_to_integer(str,start,end):
    if start>end:
        return 0
    output = string_to_integer(str,start+1,end)
    return output+int(str[start])*(10**(end-start))

str = input()
print(string_to_integer(str,0,len(str)-1))
