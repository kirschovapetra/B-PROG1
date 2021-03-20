def bin_vyhl(lst,x):
    a = 0
    b = len(lst)-1
    while a!=b:
        stred = (a+b)//2
        if x<=lst[stred]:
            b = stred
        else:
            a = stred+1
    if lst[a]==x:
        return a
    else:
        return -1
        
print(bin_vyhl([1,2,3,4],2))
