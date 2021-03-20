n=5
M=[]
for i in range(n):
    m=[]
    for j in range(n):
        m.append('.')
    M.append(m)

for i in range(n):
    M[i][i]='x'
    M[i][n-1-i]='x'


for i in range(n):
    for j in range(n):
        print(M[i][j],end=' ')
    print('\n')
