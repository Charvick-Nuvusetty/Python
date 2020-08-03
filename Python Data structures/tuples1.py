name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    line=line.rstrip()
    if  not line.startswith('From '):
        continue
    list=line.split()
    #print(list)
    t=list[5]
    #print(t)
    time=t.split(':')
    #print(time)
    ft=time[0]
    #print(ft)
    if ft in count:
        count[ft]=count[ft]+1
    else:
        count[ft]=1
    #print(count)
list1=sorted([(k,v)for k,v in count.items()])
#print(list1)
for key,value in list1:
    print(key,value)
