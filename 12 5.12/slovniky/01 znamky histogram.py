
def slovnik(zoz):
    dict={}
    lst=['A','B','C','D','E','FX']
    for i in lst:
        dict[i]=0
    for i in zoz:
        dict[i]+=1
    return dict

L=['FX', 'FX', 'E', 'FX', 'B', 'FX', 'E', 'E']
print(slovnik(L))

def histogram(d):
    for key in d:
        print(key,d[key]*'*')
histogram(slovnik(L))
