def hviezdy(n):
    print(n*'*',end='')
def medzery(n):
    print(n*' ',end='')

k = 3
for i in range(k):
    for j in range(1,k+1):
        hviezdy(j)
        medzery(k-j)
    print('\n')
    
