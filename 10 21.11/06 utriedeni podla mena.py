f = open('data2.txt','r+')
riadok = f.readline()
ziaci = {}
zoz_mien = []
while riadok:
    meno = riadok[:2]
    bodov = riadok[3:-1]
    ziaci[meno] = int(bodov)
    zoz_mien.append(meno)
    riadok = f.readline()
print(ziaci)

for i in range(len(zoz_mien)):
    for j in range(len(zoz_mien)-1):
        if zoz_mien[j+1]<zoz_mien[j]:
            zoz_mien[j+1],zoz_mien[j]=zoz_mien[j],zoz_mien[j+1]
        if zoz_mien[j+1]==zoz_mien[j]:
            if ziaci[zoz_mien[j+1]]<ziaci[zoz_mien[j]]:
                zoz_mien[j+1],zoz_mien[j]=zoz_mien[j],zoz_mien[j+1]


f.write('\nutriedeni podla mena\n')
for i in zoz_mien:
    f.write(i+' '+str(ziaci[i]))
    f.write('\n')

f.close()
