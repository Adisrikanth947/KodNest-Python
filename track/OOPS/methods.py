
class Student:
    company = "kodnest Technologies"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    #instance method -
    def study(self):
        a = 10
        print(f"{self.name} is studying")

    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)
    @staticmethod
    def trip(name):
        print(f"{name} goes for a trip")
    @classmethod
    def change_company(cls , new_company):
        cls.company = new_company

Student.change_company("Kodnest Tecnologies pvt")

s1 = Student("Srikanth", 22)
print(Student.company)
print(f"Company: {Student.company}")
print(s1.company)
s1.study()
s1.getDetails()
Student.trip(s1.name)
print(s1.name)

print("\n")

s2 = Student("radha", 33)
Student.trip(s2.name)
print(s2.name)
s2.study()
