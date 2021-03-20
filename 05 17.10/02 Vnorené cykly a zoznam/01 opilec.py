import random
n = int(input('zadaj neparne n'))
mesto = ['home']
for i in range(0,n):
    mesto.append('.')
mesto.append('pub')

poz = (n+1)//2
mesto[poz] = 'O'
for i in range(0,n+2):
    print(mesto[i],end='')
print('\n')

j = 0
domov = 0
krcma = 0
zaspal = 0
for i in range(100):
    while j<20:
        posun = random.randint(-1,1)
        mesto[poz],mesto[poz+posun] = mesto[poz+posun],mesto[poz]
        poz = poz+posun
        for i in range(0,n+2):
            print(mesto[i],end='')
        print('\n')
        if (poz == 0):
            print('je doma')
            domov +=1
            break
        if (poz == n+1):
            print('je v krcme')
            krcma +=1
            break
        j +=1
    if j==20:
        print('zaspal')
        zaspal +=1
        break
print('domov sa dostal',domov,'-krat')
print('do krcmy sa dostal',krcma,'-krat')
print('zaspal',zaspal,'-krat')
    



