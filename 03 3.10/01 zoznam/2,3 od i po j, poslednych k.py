list = []
for i in range(10):
    list.append(2**(i % 113))

i = int(input('zadaj i '))
j = int(input('zadaj j '))
k = int(input('zadaj k '))

for i in range(i,j+1):
    print(list[i])

dlzka = len(list)

for t in range(dlzka-k,dlzka):
    print(list[t])


