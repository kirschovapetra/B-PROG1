n = 10
a = []
for i in range(2,n+1):
    a.append(i)
print(a)
#a = [2,3,4,5,6,7,8,9,10]

i = 0
while i<len(a):
    b = [a[i]]
    for j in range(len(a)):
        if a[j] % a[i] != 0:
            b.append(a[j])
    a = b
    i += 1
    
b = []
i = len(a)-1
while not(i<0):
    b.append(a[i])
    i -=1
print(b)
    



    

