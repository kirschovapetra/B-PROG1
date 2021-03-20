def f(s):
    s=s.split(' ')
    max,min,poz,ap,sum=0,0,0,0,0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if len(s[i])>max:
                max=len(s[i])
                poz=i
        sum+=len(s[i])
    ap=sum/len(s)
    return (ap,max,s[poz])

print(f('a ab abc'))
            

