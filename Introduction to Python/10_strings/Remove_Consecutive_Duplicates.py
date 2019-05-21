# Remove Consecutive Duplicates

# Given a string, remove all the consecutive duplicates that are present in the given string.
# That means, if 'aaa' is present in the string then it should become 'a' in the output string.
# Sample Input:
# aabccbaa
# Sample Output:
# abcba

def Remove_Consecutive_Duplicates(str):
    last_char=str[0]
    new_str=str[0]
    for i in str[1:]:
        if i!=last_char:
            new_str+=i
            last_char=i
    return new_str

print(Remove_Consecutive_Duplicates(input()))
