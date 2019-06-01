def Pair_star(str,start,end):
    if start==end:
        return str
    if str[start]==str[start+1]:
        str=str[0:start+1]+"*"+str[start+1:]
        return Pair_star(str,start+2,end+1)
    else:
        return Pair_star(str,start+1,end)
str=input()
print(Pair_star(str,0,len(str)-1))
