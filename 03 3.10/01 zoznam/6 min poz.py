list = []
for i in range(10):
    list.append(2**(i % 113))

min = list[0]
poz = 0
for i in range(10):
    if (list[i]<min):
        min = list[i]
        poz = i        
print(min,poz)
    
