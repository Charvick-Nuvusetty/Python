
l1=float(input('Enter L1 '))
#l1=float(l)
#print(l1)
l2=float(input('Enter L2 '))
px=int(input('Enter px '))
py=int(input('Enter py '))
c=(px*px)+(py*py)+(l1*l1-l2*l2)
print("C =",c)
st1_1=((4*c*py*l1)+(16*(c*c)*(py*py)*(l1*l1)-16*(l1*l1)*((px*px)+(py*py))*((c*c)-4*(px*px)*(l1*l1)))**0.5)/(8*(l1*l1)*((px**2)+(py**2)))
print("values of s theta 1 are")
print('st1_1 is ',st1_1)
st1_2=((4*c*py*l1)-(16*(c*c)*(py*py)*(l1*l1)-16*(l1*l1)*((px*px)+(py*py))*((c*c)-4*(px*px)*(l1*l1)))**0.5)/(8*(l1*l1)*((px**2)+(py**2)))
print('st1_2 is',st1_2)
st2_1=(py-l1*st1_1)/l2
print("The value of stheta 2 for st1_1 is ", st2_1)
st2_2=(py-l1*st1_2)/l2
print("The value of stheta 2 for st1_2 is ", st2_2)
