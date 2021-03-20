def zorad(pole):
    for j in range(len(pole)):
        for i in range(len(pole)-1):
            if pole[i+1]<pole[i]:
                pole[i+1],pole[i]=pole[i],pole[i+1]
    return pole

t = 'abcba'
a = []
for i in range(len(t)):
    for j in range(i+1,len(t)):
        dvojica = t[i]+' '+t[j]
        dvojica = dvojica.split(' ')
        dvojica = zorad(dvojica)
        if (ord(dvojica[1])-ord(dvojica[0])==1) and (dvojica not in a):
            a.append(dvojica)
        dvojica = ''
print(a)
