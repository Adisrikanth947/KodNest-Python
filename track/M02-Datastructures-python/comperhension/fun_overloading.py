def add(a=0,b=0,c=0,d=0):
    return a+b+c+d
print(add(10,20))
print(add(10,20,30,40))
print(add())
#var *args
def add(*args):
    return args
print(add(10,20,30,40,50))

#sum uring var *args without gieving inbulit sum() function
def sum(*args):
    tot=0
    for i in args:
        tot+=i
    return tot
print(sum(10,20,30,40,50))
print(sum())

    
    
    