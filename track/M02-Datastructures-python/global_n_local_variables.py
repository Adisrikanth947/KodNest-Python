c=45
def add():
    global a
    a=30
    b=40
    print(a+b)
    print (c)
add()
print(c)
x=100
def display():
    x=50
    print("Local x:",x)
display()
print("Global x:",x)

x=105
def display():
    x=50
    print("local:",x)
display()
print("Global:",x)

x=10
def display():
    print(x)
display()
x=20
print(x)
