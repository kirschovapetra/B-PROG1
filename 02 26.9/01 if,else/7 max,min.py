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
