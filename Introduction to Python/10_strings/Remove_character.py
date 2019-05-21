# Remove character

# Given a string and a character x. Write a function to remove all occurrences of x character from the given string.
# Leave the string as it is, if the given character is not present in the string.
# Input format :
#
# Line 1 : Input string
#
# Line 2 : Character x
#
# Sample Input :
# welcome to coding ninjas
# o
# Sample Output :
# welcme t cding ninjas

def remove_character(str,char):
    arr=str.split(char)
    new_string=arr[0]
    for i in arr[1:]:
        new_string+=i
    return new_string

str=input()
char=input()
print(remove_character(str,char))
