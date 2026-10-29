class Student:
    name = "Srikanth"
    age = 22
    marks = 90

    def study(self):
        print(f"{self.name} is studying {self.age} years")
    
    def play(self):
        print(f"{self.name} is playing {self.age} years")

s = Student()
ss = Student()

ss.name = "Adi"
ss.age = "34"

print(s.name)
print(s.age)
print(s.marks)
print(ss.name)
print(ss.age)

s.study()
s.play()
