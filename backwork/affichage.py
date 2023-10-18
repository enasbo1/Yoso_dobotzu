from backwork.dddirection import*
from backwork.formes import*
def create_nuage(L,r,dmur): # renvois les coordonées de L*l point appartenant à un plan horiontal et formant un rectangle plein de L par l 
    mur=[]
    l=-L
    R=-r
    H=0
    for i in range(int(r)):
        for a in range(int(L)):
            Z=0
            X=avix(l,dmur)+avix(R,dmur+pi/2)
            Y=aviy(l,dmur)+aviy(R,dmur+pi/2)
            mur.append([X,Y,Z])
            l+=1
        R-=1
        l=-L
    return(mur)

def create_cible(toile, x,y):
    return(toile.create_rectangle(x-15,y-1,x-5,y+1),toile.create_rectangle(x+15,y-1,x+5,y+1),toile.create_rectangle(x-1,y-15,x+1,y-5),toile.create_rectangle(x-1,y+15,x+1,y+5))

def deplace(toile, cible, x, y):
    toile.coords(cible[0],x-15,y-1,x-5,y+1)
    toile.coords(cible[1],x+15,y-1,x+5,y+1)
    toile.coords(cible[2],x-1,y-15,x+1,y-5)
    toile.coords(cible[3],x-1,y+15,x+1,y+5)


def per_point(x,y,xcam,ycam,zcam,dcam,vcam,xpoint,ypoint,zpoint): # comme expliqué plusieurs fois dean sujet, c'est la fontion qui progete les poins en coordonées xpoint, ypoint et zpoint, en déduit leurs coordonées sphériques (sur un cercle de rayon 1 et de coordonées xcam, ycam et zcam) et les progete sur le plan tangeant en dcam, vcam (coordonées sphériques) et renvoi les coordonées obtenue dans un repert orthonormé ((dcam,vcam),xi,xj). 
    D,V=ddir(xcam,ycam,zcam,dcam,0,xpoint,ypoint,zpoint)
    dv=rot(-vcam, V)
    if -pi/2<D<pi/2 and -pi/2<V<pi/2:
        B=tan(dv)
        A=tan(D)*sqrt((tan(dv)**2)+1)
        A=x/2+(A*x)
        B=y/2+(B*x)
    else:
        A, B=2*x, 2*x
    return[A,B]
