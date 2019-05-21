# Reverse Each Word

# Given a string S, reverse each word of a string individually. For eg. if a string is "abc def", reversed string should be "cba fed".
# Input Format :
# String S
# Output Format :
# Updated string
# Constraints :
# 1 <= Length of S <= 1000
# Sample Input :
# Welcome to Coding Ninjas
# Sample Output:
# emocleW ot gnidoC sajniN

def reverse_each_word(str):
    arr=str.split()
    new_str=arr[0][::-1]
    for word in arr[1:]:
        new_str=new_str+" "+word[::-1]
    return new_str
print(reverse_each_word(input()))
