a = []
n = int(input('zadaj cislo '))
pocet_all = 0

while not n == 0:
    a.append(n)
    n = int(input('zadaj cislo '))
    pocet_all += 1
print('pocet = ',pocet_all)
for i in range(len(a)):
    print(a[i])
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i] == a[j]):
            print(a[i],'je duplicitne')

  

    
