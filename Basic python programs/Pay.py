hours=float(input('Enter s' ))
rate=float(input('Enter Rate' ))
if hours>40:
    pay=hours*rate
    fp=(hours-40.0)*(rate*0.5)
else:
    pay=hours*rate

print(pay)
