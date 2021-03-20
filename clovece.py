#PETRA KIRSCHOVÁ
'''
vysvetlivky:
- sachovnica = matica 11x11 kt. predstavuje hraciu plochu 
- suradnice_hviezd = zoznam dvojic(suradnic) na ktorych sa nachadzaju '*' 
- suradnice_poradie =ku kazdej polozke zoznamu suradnice_hviezd priradene poradove cislo = dictionary {(x,y):poradove cislo},
zacina na pozicii hraca B a pokracuje v smere hodinovych ruciciek 
- funguje pre hracie pole 11x11 
'''
import random

def gensachovnicu(n,m_A,m_B,X_A,Y_A,X_B,Y_B): #X_A,Y_A = zoznamy x-ových a y-ových suradnic figurok hraca A(to iste X_B, Y_B pre hraca B)
    list = []                                 #n = velkost pola, m_A,m_B = pocet figurok hracov A,B v poli
#prazdne pole nxn
    for i in range(n):
        L = []
        for j in range(n):
            L.append(' ')
        list.append(L)
#vnutorny kriz - domceky a x v strede 
    for i in range(1,n-1):
        list[(n-1)//2][i]='D'
        list[i][(n-1)//2]='D'
    list[(n-1)//2][(n-1)//2]='X'
#hviezdicky
    for i in range((n+1)//3,(n+1)//2+1): #trojica '* * *' hore,dole,na bokoch
        list[0][i]='*'
        list[n-1][i]='*'
        list[i][0]='*'
        list[i][n-1]='*'
    for i in range(1,(n+1)//3+1): #prva polovica kriza
        list[(n+1)//2][i]='*'
        list[(n+1)//3][i]='*'
        list[i][(n+1)//3]='*'
        list[i][(n+1)//2]='*'

    for i in range((n+1)//2,n-1): #druha polovica kriza-vykresli zvysok hviezdiciek
        list[(n+1)//3][i]='*'
        list[(n+1)//2][i]='*'
        list[i][(n+1)//2]='*'
        list[i][(n+1)//3]='*'
        
    for i in range(m_A): #aby mi oznacovalo figurky poradovym cislom 0,1,2,3
        list[X_A[i]][Y_A[i]]='A'+str(i)

    for i in range(m_B):
        list[X_B[i]][Y_B[i]]='B'+str(i)
            
    return list

def vypis(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if len(list[i][j])==2: 
                print(list[i][j],end='')
            else:
                print(list[i][j],end=' ')
        print()
  
def gensuradnice_hviezd(n,pole): #vlozenie suradnic 'l=(i,j)' vsetkych hviezdiciek do zoznamu 'list'
    list = []
    #od vychodzej pozicie hraca B (0,6) az po suradnice (5,10)
    for i in range((n+1)//2):
        l = ()
        for j in range((n+1)//2,n):
            if pole[i][j] in {'*','A0','A1','A2','A3','B0','B1','B2','B3'}:
                l = (i,j)
                list.append(l)
    # od suradnic (6,10) po (10,5)            
    for i in range((n+1)//2,n):
        l = ()
        for j in range(n-1,(n-1)//2-1,-1):
            if pole[i][j] in {'*','A0','A1','A2','A3','B0','B1','B2','B3'}:
                l = (i,j)
                list.append(l)
    # od (10,4) po (5,0)         
    for i in range(n-1,(n-1)//2-1,-1):
        l = ()
        for j in range((n+1)//3,-1,-1):
            if pole[i][j] in {'*','A0','A1','A2','A3','B0','B1','B2','B3'}:
                l = (i,j)
                list.append(l)
    # od (4,0) po (0,5)          
    for i in range((n+1)//3,-1,-1):
        l = ()
        for j in range((n+1)//2):
            if pole[i][j] in {'*','A0','A1','A2','A3','B0','B1','B2','B3'}:
                l = (i,j)
                list.append(l)
    return list


def gensuradnice_domcek(n0,n,pole): #to iste ako pre gensuradnice_hviezd
    list = []
    for i in range(n0,n):
        l = ()
        for j in range(n0,n):
            if pole[(n-1)//2][j]=='D':
                l = ((n-1)//2,j)
                list.append(l)
    return list

def gensuradnice_poradie(list): #ku kazdej polozke(suradniciam) v zozname je priradene poradove cislo 
    dict = {}
    for i in range(len(list)):
        dict[list[i]] = i
    return dict

def Stlacil_znak(z,a):
    if a==z:  
        return True
    else:
        return False

def A_ma_figurky(list): #zistujem,ci ma hrac figurky v poli, neratam tie co maju poziciu>59 - su v domceku
    for i in range(len(list)):
        if list[i]<=59: 
            return True
    else:
        return False

def B_ma_figurky(list):
    for i in range(len(list)):
        if list[i]<=39:
            return True
    else:
        return False
        
def vyhral_A(list): #hrac vyhral, ked su vsetky miesta v domceku obsadene
    for i in range(6,10):
        if (list[i][5] =='D'):
            return False
    else:
        return True

def vyhral_B(list):
    for i in range(1,5):
        if (list[i][5] =='D'):
            return False
    else:
        return True
'''__________________________________________________________koniec funkcii_________________________________________________________________'''


c = int(input('zadajte velkost hracej plochy (11) '))

#vychodzia pozicia hraca A a B v sachovnici
#Ax,Ay,Bx,By beriem ako zoznamy x-ovych a y-ovych suradnic figurok hracov, na zaciatku ma kazdy len 1 figurku tak su to jednoprvkove zoznamy 
Ax=[c-1]
Ay=[(c+1)//3]
Bx=[0]
By=[(c+1)//2]

#pocet_A,pocet_B udava pocet figuriek A,B v poli 
pocet_A= 1
pocet_B= 1

sachovnica = gensachovnicu(c,pocet_A,pocet_B,Ax,Ay,Bx,By)
vypis(sachovnica)

suradnice_hviezd = gensuradnice_hviezd(c,sachovnica)
suradnice_poradie = gensuradnice_poradie(suradnice_hviezd)

#B_poz a A_poz su zoznamy pozicii figurok hracov,na zaciatku len 1 figurka - 1 pozicia 
B_poz = [0]
A_poz = [20]

#premenne 'a' a 'b' udavaju s ktorou figurkou budem hrat, na zaciatku mam len nultu figurku
a = 0
b = 0

while not (vyhral_A(sachovnica) or vyhral_B(sachovnica)): 
#hadze B
    if B_ma_figurky(B_poz)==False: #ked nema figurky v poli, hadze 3-krat
        print('Hrac B, hadzete 3krat ')
        for i in range(3): 
            print('Pre hod kockou stlacte k ')
            if Stlacil_znak('k',input())==True:
                kocka = random.randint(1,6)
                print('hodili ste',kocka)
                if (kocka==6): #nastavim novu figurku na vychodziu poziciu 
                    B_poz.append(0) 
                    Bx.append('')
                    By.append('')
                    b=-1
                    Bx[b],By[b] = suradnice_hviezd[B_poz[b]]
                    break
                else:
                    print('Skuste znovu ')
                    b='' #toto sem pridavam preto, aby program preskocil hned na tah hraca A a neriesilo sa s ktorou figurkou bude hrac B hrat
            else: #ak hrac stlaci zly znak
                print('Stlacili ste nespravny znak')
                continue
                    
    else: #ked ma figurky v poli, hadze normalne
        t = input('hrac B - s ktorou figurkou chcete v tomto kole hrat? (zadajte 0/1/2/3) ')
        if t.isdigit()==False or int(t)>len(B_poz): #ak hrac stlaci zly znak
            print('Stlacili ste nespravny znak')
            continue
        else:
            b=int(t)
        print('Na rade je hrac B, pre hod kockou stlacte k ')
        if Stlacil_znak('k',input())==True: # hod kockou
            kocka1 = random.randint(1,6)
            print('hodili ste',kocka1)
            B_poz[b] += kocka1
            kocka2 = 0
            if (kocka1==6): 
                print('Na rade je hrac B')
                print('Pre hod kockou stlacte k, pre nastavenie novej figurky stlacte lubovolny znak ')
                if Stlacil_znak('k',input())==True: #posun hraca
                    kocka2 = random.randint(1,6)
                    print('hodili ste',kocka1,'+',kocka2,'=',kocka1+kocka2)
                    B_poz[b] += kocka2
                else: #nastavenie novej figurky - prida sa nova figurka, jej pozicia je 0
                    B_poz[b]-=6
                    B_poz.append(0)
                    Bx.append('')
                    By.append('')
                    Bx[-1],By[-1] = suradnice_hviezd[B_poz[-1]]
        else: 
            print('stlacili ste nespravny znak')
            continue
                    
    if b!='': #toto program preskakuje ked hrac nema figurky a nehodi 6-ku
        if len(B_poz)>0:
            if (B_poz[b] in A_poz) and A_poz[A_poz.index(B_poz[b])]<=59: #vyhodenie figurky - ked sa pozicia figurky B nachadza medzi poziciami figurok A tak A vypadava
                Ax.pop(A_poz.index(B_poz[b]))
                Ay.pop(A_poz.index(B_poz[b]))
                A_poz.remove(B_poz[b])
                pocet_A=len(A_poz)
                print('Hrac A vypadava')
#hrac A sa pohybuje po posunutom poli - nie od 0 po 39 ale od 20 po 59, preto pridavam tuto podmienku:                
            if ((B_poz[b]+40) in A_poz) and A_poz[A_poz.index(B_poz[b]+40)]<=59: 
                Ax.pop(A_poz.index(B_poz[b]+40))
                Ay.pop(A_poz.index(B_poz[b]+40))
                A_poz.remove(B_poz[b]+40)
                pocet_A=len(A_poz)
                print('Hrac A vypadava')
        
        if B_poz[b]>39: #ked sa dostane na koniec pola hviezdiciek
            suradnice_domcek = gensuradnice_domcek(0,(c-1)//2,sachovnica) #k suradniciam hviezdiciek pripojim suradnice domceka hraca B
            suradnice_hviezd.extend(suradnice_domcek)
            suradnice_poradie = gensuradnice_poradie(suradnice_hviezd)
            if B_poz[b]>43: #nezmesti sa do domceka
                B_poz[b]=B_poz[b]-kocka1-kocka2
                print('skuste znovu v dalsom tahu')
            else: #zmesti sa ale na policku uz ma figurku
                if sachovnica[B_poz[b]-39][5] in {'B0','B1','B2','B3'}:
                    B_poz[b]=B_poz[b]-kocka1-kocka2
                    print('skuste znovu v dalsom tahu')
                else:
                    Bx[b] = B_poz[b]-39
                    By[b] = 5
                    sachovnica = gensachovnicu(c,pocet_A,pocet_B,Ax,Ay,Bx,By)
        else:
            Bx[b],By[b] = suradnice_hviezd[B_poz[b]]
            
            
        pocet_B = len(B_poz)        
        sachovnica = gensachovnicu(c,pocet_A,pocet_B,Ax,Ay,Bx,By)
        vypis(sachovnica)
        
        if vyhral_B(sachovnica)==True:
            break
    
#hadze A, kod v podstate podobny ako pre B
    if A_ma_figurky(A_poz)==False: 
        print('Hrac A, hadzete 3krat ')
        for i in range(3): 
            print('Pre hod kockou stlacte k ')
            if Stlacil_znak('k',input())==True:
                kocka = random.randint(1,6)
                print('hodili ste',kocka)
                if (kocka==6):
                    A_poz.append(20)
                    Ax.append('')
                    Ay.append('')
                    a=-1
                    Ax[a],Ay[a] = suradnice_hviezd[A_poz[a]]
                    break
                else:
                    print('Skuste znovu ')
                    a=''
            else: 
                print('stlacili ste nespravny znak')
                continue
                    
    else:
        t = input('hrac A - s ktorou figurkou chcete v tomto kole hrat? (zadajte 0/1/2/3) ')
        if t.isdigit()==False or int(t)>len(A_poz):
            print('Stlacili ste nespravny znak')
            continue
        else:
            a=int(t)
        print('Na rade je hrac A, pre hod kockou stlacte k ')
        if Stlacil_znak('k',input())==True:
            kocka1 = random.randint(1,6)
            print('hodili ste',kocka1)
            A_poz[a] += kocka1
            kocka2=0
            if (kocka1==6):
                print('Na rade je hrac A')
                print('Pre hod kockou stlacte k, pre nastavenie novej figurky stlacte lubovolny znak')
                if Stlacil_znak('k',input())==True:
                    kocka2 = random.randint(1,6)
                    print('hodili ste',kocka1,'+',kocka2,'=',kocka1+kocka2)
                    A_poz[a] += kocka2
                else:
                    A_poz[a]-=6
                    A_poz.append(20)
                    Ax.append('')
                    Ay.append('')
                    Ax[-1],Ay[-1] = suradnice_hviezd[A_poz[-1]]
        else: 
            print('stlacili ste nespravny znak')
            continue

    if a!='':
        if len(A_poz)>0:
            if (A_poz[a]in B_poz) and B_poz[B_poz.index(A_poz[a])]<=39:
                Bx.pop(B_poz.index(A_poz[a]))
                By.pop(B_poz.index(A_poz[a]))
                B_poz.remove(A_poz[a])
                pocet_B=len(B_poz)
                print('Hrac B vypadava')
                
            if (A_poz[a]-40 in B_poz) and B_poz[B_poz.index(A_poz[a]-40)]<=39:
                Bx.pop(B_poz.index(A_poz[a]-40))
                By.pop(B_poz.index(A_poz[a]-40))
                B_poz.remove(A_poz[a]-40)
                pocet_B=len(B_poz)
                print('Hrac B vypadava')
                
        if A_poz[a]>59:    
            if A_poz[a]>63:
                A_poz[a]=A_poz[a]-kocka1-kocka2 
                print('skuste znovu v dalsom tahu')
            else:
                if sachovnica[c-1-(A_poz[a]-59)][5] in {'A0','A1','A2','A3'}:
                    A_poz[a]=A_poz[a]-kocka1-kocka2
                    print('skuste znovu v dalsom tahu')
                else:
                    Ax[a] = c-1-(A_poz[a]-59)
                    Ay[a] = 5
                    sachovnica = gensachovnicu(c,pocet_A,pocet_B,Ax,Ay,Bx,By)
        elif A_poz[a]>39: #ked prejde hrac A cez poziciu 0(pre neho je to pozicia 40) tak sa zacina indexovat od nuly
            Ax[a],Ay[a] = suradnice_hviezd[A_poz[a]-40]     
        else:
            Ax[a],Ay[a] = suradnice_hviezd[A_poz[a]]
                
        pocet_A = len(A_poz)
        sachovnica = gensachovnicu(c,pocet_A,pocet_B,Ax,Ay,Bx,By)
        vypis(sachovnica)

if vyhral_B(sachovnica):
    print('Gratulujem, vitazom sa stava hrac B!!! :) ')
else:
    print('Gratulujem, vitazom sa stava hrac A!!! :) ')




