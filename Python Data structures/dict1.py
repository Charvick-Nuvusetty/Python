fname = input("Enter file name: ")
if len(fname) < 1 :
     fname = "mbox-short.txt"
fh = open(fname)
lines=dict()
emails=[]
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("From "):
        continue
    list=line.split()
    #print(list)
    emails=list[1]
    print(emails)
    for word in emails:
        print('###')
        print(word)
