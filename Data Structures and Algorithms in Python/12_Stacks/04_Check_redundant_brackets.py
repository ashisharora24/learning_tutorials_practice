import queue

def checkRedundant(string):
    q = queue.LifoQueue()
    previousCount = -1
    currentCount = -1
    for i in range(len(string)):
#        print("--------------------")
        currLetter = string[i]
        if currLetter != ')':
            q.put(currLetter)
        if currLetter == ')':
            currentCount = 0
            while q.get() != '(':
                currentCount += 1
            if previousCount == -1:
                previousCount = currentCount
            else:
                if currentCount == 0:
                    return True
                else:
                    previousCount = -1
    return False

string = input()
ans = checkRedundant(string)
if ans is True:
    print('true')
else:
    print('false')
