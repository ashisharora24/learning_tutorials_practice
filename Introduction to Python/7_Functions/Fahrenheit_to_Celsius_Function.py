# Fahrenheit to Celsius Function
# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
# Input Format :
# 3 integers - S, E and W respectively
# Output Format :
# Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
# Sample Input :
# 0
# 100
# 20
# Sample Output :
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37

def fahrenheit_to_celsius(f):
    return int(((f-32)*5)/9)

# S=int(input())
# E=int(input())
# W=int(input())
# for i in range(S,E+1,W):
#     print(i," ",fahrenheit_to_celsius(i))


def printTable(start,end,step):
    for i in range(start,end+1,step):
        print(i," ",fahrenheit_to_celsius(i))


s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
