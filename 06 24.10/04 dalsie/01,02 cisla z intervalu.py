def f(od,do,step):
    if (step<0):
        od,do = do,od
    for i in range(od,do,step):
        print(i)
f(2,20,-3)
