s=input()
n=input()
k = s.split(' ')
w = n.split(' ')
a=[]
if (len(k)<len(w)) or (len(k)>len(w)):
    for i in range (len(k)):
        a.append(k[i])
        a.append(w[i])
    a=' '.join(a)
    print (a)
if (len(k)==len(w)):
    for i in range (len(k)):
        a.append(k[i])
        a.append(w[i])    
    a=' '.join(a)
    print (a)