# Compress the String

# Write a program to do basic string compression.
# For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
# For e.g. if a String has 'x' repeated 5 times, replace this "xxxxx" with "x5".
# Note : Consecutive count of every character in input string is less than equal to 9.
# Input Format :
# Input string S
# Output Format :
# Compressed string
# Sample Input:
# aaabbccdsa
# Sample Output:
# a3b2c2dsa

def compress_string(string):
    last_char=string[0]
    last_count=1
    new_str=""
    for i in string[1:]:
        if i!=last_char:
            if last_count==1:
                new_str=new_str+last_char
            else:
                new_str=new_str+last_char+str(last_count)
            last_char=i
            last_count=1
        else:
            if last_count==9:
                new_str=new_str+last_char+str(9)
                last_count=1
            else:
                last_count+=1
    if last_count==1:
        new_str=new_str+last_char
    else:
        new_str=new_str+last_char+str(last_count)
    return new_str
print(compress_string(input()))
