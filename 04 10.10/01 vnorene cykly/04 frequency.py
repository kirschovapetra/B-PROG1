list = [0,0,1,2,2,1,0,1,1]
print(list)
unique = []
for i in range(len(list)):
    pocet = 0
    for j in range(i+1,len(list)):
        if (list[i] == list[j]):
            pocet +=1
    if (pocet == 0):
        unique.append(list[i])
print(unique)



frequency = []
for i in range(len(unique)):
    pocet = 0
    for j in range(len(list)):
        if unique[i]==list[j]:
            pocet +=1
    frequency.append(pocet)

print(frequency)
    


            





