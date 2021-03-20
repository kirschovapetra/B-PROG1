p = [2,0,0,1]
l = [0]
sucet = 0
a = int(input('zadaj a '))

for i in range(4):
    sucet = p[i]+l[i]
    l.append(sucet*a)
print(sucet)
