str = input('')
res = ""
for i in range(len(str)):
    if (len(str)%(i+1)) == 0:
        res += str[i]
print(res)