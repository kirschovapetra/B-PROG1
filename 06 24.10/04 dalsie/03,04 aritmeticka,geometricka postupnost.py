def aritm_p(zaciatok,d,n):
    a = [zaciatok]
    for i in range(0,n-1):
        a.append(a[i]+d)
    print('aritm_p',a)
aritm_p(2,3,10)

def geo_p(zaciatok,q,n):
    b = [zaciatok]
    for i in range(0,n-1):
        b.append(b[i]*q)
    print('geo_p',b)
geo_p(2,3,10)
