class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackUsingLL:

    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self, data):
        s = Node(data)
        temp = self.__head
        self.__head = s
        self.__head.next = temp
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return 0
        pop = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return pop

    def top(self):
        if self.__size == 0:
            return 0
        return self.__head.data

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

def countBracketReversals(string):
    s = StackUsingLL()
    for i in range(len(string)):
        currValue = string[i]
        print(currValue)
        if currValue == '{':
            s.push(currValue)
            print("added value : ", currValue)
        elif currValue == '}':
            if s.isEmpty():
                s.push(currValue)
                print("added value : ", currValue)
            else:
                if s.top() == '{':
                    s.pop()
                else:
                    s.push(currValue)
                    print("added value : ", currValue)
    count = 0
    # print("************************")
    if s.isEmpty():
        print("is empty")
        return 0
    else:
        print("Not empty")
        if s.getSize() == 1:
            return -1
        else:
            while s.getSize() > 1:
                print("************************")
                lastValue = s.pop()
                secondlastValue = s.pop()
                print("lastValue : ", lastValue)
                print("secondlastValue : ", secondlastValue)
                if lastValue == '{' and secondlastValue == '}':
                    print("1")
                    pass
                elif lastValue == '{' and secondlastValue == '{':
                    count += 1
                    print("2")
                elif lastValue == '}' and secondlastValue == '}':
                    count += 1
                    print("3")
                elif lastValue == '}' and secondlastValue == '{':
                    count += 2
                    print("4")
            if s.getSize() == 1:
                return -1
            else:
                return count


string = input()
ans = countBracketReversals(string)
print(ans)
