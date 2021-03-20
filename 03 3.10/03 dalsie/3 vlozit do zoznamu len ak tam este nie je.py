a = []
n = int(input('zadaj cislo '))
pocet_all = 0

while not n == 0:
    for i in range(len(a)):
        if (n == a[i]):
            print(n,'sa uz v zozname nachadza')
            break
    else:
        a.append(n)
    n = int(input('zadaj cislo '))
    pocet_all += 1
print('pocet = ',pocet_all)
for i in range(len(a)):
    print(a[i])


  

    
