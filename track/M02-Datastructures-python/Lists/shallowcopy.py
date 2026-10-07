#normal assignment(not copy)
original=[[10,20],[30,40]]
copy=original
copy[0][0]=100
print(copy)#[[100, 20], [30, 40]]
print(original)#[[100, 20], [30, 40]]

a=[[10,20,3,4,5,6],[20,30,4,4,4,]]
b=a.copy()
b[0][0]=100
print(a)#[[10, 20], [30, 40]]
print(b)#[[100, 20], [30, 40]]

#shallow copy
original=[[10,20],[30,40]]
copy=original.copy()
copy[0][0]=100
print(copy)#[[100, 20], [30, 40]]
print(original)#[[100, 20], [30, 40]]

#deep copy
import copy
original=[[10,20],[30,40]]
copy=copy.deepcopy(original)
copy[0][0]=100

print(original)#[[10, 20], [30, 40]]
print(copy)#[[100, 20], [30, 40]]


