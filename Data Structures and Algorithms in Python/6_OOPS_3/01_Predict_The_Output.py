from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def fun1(self):
        pass

    @abstractmethod
    def fun2(self):
        pass

o = A()
o.fun1()
