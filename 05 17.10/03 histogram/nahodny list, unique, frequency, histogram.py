import random
n = 100
list = []
for i in range(n):
    list.append(random.randint(0,20))
print('list',list)
unique = []
for i in range(len(list)):
    if not (list[i] in unique):
        unique.append(list[i])
print('unique',unique)

for i in range(len(unique)):
    pocet = 0
    for j in range(len(list)):
        if (unique[i] == list[j]):
            pocet +=1
    #print(unique[i],'pocet =',pocet)

frequency = []
for i in range(len(unique)):
    pocet = 0
    for j in range(len(list)):
        if (unique[i] == list[j]):
            pocet += 1
    frequency.append(pocet)
print('frequency',frequency)

for i in range(len(frequency)):
    print(unique[i],frequency[i]*'*')

        
