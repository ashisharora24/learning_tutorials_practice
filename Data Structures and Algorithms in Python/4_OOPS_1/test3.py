class Student:
    def __init__(self,name,age):
        self.__name = name
        self.age = age
    def print_student_details():
        print(self.__name, end= " ")
        print(self.age)
s = Student("Rohan",20)
print(s.name)
