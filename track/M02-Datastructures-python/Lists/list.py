n= [1,2,3,4,5,3]
print(n)
print(n[3])
print(type(n))
print(len(n))
print(n[-4:-1])
#list of students 
s=list([45.7,True,2,3,3,"sri"])
print(type(s))
print(s,type(s))
#adding elements
n=[1,2,3,4,5]
n.append(6)
print(n)#123456
n.insert(0,3)#0=postion of index ,3=value #3123456
print(n)#3123456
n.extend([10,20,30])#it will add the elements from the list
print(n)#3123456102030
n.pop()#pop will do remove last element  but we give index position it remove that element
print(n)#312345
n.pop(0)#0=index value it will remove at that position element
print(n)#12345
n=[220,3,4,5,665,5453,20]
n.remove(20)#it will remove the value of element
print(n)#2203456655453
n.clear()#it will remove all the elements from the list
print(n)#[]
#changing elements 
n=[1,2,3,4,5,3]
n[5]=6#index values can be changed
print(n)#123456
n[1:4]=[20,30,40]#it slice value can be changed
print(n)#120304056

n=[1,2,3,4,5,3]
n.append(6)
n.insert(0,3)
n.extend([10,20,30])
print(n)

##copy
a=[1,2,3]
b=a.copy()#it will copy the elements from the list to another list
print(b)#123
##count
l=[1,2,3452,3,6,4,44,4,2,4,]
l.count(4)
print(l.count((4)))#4 is repeated 4 times
##sorting
x=[6,4,3,8,1,2,3,5,7]
x.sort()#it will sort the elements in ascending order
print(x)#123345678
x.sort(reverse=True)#it will sort the elements in descending order
print(x)#876543321

a=[1,2,3]
b=a.copy()#it will copy the elements from the list to another list
print(b.index(3))#it will return the index value of the element #3=index value is 2

