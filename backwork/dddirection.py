from math import*
from backwork.direction import*
def avixyz(a,d,v):
    x=cos(v)*cos(d)*a
    y=cos(v)*sin(d)*a
    z=sin(v)*a
    return(x,y,z)
def ddis(a,b,c,x,y,z):
    x1=x-a
    y1=y-b
    z1=z-c
    o=sqrt(y1**2+x1**2)
    n=sqrt(o**2+z1**2)
    return(n)
def ddir(a,b,c,d,v,x,y,z):
    x1=x-a
    y1=y-b
    z1=z-c
    L=0
    V=0
    o=sqrt(y1**2+x1**2)
    if x1>0:
        if y1>=0:
            L=atan(y1/x1)
        else:
            L=atan(y1/x1)
    elif x1<0:
        if y1>=0:
            L=atan(y1/x1)+pi
        else:
            L=atan(y1/x1)+pi
    else:
        if y1<0:
            L=-pi/2
        else:
            L=pi/2
    D=rot(-d,L)
    if o>0:
        if z1>=0:
            V=atan(z1/o)
        else:
            V=atan(z1/o)
    elif o<0:
        if z>=0:
            V=atan(z1/o)+pi
        else:
            V=atan(z1/o)+pi
    else:
        if z1<0:
            V=-pi/2
        else:
            V=pi/2
    V=rot(-v,V)
    return D,V
def dlim(x,x1,y,y1,z,z1,a,b,c,d,v):
    if b<y or b>y1:
        d=-d
    if a<x:
        d=-d-pi
    if a>x1:
        d=-d+pi
    if c<z or c>z1:
        v=-v
    return(d)
def limxyz(a,b,c,x,x1,y,y1,z,z1):
    while a<x:
        a=x+5
    while a>x1:
        a=x1-5
    while b<y:
        b=y+5
    while b>y1:
        b=y1-5
    while c<z:
        b=y+5
    while c>z1:
        b=y1-5
    return a,b
