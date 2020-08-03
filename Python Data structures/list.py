fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word=line.rstrip().split()
    for i in word:
        if i in lst:
            continue
        else:
            lst.append(element)
lst.sort()
print(lst)        
