def replace_pi(str):
    if len(str)==0 or len(str)==1:
        return str
    else:
        output = replace_pi(str[1:])
        if str[0:2]=="pi":
            return "3.14"+output[1:]
        else:
            return str[0]+output

print(replace_pi("pi"))
