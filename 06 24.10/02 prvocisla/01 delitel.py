def delitelnost(a,d):
    if a%d==0:
        return True
    if a%d>0:
        return False
cislo = 12
for i in range(1,cislo+1):
    if delitelnost(cislo,i) == True:
        print(i)
