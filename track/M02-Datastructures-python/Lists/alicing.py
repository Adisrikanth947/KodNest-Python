marks=[70,81,60]
stu_marks=marks
stu_marks[0]=100
print(marks)
print(stu_marks)
first=[1,2,3]
second=first
print(first is second)
print(first==second)
first=[1,2,3]
second=[1,2,3]
print(first is second)
print(first==second)

#modification/mutation
num=[10,20]
val=num
val.append(30)
print(num)
print(val)


#reassignmnet
num=[10,20]
val=num
val=[100,200]
print(num)
print(val)