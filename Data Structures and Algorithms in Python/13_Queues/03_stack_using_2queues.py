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
            # print("SIZE ONE")
            self.__count -= 1
            self.__latestItem = None
            return self.q1.get()
        else:
            lastNode = self.q1.get()
            #print("lastNode : ", lastNode)
            while self.q1.empty() is False:
                # print("lastNode : ", lastNode)
                self.q2.put(lastNode)
                lastNode = self.q1.get()
            while self.q2.empty() is False:
                self.__latestItem = self.q2.get()
                self.q1.put(self.__latestItem)
            self.__count -= 1
            return lastNode

    def top(self):
        if self.getSize() == 0:
            return -1
        return self.__latestItem

    def getSize(self):
        return self.__count

s = StackUsingQueues()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)

print(s.getSize())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
