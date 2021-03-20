list = []
for i in range(10):
    list.append(2**(i % 113))
print(list)
n = int(input('zadaj cislo '))
poz = 0

for i in range(10):
    if (n == list[i]):
        poz = i
        break
else:
    poz = -1
print(poz)

    
