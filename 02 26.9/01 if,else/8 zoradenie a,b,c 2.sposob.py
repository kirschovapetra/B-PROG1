a = 5
b = 2
c = 3

if (a>b):
    a,b = b,a
if (c>b):
    print(a,b,c)
elif (c<a):
    print(c,a,b)    
else:
    print(a,c,b)
