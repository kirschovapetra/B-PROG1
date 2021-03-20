sum = 0
a = [] 
for i in range(101):
    sum = sum + 1/(2**i)
    a.append(sum)
print(a)

for i in range(100):
    if (a[i] == a[i+1]):
        print(i)
        break
        
        

