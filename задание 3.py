a=int(input())
res = 1
for i in range (a):
    res = res * a
    a = a-2
    if a < 0:
        break
print (res)
    