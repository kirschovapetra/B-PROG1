def gr(a,n,q):
    G=[]
    for i in range(n):
        sum=0
        for j in range(i+1):
            sum+=a*q**j
        G.append(sum)
    return G
print(gr(1,5,2))
