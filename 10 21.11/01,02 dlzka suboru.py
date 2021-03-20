#zapis pocet cisel do suboru
import random
f = open('data.txt', 'r+')
n = random.randint(5,15)
for i in range(n):
    f.write(str(random.randint(0,20)))
    f.write('\n')
f.close()

f = open('data.txt', 'r+')
subor = f.readlines()
print(subor,'=',len(subor))
f.close()
