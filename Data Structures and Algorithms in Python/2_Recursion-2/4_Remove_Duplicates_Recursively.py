# Remove Duplicates Recursively
# Given a string S, remove consecutive duplicates from it recursively.
# Input Format :
# String S
# Output Format :
# Output string
# Constraints :
# 1 <= Length of String S <= 10^3
# Sample Input :
# aabccba
# Sample Output :
# abcba

def removeConsecutiveDuplicates(string):
    if len(string)==0 or len(string)==1:
        return string
    else:
        output = removeConsecutiveDuplicates(string[1:])
        if string[0]==string[1]:
            return string[0]+output[1:]
        else:
            return string[0]+output
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
