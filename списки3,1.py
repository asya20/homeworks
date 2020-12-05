s=input('ââåäèòå ñëîâà ÷åðåç ïðîáåë:')
k=list(s)
k = s.split(' ')
if ('repeat' in k) and (type((k[-1:])==int)):
    n = int(''.join(k[-1:]))
    print (k[:-2] * n + k[-2:])
