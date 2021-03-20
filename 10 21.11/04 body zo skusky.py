import random
def rand_ret(velkost):
    ret = ''
    for i in range(velkost):
        ret += chr(random.randint(ord('a'),ord('z')))
    return ret
f = open('data2.txt','r+')
n = int(input('zadaj pocet riadkov'))
for i in range(n):
    f.write(rand_ret(2)+' '+str(random.randint(0,100)))
    f.write('\n')
f.close()
