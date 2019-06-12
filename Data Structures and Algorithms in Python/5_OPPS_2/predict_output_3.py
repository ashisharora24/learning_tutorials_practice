class Vehicle:
     def __init__(self,color):
         self.__color = color
class Car(Vehicle):
    def __init__(self,color,numGears):
        super().__init__(color)
        self.numGears = numGears
    def printCar(self):
        print(c.__color,end=" ")
        print(c.numGears)
c = Car("black",5)
c.printCar()
