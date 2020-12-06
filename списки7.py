from math import *
a = input()
b = []
if type((a) == float):
    if float(a) % 1.0 >= 0.5:
        a=int(float(a))+1
        b.append(a)
        print(b)
    else:
        a=int(float(a))
        b.append(a)
        print(b)
elif type((a) == int):
    a=int(a)
    b.append(a)
    print (b)
elif (a =='True') or (a == 'False'):
    a=bool(a)
    b.append(a)
    print(b)
else:
    print ('nothing')
#ошибка проверяется только на float 
    