# Remove X
# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# Sample Input 2 :
# abc
# Sample Output 2:
# abc
# Sample Input 3 :
# xx

# Problem: Remove x from string
def removeX(string):
    if len(string)==0:
        return ""
    output = removeX(string[1:])
    if string[0]=="X" or string[0]=="x":
        return output
    else:
        return string[0]+output[1:]

# Main
string = input()
print(removeX(string))
