import random
def gensachovnicu(n):
    list = []
    for i in range(n):
        L = []
        for j in range(n):
            L.append('_')
        list.append(L)

    for i in range(1,n-1):
        list[(n-1)//2][i]='D'
        list[i][(n-1)//2]='D'
    list[(n-1)//2][(n-1)//2]='X'

    for i in range(n//3,n-n//3):
        list[0][i]='*'
        list[n-1][i]='*'
        list[i][0]='*'
        list[i][n-1]='*'

    for i in range(1,n//3+1):
        list[n//3][i]='*'
        list[n-n//3-1][i]='*'
        list[i][n//3]='*'
        list[i][n-n//3-1]='*'

    for i in range(n-n//3-1,n):
        list[n//3][i]='*'
        list[n-n//3-1][i]='*'
        list[i][n//3]='*'
        list[i][n-n//3-1]='*'

    for i in range(n):
        for j in range(n):
            print(list[i][j], end=' ')
        print()
        
gensachovnicu(int(input('zadaj velkost hracieho pola ')))

kocka = random.randint(1,6)
poz_A = 






























