a = []
a_2 = []
n = int(input('zadaj cislo '))
pocet_all = 0
pocet_zap = 0
sum = 0
ap = 0
zap = False
while not n == 0:
    a.append(n)
    sum += n
    if (n < 0):
        pocet_zap += 1
        zap = True
    n = int(input('zadaj cislo '))
    pocet_all += 1
  
print('vsetkych =',pocet_all)
print('boli aj zaporne cisla?',zap)
print('zapornych =',pocet_zap)
print('suma =',sum)
ap = sum/pocet_all
print('priemer=',ap)

min = a[0]
for i in range(len(a)):
    if (a[i]<min):
        min = a[i]
print('minimum =',min)
print(a)
a.pop(remove)
print(a)        
min_2 = a[0]
for i in range(len(a)):
    if (a[i]<min_2):
        min_2 = a[i]
print('druhe minimum =',min_2)
    
    
