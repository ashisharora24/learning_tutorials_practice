class Parent():

    name="ashish"
    age="32"
    surname="arora"
    category="hindu"

    def __init__(self,name="ashish",age="32",surname="arora",religion="hindu"):
        self.name=name
        self.surname=surname
        self.age=age
        self.__category=religion

    def print_info(self):
        print("------- Printing info ---------------")
        print("Name : ",self.name)
        print("Surname : ",self.surname)
        print("Age : ", self.age)
        print("Category : ",self.__category)
        _
        for :
            count++

    @staticmethod
    def static():
        print(" this is static and cannot be modified")
        print("Name : ",Parent.name)
        print("Surname : ",Parent.surname)
        print("Age : ", Parent.age)
        print("Category : ", Parent.category)


class Child(Parent):
    def __init__(self,name="ashish",age="32",surname="arora",religion="hindu",father_name="I B Arora"):
        super().__init__(name,age,surname,religion)
        self.father_name=father_name

    def child_details(self):
        print("Name : ",self.name)
        print("Surname : ",self.surname)
        print("Age : ", self.age)
        print("Category : ",self.__category)
        print("father_name : ",self.father_name)

S1=Child()
S1.child_details()
