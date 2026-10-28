s=[]
for i in range(1,6):
    s.append(i*i)
print(s)
s=[i*i for i in range(1,6)]
print(s)
n=[i for i in range(1,11) if i%2==0]
print(n)
n=[10,20,30,40,50]
n1=[i if i>25 else 0 for i in n]
print(n1)
