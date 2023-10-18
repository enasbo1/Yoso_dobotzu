from backwork.dddirection import*

def create_dobo(): # renvois les coordonées de 115 points formant une sphère creuse
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

def create_rond(r): # renvois les coordonées points appartenant à un plan horiontal et formant un cercle plein de rayon r
    n=0
    for a in range(r):
        perimetre = int((a+1)*pi)
        n+=perimetre
    cercle = [[]for i in range(n)]
    n=0
    for a in range(r):
        perimetre = int((a+1)*pi)
        for i in range(perimetre):
            d = (i/perimetre)*(2*pi)
            X=avix(a+1,d)
            Y=aviy(a+1,d)
            cercle[n]=[X,Y,0]
            n+=1
    return(cercle)

def create_cercle(r): # renvois les coordonées de ~r*3 points formant une sphère creuse de rayons r
    n=0
    perimetre = int(r*pi)
    cercle = [[]for i in range(perimetre)]
    for i in range(perimetre):
        d = (i/perimetre)*(2*pi)
        X=avix(r,d)
        Y=aviy(r,d)
        cercle[n]=[X,Y,0]
        n+=1
    return(cercle)

def create_trais(t,d,v,x0,y0,z0): # renvois les coordonées de t points appartenant à une droite orientée en direction sphérique d,v et passant par x0, y0, z0  et formant un segment de longueure t
    trai = [[]for i in range(t)]
    for i in range(t):
        x1, y1, z1 = avixyz(i,d,v)
        trai[i] = [x1+x0,y1+y0,z1+z0]
    return(trai)

def create_aile(angle,ditec): # renvois les coordonées de points appartenant à une un plan orienté en direction sphérique 0,direc et formant unune aile plus ou moins déployé en fontion de angle
    x0,y0,z0=0,0,0
    direc=cos(ditec)
    dires=sin(ditec)
    ang=sin(angle)
    D=asin(direc*ang)
    V=asin(dires*ang)
    aile = create_trais(3,D,V,x0,y0,z0)
    x1,y1,z1 = avixyz(3,D,V)
    x0=x0+x1
    y0=y0+y1-0.5
    z0=z0+z1
    ang=sin(-angle*1.5)
    D=asin(direc*ang)
    V=asin(dires*ang)
    aile = aile+create_trais(7,D,V,x0,y0,z0)
    x1,y1,z1 = avixyz(5,D,V)
    x0=x0+x1
    y0=y0+y1-0.5
    z0=z0+z1
    d0=(-angle*1.5)+pi
    d1=angle-d0
    for i in range(5):
        ang=sin(rot(d0,(i*d1)/4))
        D=asin(direc*ang)
        V=asin(dires*ang)
        aile = aile+create_trais(int(3+i),D,V,x0,y0,z0)
    return(aile)

def create_epee(pointed, pointev, tranchant): # renvois les coordonées de points appartenant à une un plan auquel apartient une droite orientée en direction sphérique pointed,pointev et formant une épée orienté en fontion de tranchant
    x0,y0,z0=0,0,0
    x1,y1,z1 = avixyz(-3,pointed,pointev)
    aile=create_trais(4,pointed,pointev,x1,y1,z1)
    for i in range(4):
        X = ((i%2)/2)+x1-0.25
        Y = ((i//2)/2)+y1-0.25
        Z = z1
        aile = aile+[[X,Y,Z]]
    for i in range(2):
        X = x1
        Y = y1
        Z = ((i%2)/2)+z1-0.25
        aile = aile+[[X,Y,Z]]
    x1,y1,z1 = avixyz(1,pointed,pointev)
    x0=x0+x1
    y0=y0+y1
    z0=z0+z1
    direc=cos(tranchant)
    dires=sin(tranchant)
    x = -direc*sin(pointev)*sin(pointed)+dires*sin(pointed)
    y = -direc*sin(pointev)*cos(pointed)-dires*cos(pointed)
    z = direc*cos(pointev)
    D, V = ddir(0,0,0,0,0,x,y,z)
    x1,y1,z1 = avixyz(-3,D,V)
    aile = aile+create_trais(7 ,D,V,x0+x1,y0+y1,z0+z1)
    for i in range(3):
        x1,y1,z1 = avixyz(i,D,V)
        aile = aile+create_trais(9-(i*2),pointed,pointev,x1+x0,y1+y0,z1+z0)
    for i in range(2):
        x1,y1,z1 = avixyz(-i-1, D, V)
        aile = aile+create_trais(10,pointed,pointev,x1+x0,y1+y0,z1+z0)
    return(aile)


def create_queu1(D, V): # renvois les coordonées de points appartenant à une un plan vertical orienté en D et formant une queu en forme d'éclair plus ou moins déployé en fonction de V
    x0,y0,z0=0,0,0
    aile=[[0,0,0]]
    for i in range(2):
        aile = create_trais(3,D,V,x0,y0,z0+i)
    x1,y1,z1 = avixyz(3,D,V)
    x0=x0+x1
    y0=y0+y1
    z0=z0+z1
    for i in range(3):
        aile = aile+create_trais(2,D,-V,x0,y0,z0+i)
    x1,y1,z1 = avixyz(2,D,-V)
    x0=x0+x1
    y0=y0+y1
    z0=z0+z1
    for i in range(4):
        aile = aile+create_trais(7,D,V,x0,y0,z0+i)
    return(aile)

def create_queu2(D, monte): # renvois les coordonées de points appartenant à une un plan vertical orienté en D et formant une queu d'une forme normale(c'est la queu du dobo de feux) plus ou moins déployé en fonction de 'monte'
    x0,y0,z0=0,0,0
    aile=[[0,0,0]]
    v=monte/5
    V=0
    aile = create_trais(1,D,V,x0,y0,z0)
    for a in range(5):
        V=rot(v,V)
        for i in range(4):
            aile = aile+create_trais(2,D,-V,x0,y0,z0)
        x1,y1,z1 = avixyz(2,D,V)
        x0=x0+x1
        y0=y0+y1
        z0=z0+z1
    return(aile)
