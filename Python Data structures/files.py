fname=input("Enter file name:")
fh=open(fname)
count=0
total=0
avg=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    num=float(line[21:])
    total=total+num
avg=total/count
print(total)
print("Average spam confidence:",avg)
