import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def return_expression(expre):
    if expre in'{[(':
        return 0
    elif expre == '}':
        return '{'
    elif expre == ']':
        return '['
    elif expre == ')':
        return '('
    else:
        return -1



def checkBalanced(expr):
    q = queue.LifoQueue()
    for i in range(len(expr)):
        currItem = expr[i]
        revItem = return_expression(currItem)
        if revItem == 0:
            q.put(currItem)
        elif revItem != -1:
            if q.empty():
                return False
            else:
                if q.get() != revItem:
                    return False
    if q.empty():
        return True
    else:
        return False


exp=input()
if checkBalanced(exp):
    print('true')
else:
    print('false')
