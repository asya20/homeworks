str1=input()
str2=''
a = list(str1)
if ('!!!' in str1) and (a[0] !='!') and (a[1] != '!') and (a[2] != '!'):
    print ('exclaim')
else:
    print ('nota bene')
    for i in range (len(a)):
        if a[i] != '!':
            str2=str2+ a[i]
print (str2)
if '???' in str1:
    print ('question')
elif '???' and '!!!' in str1:
    print('nothing')
elif '???' and '!!!' not in str1:
    print ('random')