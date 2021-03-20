def prvok_patri(prvok,s1):
    for i in s1:
        if prvok==i:
            return True
    else:
        return False

def niektory_znak(ret1,ret2):
    for i in set(ret1):
        if prvok_patri(i,set(ret2))==True:
            return 1
    else:
        return 0
def kazdy_znak(ret1,ret2):
    for i in set(ret1):
        if prvok_patri(i,set(ret2))==False:
            return 0
    else:
        return 1

def prienik_ret(ret1,ret2):
    s=set()
    for i in set(ret1):
        if prvok_patri(i,set(ret2))==True:
            s.add(i)
    return s

def viac(ret):
    pocet=0
    s=set()
    for i in range(len(ret)):
        for j in range(i+1,len(ret)):
            if ret[i]==ret[j]:
                pocet+=1
            if pocet>1:
                s.add(ret[i])
    return len(s)
r1='ahoj'
r2='mama'
r3='ahoj'
print(niektory_znak(r1,r2))
print(kazdy_znak(r1,r2))
print(kazdy_znak(r1,r3))
print(prienik_ret(r1,r2))
print(viac(r2))


