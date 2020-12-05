str1 = input()
str2 = list(str1)
for i in range (len(str2)):
    if ((str2[i]=='s') or (str2[i]=='S')) and str2[:-1] :
        str2[i] = str(str2[i-1]*2) + str(str2[i-2])
        print (str2)
#должен вывести ['t', 'e', 'eet', 't', '_', '__t', 't', 'r', 'i', 'n', 'g', 'ggs', 's'].
#ошибка в конце

        