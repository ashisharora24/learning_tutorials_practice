class QueueUsingArray:

    def __init__(self):
        self.__arr = []
        self.__front = 0
        self.__size = 0

    def enqueue(self,data):
        self.__arr.append(data)
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            return -1
        element = self.__arr[self.__front]
        self.__front += 1
        self.__size -= 1
        return element

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def front(self):
        if self.__size == 0:
            return -1
        return self.__arr[self.__front]


q = QueueUsingArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size())
while (q.isEmpty() is False):
    print(q.front())
    q.dequeue()
