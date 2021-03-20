L=[]
for i in range(1,11):
    l=[]
    for j in range(1,11):
        l.append(i*j)
    L.append(l)

for i in range(len(L)):
    for j in range(len(L[i])):
        print(L[i][j],end='  ')
    print('\n')
