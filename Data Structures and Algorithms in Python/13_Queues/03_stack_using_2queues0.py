# You need to implement a Stack class using two queues as its data members.
# Only 2 data members should be there inside the class - two queues, which should be created dynamically and both should be public. Use the inbuilt queue.
# Implement the following public functions :
# 1. Constructor -
# Initialises both the data members.
# 2. push :
# This function should take one argument of type T and has return type void. This function should insert an element in the stack. Time complexity should be O(1).
# 3. pop :
# This function takes no input arguments and has return type T. This should removes the last element which is entered and return that element as an answer.
# 4. top :
# This function takes no input arguments and has return type T. This should return the last element which is entered and return that element as an answer.
# 5. getSize :
# Return the size of stack i.e. count of elements which are present ins stack right now. Time complexity should be O(1).

import queue
class StackUsingQueues:

    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.__count = 0
        self.__latestItem = None

    def push(self, data):
        self.q1.put(data)
        self.__count += 1
        self.__latestItem = data

    def pop(self):
        if self.getSize() == 0:
            return -1
        elif self.getSize() == 1:
            self.__count -= 1
            self.__latestItem = None
            return self.__s1.get()
        else:
            lastNode = self.s1.get()
            while self.q1.empty() is False:
                self.s2.put(lastNode)
                lastNode = self.s1.get()
            while self.s2.empty() is False:
                self.__latestItem = self.s2.get()
                self.s1.put(self.__latestItem)
            self.__count -= 1
            return lastNode

    def top(self):
        if self.getSize() == 0:
            return -1
        return self.__latestItem

    def getSize(self):
        return self.__count

s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    print("choice : ", choice)
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() !=0:
            print(s.q1.get(),end=' ')

    i+=1
