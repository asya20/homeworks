from math import *
a = input()
b = []
if type((a) == float):
    if (float(a) % 1.0 >= 0.5):
        a=int(float(a))+1
        b.append(a)
        print(b)
    elif type((a) == int):
        b.append(a)
if a=='True' or a=='False':
    b.append('boolean')