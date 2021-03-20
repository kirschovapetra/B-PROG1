f = open('data.txt', 'r+')
riadky = []
sum = 0
riadok = f.readline()
while  riadok !='':
    riadky.append(riadok[:-1])
    sum += int(riadok[:-1])
    riadok = f.readline()
print(riadky)
print(sum/len(riadky))
f.close()
