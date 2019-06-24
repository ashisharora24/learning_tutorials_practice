from sys import setrecursionlimit


def reverseStack(s1, s2):
    if (len(s1) <= 1):
        return

    while (len(s1) != 1):
        ele = s1.pop()
        s2.append(ele)

    lastElement = s1.pop()

    while (len(s2) != 0):
        s1.append(s2.pop())

    reverseStack(s1, s2)
    s1.append(lastElement)


setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1, s2)
while(len(s1) != 0):
    print(s1.pop(), end=' ')
