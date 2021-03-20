def gr(a,n,q):
    G=[]
    for i in range(n):
        sum=0
        for j in range(i+1):
            sum+=a*q**j
        G.append(sum)
    return G

if q>-1 and q<1:
    print()
