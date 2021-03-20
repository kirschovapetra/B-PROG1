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

