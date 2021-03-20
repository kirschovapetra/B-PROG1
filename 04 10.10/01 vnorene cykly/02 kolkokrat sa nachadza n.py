import random
list = []
for i in range(10):
    list.append(random.randint(0,9))
    print(list[i])

n = int(input('zadaj n '))
pocet = 0
for i in range(10):
    if list[i]==n:
        pocet +=1
print(pocet)





