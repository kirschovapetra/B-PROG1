def F1(prvok,s1):
    for i in s1:
        if prvok==i:
            return True
    else:
        return False

m1 = {'a','b',2,3,'c'}
m2 = {'a','c',9}
n = 9
print(n,'sa nachadza',F1(n,m1))


def F2(s1,s2):
    s = set()
    for i in s1:
        if F1(i,s2)==True:
            s.add(i)
    return s

print('prienik',F2(m1,m2))

def F3(s1,s2):
    s = set()
    for i in s1:
        if F1(i,s2)==False:
            s.add(i)
    return s

print('rozdiel m1-m2',F3(m1,m2))

def F4(s1,s2):
    s = set()
    for i in s1:
        for j in s2:
            s.add(i)
            s.add(j)
    return s



print('zjednotenie',F3(m1,m2))
