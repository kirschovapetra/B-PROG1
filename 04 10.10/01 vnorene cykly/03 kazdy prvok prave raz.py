list = [1,2,3,2,4]
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



            





