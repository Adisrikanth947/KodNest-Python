l=["python","java","python","java","java","python"]
frequecy={}
for lang in l:
    if lang in frequecy:
        frequecy[lang]+=1
    else:
        frequecy[lang]=1
print(frequecy)
#using counter
from collections import Counter
l=["python","java","python","java","java","python","SQL"]
frequency=Counter(l)
print(frequency)
print(frequency['python'])
print(frequency['java'])
print(frequency['SQL'])

ll=["python","java","python","java","java"]
frequency=Counter(ll)
for lang, count in frequecy.items():
    print(ll,count)
letter_counts=Counter("rfewkjfbwekjfweiufoer")
print(letter_counts)
    