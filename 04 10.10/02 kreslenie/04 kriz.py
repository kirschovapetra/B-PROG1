n=5
m=2
s=''
for i in range(n,m,-1):
    s=s+str(i)
for i in range(m,n+1):
    s=s+str(i)
for i in range((len(s)+1)//2-1):
    print((n-m)*' '+s[i])
print(s)
for i in range((len(s)+1)//2,len(s)):
    print((n-m)*' '+s[i])

    

