class Student:
    name="ashish arora"
    age=33
    marks=50
    passingMark=40

print(Student.name)
print(Student.age)
print(Student.marks)

S1 = Student()
print(S1.name)
print(S1.age)
print(S1.marks)

S1.name="Astha"
S1.age=32
S1.marks=80

print(Student.name)
print(Student.age)
print(Student.marks)

print(S1.name)
print(S1.age)
print(S1.marks)

print("---------------------------")
Student.age=25
print(Student.name)
print(Student.age)
print(Student.marks)

print(S1.name)
print(S1.age)
print(S1.marks)
