
class Student:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def study(self):
        print(f"{self.name} is Studying")

    def getDetails(self):
        
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)

    def trip(self):
        print(f"{self.name} goes for a trip")


s1 = Student("rahul", 20, "kodnest")
s1.study()
s1.trip()
s1.getDetails()

print("\n")

s2 = Student("Srikanth", 22, "Kodnest")
print(s2.name)
s2.study()
s2.trip()
s2.getDetails()
