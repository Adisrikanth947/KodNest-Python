
class Student:
    company = "kodnest Technologies"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        a = 10
        print(f"{self.name} is studying")

    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)
    
    def trip(self):
        print(f"{self.name} goes for a trip")


s1 = Student("Srikanth", 22)
print(Student.company)
print(f"Company: {Student.company}")
print(s1.company)
s1.study()
s1.getDetails()
s1.trip()

print("\n")

s2 = Student("radha", 33)
s2.study()
