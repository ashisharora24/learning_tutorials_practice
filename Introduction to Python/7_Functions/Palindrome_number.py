# Palindrome number
# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
# Sample Input 1 :
# 121
# Sample Output 1 :
# true
# Sample Input 2 :
# 1032
# Sample Output 2 :
# false

def checkPalindrome(num):
    num=str(num)
    reverse_num=num[::-1]
    if num==reverse_num:
        return True
    return False

num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
