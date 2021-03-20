def pocet(x,y):
    n = int(input('zadaj cislo'))
    all = 0
    sum = 0
    max = 0
    min = n
    pocet_y = 0
    vacsie = 0
    while not n == x:
        all += 1
        sum += n
        if (n>x):
            vacsie += 1
        if (n<min):
            min = n
        if (n>max):
            max = n
        if n==y:
            pocet_y +=1
            je = True
        else:
            je = False
        n = int(input('zadaj cislo'))
    print('pocet',all,'ap',sum/all,'max',max,'min',min,'vacsie ako x',vacsie,'y patri',je,pocet_y,'krat')

pocet(2,3)



            

