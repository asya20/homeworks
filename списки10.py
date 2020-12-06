s=input()
k=int(input())
n = s.split(' ')
a=[]
b=[]
for i in range (k,len(n)):
    a.append(n[i])
for i in range (0,k):
    b.append(n[i])
print (a+b)  