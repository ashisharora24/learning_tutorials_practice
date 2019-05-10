# Fibonacci MemberFibonacci Member
# Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
#     F(n) = F(n-1) + F(n-2)
# Input Format :
# Integer N
# Output Format :
# true or false
# Sample Input 1 :
# 5
# Sample Output 1 :
# true
# Sample Input 2 :
# 14
# Sample Output 2 :
# false

def check_if_number_is_member_of_fibonacci(n):
    status=False
    i=0
    a = 0;
    b = 1;
    n_value=1
    while n_value<=n:
        n_value=a+b
        if n_value==n:
            status=True
            break
        a=b
        b=n_value
    return status


n = int(input())
print(check_if_number_is_member_of_fibonacci(n))
