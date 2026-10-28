class Emplyoee:
    def __init__(self, name,age,salary):
        self.name = name
        self.age =age
        self.salary = salary
    def work(self):
        print(f"{self.name} is working in a company and his/her age is {self.age} years and salar{self.salary}y is ")
    
ss = Emplyoee("Srikanth",22,80000)
print(f"name: {ss.name}\nage: {ss.age}\nsalary: {ss.salary}")

ss.work()




