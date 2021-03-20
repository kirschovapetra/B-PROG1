#od najvacsieho po najmensie
print('napis a')
a = int(input())
print('napis b')
b = int(input())
if (a<b):
    a,b = b,a
print('a = ',a,'b = ',b)

#rotacia 3 cisel
print('zadaj a')
a = int(input())
print('zadaj b')
b = int(input())
print('zadaj c')
c = int(input())

a,b = b,a
a,c = c,a
b,c = c,b
print(a,b,c)

#max a min
print('zadaj a')
a = int(input())
print('zadaj b')
b = int(input())
print('zadaj c')
c = int(input())

print(a,b,c)
max = 0
if (b>max):
    max = b
elif (c>max):
    max = c
else:
    max = a
print(max)

min = max
if (b<min):
    min = b
elif (c<min):
    min = c
else:
    min = a
print(min)

#abc sort1
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

#abc sort2
'''a = 7
b = 3
c = 6

if (a>b):
    a,b = b,a
if (a>c):
    a,c = c,a
if (b>c):
    b,c = c,b
  
print(a,b,c)'''
