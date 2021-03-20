def test_prvociselnosti(a):
    for d in range(2,a):
        if (a%d==0):
            return False
    else:
        return True
for i in range(2,50):
    if test_prvociselnosti(i)==True:
        print(i)
