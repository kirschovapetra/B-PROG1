a = [0,2,-1,4,6,3,11,-2,4]

for i in range(1,len(a)):
    tmp = a[i]
    k = i
    while k>0 and tmp<a[k-1]:
        a[k]=a[k-1]
        k-=1
    a[k] = tmp
print(a)
