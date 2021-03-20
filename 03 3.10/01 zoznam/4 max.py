list = []
for i in range(10):
    list.append(2**(i % 113))

max = 0
for i in range(10):
    if (list[i]>max):
        max = list[i]
print(max)
    
