names=("Adisri","sri","kanth","p","Adisri")
print(names,type(names),len(names))
print(names.count("Adisri"))#count is used to count the number of elements in the tuple
print(names.index("sri"))#index is used to find the index value of the element
print(names[3])#index value is 3 it will return the element at the index value of 3
print(names[0:3])#"Adisri","sri","kanth"# it will return the elements from the index value of 0 to 3 but not including 3
yn=names[0:2]
print(yn,type(yn))

#loop
for n in names:
    print(n)#adisri,sri,kanth,p,Adisri
fruits=("apple")
print(fruits,type(fruits))#str

#constructors
stu_inf=tuple(["sri",21,"Python"])
print(stu_inf,type(stu_inf))#('sri', 21, 'Python') <class 'tuple'>
n=1,2,3,4,5
print(n,type(n))# (1, 2, 3, 4, 5) <class 'tuple'>
#n[0]=44
#print(n)#TypeError: 'tuple' object does not support item assignment
#del n 
#print(n)#name error

age=[10,20]
age[1]=34
print(age)
fruits=("apple")
print(fruits*33,type(fruits))#appleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleappleapple



#tuple packing and unpacking
#unpacking
f=("apple","banana","orange")
(f1,f2,f3)=f
print(f1,f2,f3)
print(f1)
print(f2)
print(f3)
(f1,*f2)=f
print(f1)
print(f2,type(f2))
#packing
a=10
b=20
c=30
n=(a,b,c)
print(n,type(n))
a=(1,2,3)
b=(4,5,6)
c=a+b
print(a+b,type(a+b))
print(c)






