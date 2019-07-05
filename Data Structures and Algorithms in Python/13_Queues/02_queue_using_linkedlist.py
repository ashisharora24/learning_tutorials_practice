class  Node():
    def __init__(self,data):
        self.data = data
        self.next =  None
class QueueUsingLinkedList:

    def __init__(self):
        self.__count = 0
        self.__head = None
        self.__tail = None

    def enqueue(self, data):
        n =  Node(data)
        if self.__head is None:
            self.__head = n
            self.__tail = n
        else:
            self.__tail.next = n
            self.__tail = n
        self.__count += 1

    def dequeue(self):
        if self.__head is None:
            return -1
        else:
            element = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1
            return element

    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.__head is None

    def front(self):
        if self.__head is None:
            return -1
        return self.__head.data

ll = QueueUsingLinkedList()
ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)
ll.enqueue(4)
ll.enqueue(5)
print("size : ", ll.size())

while (ll.isEmpty() is False):
    print(ll.front())
    ll.dequeue()
