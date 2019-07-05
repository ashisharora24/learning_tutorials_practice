class QueueUsingTwoStacks:

    def __init__(self):
        self.__s1 = []
        self.__s2 = []
        self.__count = 0
        self.__first = 0

    def push(self, data):
        if self.__count == 0:
            self.__first = data
        self.__s1.append(data)
        self.__count += 1
        # print(self.__s1)

    def pop(self):
        if self.__count == 0:
            return 0
        elif self.__count == 1:
            self.__count -= 1
            self.__first = None
            return self.__s1.pop()
        else:
            #print("len(self.__s1)", len(self.__s1))
            while len(self.__s1) >0:
                self.__s2.append(self.__s1.pop())
            # print("self.__s2", self.__s2)
            self.__count -= 1
            element = self.__s2.pop()
            counter = 0
            while (len(self.__s2)>0):
                ele = self.__s2.pop()
                if counter == 0:
                    self.__first = ele
                    counter = 1
                self.__s1.append(ele)
            return element


    def top(self):
        return self.__first

    def getSize(self):
        return self.__count

    def isEmpty(self):
        return self.getSize()

q =  QueueUsingTwoStacks()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print("------------------")
while q.getSize()>0:
    print(q.pop())
