from backwork.affichage import*
from tkinter import*
class Item:
    def __init__(self, x, y, z, color, nature,d):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.flui=3
        self.etat='solide'
        self.color = color
        if nature=="nuage":
            self.nuage(1,1,d)
        if nature=="magie":
            self.etat='liq'
    
    def syncro(self, item):
        self.x=item.x
        self.y=item.y
        self.z=item.z
        self.d=item.d

    def nuage(self,L,l,d):
        self.type = "nuage"
        self._temp = create_nuage(d,L,l)
        self.d = d
        self.pixels = [Pixel(self._temp[i][0], self._temp[i][1], self._temp[i][2], self.color, self) for i in range(len(self._temp))]
    
    def tour(self,FPS):
        if self.type == 'yoso':
            self.syncro(self.dobo)
    
    def dobotzu(self,d):
        self.v_z=0
        self.coo=[0,0,0,0]
        self.type = "dobo"
        self._temp = create_dobo()
        self.d = d
        self.pixels = [None for i in range(len(self._temp)+15)]
        for i in range(115):
            if i==51 or i==64:
                self.pixels[i]=Pixel(self._temp[i][0], self._temp[i][1], self._temp[i][2], 'black', self)
            else:
                self.pixels[i]=Pixel(self._temp[i][0], self._temp[i][1], self._temp[i][2], self.color, self)
        self._temp = create_cercle(5)
        for i in range(15):
            self.pixels[i+115] = Pixel(self._temp[i][0],self._temp[i][1],self.z*(-1),'red',self)
        self.yoso = Item(self.x, self.y, self.z,'white','magie',self.d)
        self.yoso.magie(self)

    def tetzu(self,d):
        self.v_z=0
        self.coo=[0,0,0,0]
        self.type = "dobo"
        self._temp = create_dobo()
        self.d = d
        self.pixels = [None for i in range(len(self._temp)+15)]
        for i in range(115):
            if i==51 or i==64:
                self.pixels[i]=Pixel(self._temp[i][0], self._temp[i][1], self._temp[i][2], 'black', self)
            else:
                self.pixels[i]=Pixel(self._temp[i][0], self._temp[i][1], self._temp[i][2], self.color, self)
        self._temp = create_cercle(5)
        for i in range(15):
            self.pixels[i+115] = Pixel(self._temp[i][0],self._temp[i][1],self.z*(-1),'red',self)
        self.yoso = Item(self.x, self.y, self.z,'white','magie',self.d)
        self.yoso.magie2(self)

    def magie(self, dobo):
        self.type = 'yoso'
        self.dobo = dobo
        self.pixels = [Pixel(0,0,0,self.color , self)for i in range(115)]

    def magie2(self, dobo):
        self.type = 'yoso'
        self.dobo = dobo
        self.pixels = [Pixel(0,0,0,self.color , self)for i in range(58)]

    def ombre(self):
        self.element='ombre'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'black'
        self._temp = create_rond(4)
        for i in range(len(self._temp)):
            self.pixels[i].forme(self._temp[i][0],self._temp[i][1],self.z*(-1))
        for i in range(15):
            self.dobo.pixels[i+115].color='black'
    
    def espris(self):
        self.element='espris'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'grey70'
        for i in range(15):
            self.dobo.pixels[i+115].color='grey70'
    
    def none(self):
        self.element='none'
        D=0
        self.etat='stop'
        for i in range(50):
            D+=2*pi/50
            self.pixels[i].x=200+avix(16,D)
            self.pixels[i].y=aviy(16,D)
            self.pixels[i].z=0
            self.pixels[i].color = 'black'
        for i in range(50,len(self.pixels)):
            D+=2*pi/50
            self.pixels[i].x=-200+avix(16,D)
            self.pixels[i].y=aviy(16,D)
            self.pixels[i].z=0
            if randint(0,2)==1:
                color='red'
            else:
                color='gold'
            self.pixels[i].color = color
        for i in range(15):
            self.dobo.pixels[i+115].color='grey70'

    def cauchemard(self):
        self.element='espris'
        self.dobo.touchable=0.8
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'firebrick4'
        for i in range(15):
            self.dobo.pixels[i+115].color='firebrick4'
    
    def terre(self):
        self.element='terre'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'saddle brown'
        for i in range(8):
            self.pixels[i].forme(i//2,5+i%2,(i//4)+1)
        for i in range(8):
            self.pixels[i+8].forme(i//2,(-1)*(5+i%2),(i//4)+1)
        self._temp = create_cercle(5.5)
        for i in range(len(self._temp)):
            self.pixels[i+16].forme(self._temp[i][0],self._temp[i][1],-2)
        for i in range(15):
            self.dobo.pixels[i+115].color='saddle brown'

    def fer(self):
        self.element='fer'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'honeydew3'
        for i in range(6):
            self.pixels[i+4].color = 'black'
        self._temp = create_epee(0,pi/2,pi/2)
        for i in range(len(self._temp)):
            self.pixels[i].forme(self._temp[i][0]-6, -self._temp[i][1], self._temp[i][2]-3)
        for i in range(15):
            self.dobo.pixels[i+115].color='honeydew3'

    def foudre(self):
        self.element='foudre'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'gold'
        for i in range(6):
            self.pixels[i*5].color = 'gold4'
        self._temp = create_queu1(pi,-2*pi/5)
        for i in range(len(self._temp)):
            self.pixels[i].forme(self._temp[i][0]-6, self._temp[i][1], self._temp[i][2]+1)
        for i in range(15):
            self.dobo.pixels[i+115].color='gold'

    def feux(self):
        self.element='feux'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'red'
        for i in range(20):
            self.pixels[i*5].color = 'dark orange'
        self._temp = create_queu2(pi,-2*pi/5)
        for i in range(len(self._temp)):
            self.pixels[i].forme(self._temp[i][0]-6+randint(-int(i/10),int(i/10)), self._temp[i][1]+randint(-int(i/10),int(i/10)), self._temp[i][2]+2+randint(-int(i/5),int(i/10)))
        for i in range(15):
            self.dobo.pixels[i+115].color='red'
    
    def eau(self):
        self.element='eau'
        for i in range(len(self.pixels)):
            self.pixels[i].forme(0,0,0)
            self.pixels[i].color = 'Deepskyblue2'
        for i in range(20):
            self.pixels[i*5].color = 'Deepskyblue3'
        self._temp = create_rond(5)
        for i in range(len(self._temp)):
            self.pixels[i].forme(self._temp[i][0]-2, self._temp[i][2], self._temp[i][1]-2)
        for i in range(15):
            self.dobo.pixels[i+115].color='Deepskyblue2'

class Pixel:
    def __init__(self, dx, dy, dz, color, item):
        self.item = item
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.visible=True
        self.color = color
        self.x = self.item.x+avix(self.dx,self.item.d)+aviy(self.dy,self.item.d)
        self.y = self.item.y+avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2)
        self.z = self.item.z+self.dz

    def denombre(self, nombre):
        self.id = nombre
    
    def forme(self, dx, dy, dz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
    
    def position(self, FPS):
        if self.item.etat=='liq':
            self.bx = self.item.x+(avix(self.dx, self.item.d)+aviy(self.dy, self.item.d))
            self.by = self.item.y+(avix(self.dx, self.item.d+pi/2)+aviy(self.dy, self.item.d+pi/2))
            self.bz = self.item.z+self.dz
            d , v = ddir(self.x , self.y, self.z, 0, 0, self.bx,self.by, self.bz)
            dist = ddis(self.x , self.y, self.z, self.bx,self.by, self.bz)
            vi=(self.item.flui*FPS)+abs(self.item.dobo.v_z)+dist/20
            if dist>vi:
                X, Y, Z = avixyz(vi,d,v)
                self.x += X
                self.y += Y
                self.z += Z
            else:
                self.x = self.item.x+(avix(self.dx,self.item.d)+aviy(self.dy,self.item.d))
                self.y = self.item.y+(avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2))
                self.z = self.item.z+self.dz
            
        elif self.item.etat=='fix':
            self.bx = self.item.x+(avix(self.dx, self.item.d)+aviy(self.dy, self.item.d))
            self.by = self.item.y+(avix(self.dx, self.item.d+pi/2)+aviy(self.dy, self.item.d+pi/2))
            self.bz = self.item.z+self.dz
            d , v = ddir(self.x , self.y, self.z, 0, 0, self.bx, self.by, self.bz)
            dist = ddis(self.dx , self.dy, self.dz, self.item.fx, self.item.fy, self.item.fz)
            Di=ddis(self.x , self.y, self.z, self.bx,self.by, self.bz)
            if dist!=0:
                vi=(self.item.flui*FPS)+(200*FPS/dist)+(Di/20)
                if  Di>vi:
                    X, Y, Z = avixyz(vi,d,v)
                    self.x += X
                    self.y += Y
                    self.z += Z
                else:
                    self.x = self.item.x+(avix(self.dx,self.item.d)+aviy(self.dy,self.item.d))
                    self.y = self.item.y+(avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2))
                    self.z = self.item.z+self.dz
            else:
                self.x = self.item.x+(avix(self.dx,self.item.d)+aviy(self.dy,self.item.d))
                self.y = self.item.y+(avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2))
                self.z = self.item.z+self.dz

        elif self.item.etat=='fou':
            self.bx = self.item.x+(avix(self.dx, self.item.d)+aviy(self.dy, self.item.d))
            self.by = self.item.y+(avix(self.dx, self.item.d+pi/2)+aviy(self.dy, self.item.d+pi/2))
            self.bz = self.item.z+self.dz
            d , v = ddir(self.x , self.y, self.z, 0, 0, self.bx, self.by, self.bz)
            dist = dis(self.dx , self.dy, self.item.fx, self.item.fy)
            Di=ddis(self.x , self.y, self.z, self.bx,self.by, self.bz)
            if dist!=0:
                vi=(self.item.flui*FPS)+(50*FPS/(dist**0.5))+(Di/10)
                if  Di>vi:
                    X, Y, Z = avixyz(vi,d,v)
                    self.x += X
                    self.y += Y
                    self.z += Z
                else:
                    self.x = self.item.x+(avix(self.dx,self.item.d)+aviy(self.dy,self.item.d))
                    self.y = self.item.y+(avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2))
                    self.z = self.item.z+self.dz
            else:
                self.x = self.item.x+(avix(self.dx,self.item.d)+aviy(self.dy,self.item.d))
                self.y = self.item.y+(avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2))
                self.z = self.item.z+self.dz
        
        elif self.item.etat=='stop':
            pass
        
        else:
            self.x = self.item.x+(avix(self.dx,self.item.d)+aviy(self.dy,self.item.d))
            self.y = self.item.y+(avix(self.dx,self.item.d+pi/2)+aviy(self.dy,self.item.d+pi/2))
            self.z = self.item.z+self.dz
    
    def pers(self,x,y,xcam, ycam, zcam, dcam, vcam):
        self.perx,  self.pery =  per_point(x, y, xcam, ycam, zcam, dcam, vcam, self.x, self.y, self.z)
        self.dist = int(1.4*x/ddis(xcam, ycam, zcam, self.x, self.y, self.z))
    
    def affiche(self, corp):
        if self.z<0.1 and self.visible:
            corp.toile.itemconfig(corp.corp, fill=self.color)
            X=self.perx
            Y=self.pery
            corp.toile.coords(corp.corp, X-self.dist, Y-self.dist, X+self.dist, Y+self.dist)
        else:
            corp.toile.coords(corp.corp,0,0,0,0)
    
    def affiche_1(self, corp, x1, y1):
        if self.z<0.1 and self.visible:
            corp.toile.itemconfig(corp.corp, fill=self.color)
            X=self.perx+x1
            Y=self.pery+y1
            corp.toile.coords(corp.corp, X-self.dist, Y-self.dist, X+self.dist, Y+self.dist)
        else:
            corp.toile.coords(corp.corp,0,0,0,0)

class Aff:
    def __init__(self, i, item, adresse ,toile):
        self.i = i
        self.adresse = adresse
        self.item = item
        self.toile = toile
        self.corp = toile.create_rectangle(0,0,0,0,width = 0)
    
    def dist(self, xcam, ycam, zcam):
        self.distance = ddis(xcam, ycam, zcam, self.item[self.i].x, self.item[self.i].y, self.item[self.i].z)

class Vie:
    def __init__(self, i, item, toile, x, y):
        self.i = i
        self.tx= x
        self.ty= y
        self.item = item
        self.toile = toile
        self.font = toile.create_rectangle(0,0,0,0, fill='white')
        self.barre = toile.create_rectangle(0,0,0,0, fill='red', width = 0)
    
    def dist(self, xcam, ycam, zcam):
        it_ = self.item[self.i]
        self.dobo = it_
        self.distance = ddis(xcam, ycam, zcam, it_.x, it_.y, it_.z-10)
    
    def cache(self):
        self.toile.coords(self.barre, -1,-1,-1,-1)
        self.toile.coords(self.font, -1,-1,-1,-1)
    
    def place(self, cam):
        C=per_point(self.tx, self.ty, cam.x, cam.y, cam.z, cam.d, cam.v, self.dobo.x, self.dobo.y, self.dobo.z-10)
        self.toile.coords(self.barre,C[0]-50, C[1]-4,C[0]-50+int(self.dobo.vie),C[1]+5)
        self.toile.coords(self.font,C[0]-51, C[1]-5,C[0]+50,C[1]+5)


def devant(item):
    start = True
    while start:
        start=False
        for i in range(len(item)):
            if i+1<len(item):
                if item[i].distance<item[i+1].distance:
                    num = item[i+1].i
                    item[i+1].i = item[i].i
                    item[i].i = num
                    distance = item[i+1].distance
                    item[i+1].distance = item[i].distance
                    item[i].distance = distance
                    start = True
        if start:
            start=False
            for i in range(len(item)):
                i=len(item)-(i+1)
                if i>0:
                    if item[i].distance>item[i-1].distance:
                        num = item[i-1].i
                        item[i-1].i=item[i].i
                        item[i].i = num
                        distance = item[i-1].distance
                        item[i-1].distance = item[i].distance
                        item[i].distance = distance
                        start=True
    return item
