text = 'ABCD'
def f(n,t):
    m = set()
    for i in range(len(t)):
       if ord(t[i])<n:
           m.add(t[i])
    pocet = len(m)
    return pocet
print(f(68,text))
