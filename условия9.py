from math import *
a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
if D<0:
    print ('корней нет')
elif D==0:
    x=-b/2*a
    print (x)
else:
    x1=((-b+sqrt(D))/2*a)
    x2=((-b-sqrt(D))/2*a)
    print (x1,x2)