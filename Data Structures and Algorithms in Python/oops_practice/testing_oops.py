import datetime


class Student:
    # you delcare all the variables here only
    name = "Ashish"
    age = 24

    def __init__(self):
        self.currentDT = str(datetime.datetime.now())

    def isPassed(self):
        print("self.name : ", self.name)
        print("self.age : ", self.age)
        print("self.currentDT : ", self.currentDT)
        if self.age > 20:
            print("Student Passed")
        else:
            print("Student failed")

    def hello():
        print("name : ", Student.name)


s1 = Student()
s1.name = "Astha"
print(s1.name)
print(s1.isPassed())

Student.hello()
# s1.hello()
