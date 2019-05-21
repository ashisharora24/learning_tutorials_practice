# Highest Occuring Character

# Given a string, find and return the highest occurring character present in the given string.
# If there are 2 characters in the input string with same frequency, return the character which comes first.
# Note : Assume all the characters in the given string are lowercase.
# Sample Input 1:
# 1`
# Sample Output 1:
# b
# Sample Input 2:
# xy
# Sample Output 2:
# x
def highest_occuring_character(str):

    high_count_value=str.count(str[0])
    high_count_char = str[0]
    for i in str[1:]:
        count=str.count(i)
        if count>high_count_value:
            high_count_value=count
            high_count_char=i
    return high_count_char
print(highest_occuring_character(input()))
