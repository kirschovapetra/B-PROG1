#2 1^3+2^3+...+n^3
print('zadaj n')
n = int(input())
vysledok = 0
for i in range(1,n+1):
    vysledok = vysledok + (i)**3
print(vysledok)


# vypis S stvorcov so stranou mensou ako n
print('zadaj n')
n = int(input())
i = 1
while((i*i)<n):
    print(i*i)
    i = i+1

# suma kladnych cisel
suma = 0
n = int(input('zadaj n'))
while(n>0):   
    suma = suma+n
    n = int(input('zadaj n'))
print(suma)

#a^b
a = int(input('zadaj a'))
b = int(input('zadaj b'))
mocnina = 1
for i in range(b):
    mocnina = mocnina*a
print(mocnina)

# sum = 1 + 1/2 + 1/4 + 1/8 + .... + 1/(2^100)
sum = 0
for i in range(101):
    sum = sum+1/(2**i)
print(sum)

# sum = 1 + 1/2 + 1/4 + 1/8 + .... + 1/(2^100) medzisucty
sum = 0
for i in range(100):
    sum = sum+1/(2**i)
    print(sum)

# sum = 1 + 1/2 + 1/4 + 1/8 + .... + 1/(2^100) ak nemenna hodnota tak stop
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

#zistit ci je cislo prvocislo
print('zadaj cislo')
n = int(input())

for i in range(2,n):
    if n % i == 0:
        print(n,'nie je prvocislo')
        break
else:
    print(n,'je prvocislo')

if n = 1:
    print(n,'nie je prvocislo')

#binarny rozvoj
    n = 10
ret = ''
while n>0:
    zv = n %2
    n = n//2
    ret = str(zv)+ret
print(ret)
#ciferny sucet
print('zadaj n')
n = input()
sum = 0
for i in range(len(n)):
    sum = sum + int(n[i])
print(sum)
#rovnica x2 + 2 = x3 + 2*x + 1
x = 0
while not(x**2+2-x**3-2*x-1 == 0):
    x = x + 0.001
print(x)
