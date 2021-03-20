a = int(input('zadaj a'))
b = int(input('zadaj b'))
if (a<b):
    a,b = b,a

c = a-b
while c>0:
    a = c
    if (a<b):
        a,b = b,a
    c = a-b
print(a)
    
    
    
