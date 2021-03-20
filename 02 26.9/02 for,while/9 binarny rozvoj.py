n = 10
ret = ''
while n>0:
    zv = n %2
    n = n//2
    ret = str(zv)+ret
print(ret)
