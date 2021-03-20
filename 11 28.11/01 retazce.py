def pocet_a(ret):
    poc=0
    for i in range(len(ret)):
        if ret[i]=='a':
            poc+=1
    return poc
def vyskyt_znaku(zn,ret):
    for i in range(len(ret)):
        if ret[i]==zn:
            return i
    else:
        return -1

def maxpocet_a(zoz):
    max_poz=0
    for i in range(len(zoz)):
        if pocet_a(zoz[i])>pocet_a(zoz[max_poz]):
            max_poz=i
    return zoz[max_poz]
def vyskyt_a(zoz):
    for i in range(len(zoz)):
        if pocet_a(zoz[i])>0:
            return zoz[i]
    else:
        return 0

list=['ahoj','pes','aaa','mama']
print(pocet_a(list[2]))
print(vyskyt_znaku('m',list[3]))
print(maxpocet_a(list))
print(vyskyt_a(list))
