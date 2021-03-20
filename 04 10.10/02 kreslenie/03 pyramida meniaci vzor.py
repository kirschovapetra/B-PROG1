n = 3
m = 10

for j in range(n):
    s = ''
    for i in range(m,m+1+2*j):
        s = s +str(i%10)
    print(((n-(j+1))*(' ')),s,sep = '')
        

