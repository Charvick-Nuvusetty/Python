import re
fname=input("Enter file name")
tot=0
numlist=[]
file=open(fname)
for i in file:
    i=i.strip()
    num=re.findall('[0-9]+',i)
    if len(num)<1:
        continue
    for i in range(len(num)):
        number=int(num[i])
        numlist.append(number)
print(sum(numlist))
