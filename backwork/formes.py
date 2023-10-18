from backwork.create import*
from random import randint

def forme_dobo(arg): # 0 arg taille; 115
    dobo = [[]for i in range(115)]
    h=-5
    n=0
    for a in range(10):
        v=asin(h/5)
        r=cos(v)*5
        perimetre = int(r*pi)
        for i in range(perimetre):
            d = (i/perimetre)*(2*pi)
            if n==51 or n==64:
                X=avix(r+0.2,d)
                Y=aviy(r+0.2,d)
                C='black'
            else:
                X=avix(r,d)
                Y=aviy(r,d)
                C='grey'
            dobo[n]=[X,Y,h,C]
            n+=1
        h+=1
    return(dobo)

def forme_feux(arg): # 0 arg ;  115
    li=[[-6,0,2,'red']for i in range(115)]
    for i in range(20):
        li[i*5][3] = 'dark orange'
    _temp = create_queu2(pi,-2*pi/5)
    for i in range(len(_temp)):
        li[i][0] = _temp[i][0]-6+randint(-int(i/10),int(i/10))
        li[i][1] = _temp[i][1]+randint(-int(i/10),int(i/10))
        li[i][2] = _temp[i][2]+2+randint(-int(i/5),int(i/10))
    return li

def forme_eau(arg): #0 arg ; 115
    li=[[0,0,0,'Deepskyblue2']for i in range(115)]
    for i in range(20):
        li[i*5][3] = 'Deepskyblue3'
    _temp = create_rond(5)
    for i in range(len(_temp)):
        li[i][0] = _temp[i][0]-2
        li[i][1] = _temp[i][2]
        li[i][2] = _temp[i][1]-2
    return li

def forme_foudre(arg): #0 arg ; 115
    li=[[-6,0,1,'gold']for i in range(115)]
    for i in range(20):
        li[i*5][3] = 'gold4'
    _temp = create_queu1(pi,-2*pi/5)
    for i in range(len(_temp)):
        li[i][0] = _temp[i][0]-6
        li[i][1] = -_temp[i][1]
        li[i][2] = _temp[i][2]+1
    return li

def forme_boule_feux(arg): # 0 arg; 24
    aile=[[randint(-2,3),randint(-2,3),randint(-2,3),'red']for i in range(24)]
    for i, a in enumerate(aile):
        if i%5==0:
            a[3]='dark orange'
    return(aile)

def forme_fla_point(arg): # x arg, x
    li=[ar.split(')')for ar in arg]
    for a in range(len(arg)):
        if a%5==0:
            li[a]=li[a]+['dark orange']
        else:
            li[a]=li[a]+['red']
        for i in range(3):
            li[a][i]=float(li[a][i])
    return(li)

def forme_torche(arg): # 0 arg, 115
    li=[[0,0,0,'red']for i in range(115)]
    for i,qu in enumerate(li):
        X,Y,Z=avixyz(randint(1,10)+randint(1,10),
                     randint(-100,100)*pi/100,
                     randint(-100,100)*pi/100)
        qu[0]=X
        qu[1]=Y
        qu[2]=Z
        if i%5==0:
            qu[3]='dark orange'
    return li

def forme_brule(arg): # 0 arg, 115
    li=[[0,0,0,'red']for i in range(115)]
    for i,qu in enumerate(li):
        X,Y,Z=avixyz(6,
                     randint(-100,100)*pi/100,
                     (randint(-50,50)+randint(-50,50))*pi/100)
        qu[0]=X
        qu[1]=Y
        qu[2]=Z
        if i%5==0:
            qu[3]='dark orange'
        if randint(0,1)==1:
            qu[3]='grey'
    return li

def forme_aqua_point(arg): # x arg, x
    li=[ar.split(')')for ar in arg]
    for a in range(len(arg)):
        if a%5==0:
            li[a]=li[a]+['Deepskyblue3']
        else:
            li[a]=li[a]+['Deepskyblue2']
        if len(li[a])>3:
            for i in range(3):
                li[a][i]=float(li[a][i])
        else:
            print('erreur')
            print(li[a])
    return(li)

def forme_boule_eau(arg): # 0 arg; 24
    aile=[[randint(-2,3),randint(-2,3),randint(-2,3),'Deepskyblue2']for i in range(24)]
    for i, a in enumerate(aile):
        if i%5==0:
            a[3]='Deepskyblue3'
    return(aile)

def forme_dobeau(arg): # 0 arg taille; 115
    dobo = [[]for i in range(115)]
    h=-5
    n=0
    for a in range(10):
        v=asin(h/5)
        r=cos(v)*5
        perimetre = int(r*pi)
        for i in range(perimetre):
            d = (i/perimetre)*(2*pi)
            if n==51 or n==64:
                X=avix(r+0.2,d)
                Y=aviy(r+0.2,d)
                C='black'
            elif n%6==0:
                X=avix(r+0.1,d)
                Y=aviy(r+0.1,d)
                C='Deepskyblue2'
            else:
                X=avix(r,d)
                Y=aviy(r,d)
                C='grey'
            dobo[n]=[X,Y,h,C]
            n+=1
        h+=1
    return(dobo)


def forme_traine(arg): #1 arg: type ; taille=35
    ty = arg[0]
    ret=[[-6,0,1,'gold']for i in range(35)]
    x0, y0, z0 = 0, 0, 0
    for i, li in enumerate(ret):
        if i%5==0:
            li[3]='gold4'
        li[0] +=x0+randint(-10,10)
        li[1] -=y0+randint(-10,10)
        li[2] +=z0+randint(-10,10)
        if ty=='up':
            x1,y1,z1 = avixyz(60/35, 0, -pi/2)
            x0=x0+x1
            y0=y0+y1
            z0=z0+z1
        else:
            x1,y1,z1 = avixyz(80/35,0,0)
            x0=x0+x1
            y0=y0+y1
            z0=z0+z1
    return ret

def forme_tir_elec(arg): #0 arg ; taille=4
    ret=[[(i-1.5)/2,(i-1.5)/2,(i-1.5)/2,'gold']for i in range(4)]
    return ret

def forme_eclair(arg): #0 arg : taille = 35
    ret=[[-6,0,1,'gold']for i in range(35)]
    for i, li in enumerate(ret):
        if i%5==0:
            li[3]='gold4'
        x0,y0,z0 = avixyz(randint(10,80),randint(-20,20)*(pi/20),0)
        li[0]=  x0
        li[1]=  y0
        li[2]=  z0 + randint(-10,10)
    return ret

def forme_dobo_eclair(arg): #0arg : taille=115
    dobo = [[]for i in range(115)]
    h=-5
    n=0
    for a in range(10):
        v=asin(h/5)
        r=cos(v)*5
        perimetre = int(r*pi)
        for i in range(perimetre):
            d = (i/perimetre)*(2*pi)
            if n==51 or n==64:
                X=avix(r+0.2,d)
                Y=aviy(r+0.2,d)
                C='black'
            elif n%7==0:
                X=avix(r+0.1,d)
                Y=aviy(r+0.1,d)
                C='gold4'
            else:
                X=avix(r,d)
                Y=aviy(r,d)
                C='grey'
            dobo[n]=[X,Y,h,C]
            n+=1
        h+=1
    return(dobo)

def forme_none(arg): #0 arg; taille = 1
    return [[0,0,0,'white']]


def forme_terre(arg): #1 arg: color; taille = 115
    color=arg[0]
    ret = [[0,0,0,color]for i in range(115)]
    for i in range(8):
        ret[i][0]=i//2
        ret[i][1]=5+i%2
        ret[i][2]=(i//4)+1
    for i in range(8):
        ret[i+8][0]=i//2
        ret[i+8][1]= -(5+i%2)
        ret[i+8][2]=(i//4)+1
    _temp = create_cercle(5.5)
    for i in range(len(_temp)):
        ret[i+16][0]=_temp[i][0]
        ret[i+16][1]=_temp[i][1]
        ret[i+16][2]= -2
    return(ret)

def forme_terratape(arg): # 2 arg : color, tim ; taille = 33
    color, tim = arg
    ret=[[0,0,0,color]for i in range(115)]
    tim=float(tim)
    _temp = create_cercle(5.5)
    for i in range(len(_temp)):
        ret[i+16][0]=_temp[i][0]
        ret[i+16][1]=_temp[i][1]
        ret[i+16][2]= -2
    if tim<0.5:
        X = (tim*20)-((tim*4)**2)
        Y = 5-((tim*4)**2)
        Z = -(tim*4)**2
    elif tim<0.6:
        X = 6
        Y = 1
        Z = -4
    else:
        X = 6
        Y = 1
        Z = 7
    if tim<1:
        for i in range(8):
            ret[i][0]=(i//2)+X
            ret[i][1]=i%2+Y
            ret[i][2]=(i//4)+Z
            ret[i+8][0]=(i//2)+X
            ret[i+8][1]=i%2-Y
            ret[i+8][2]=(i//4)+Z
    return ret

def forme_terrazone(arg): # 0 arg ; taille= 82
    ret=[[0,0,0,'saddle brown']for i in range(82)]
    for y, p  in enumerate(ret):
        i=y+33
        _rand=-10+(i*27)%20
        p[0]=avix((i/11.5)**2,i*pi/2.5)+avix(_rand,(i*pi/2.5)+pi/2)
        p[1]=aviy((i/11.5)**2,i*pi/2.5)+aviy(_rand,(i*pi/2.5)+pi/2)
        p[2]=0
    return ret

def forme_terbaston(arg): #3arg: color, tim1, tim2
    color, tim1, tim2 = arg
    ret=[[0,0,0,color]for i in range(16)]
    tim1=float(tim1)
    tim2=float(tim2)
    if tim1<=0.5:
        for i in range(8):
            ret[i][0]=(i//2)+tim1*20
            ret[i][1]=5+i%2
            ret[i][2]=(i//4)+1
    elif tim1<1:
        for i in range(8):
            ret[i][0]=(i//2)+10-((tim1-0.5)*20)
            ret[i][1]=5+i%2
            ret[i][2]=(i//4)+1
    else:
        for i in range(8):
            ret[i][0]=(i//2)+10
            ret[i][1]=5+i%2
            ret[i][2]=(i//4)+1
    if tim2<=0.5:
        for i in range(8):
            ret[i+8][0]=(i//2)+tim2*20
            ret[i+8][1]=-(5+i%2)
            ret[i+8][2]=(i//4)+1
    elif tim2<1:
        for i in range(8):
            ret[i+8][0]=(i//2)+10-((tim2-0.5)*20)
            ret[i+8][1]=-(5+i%2)
            ret[i+8][2]=(i//4)+1
    else:
        for i in range(8):
            ret[i+8][0]=(i//2)+10
            ret[i+8][1]=-(5+i%2)
            ret[i+8][2]=(i//4)+1
    return ret
