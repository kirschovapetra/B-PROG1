list = []
for i in range(5):
    list.append(i)
print(list)
print('\n')

'''prvy = list[0]  
for i in range(4):
    list[i] = list[i+1]
    
for i in range(4):  
    print(list[i])
print(prvy)
print('\n')'''

x = int(input('zadaj x '))
for i in range(x):
    posledny = list[len(list)-1]
    j = len(list)-1
    while (j>0):
        list[j] = list[j-1]
        j -= 1
    list[0] = posledny
        

print(list)
    

    
    
