from backwork.Item import*
from client.Myoso import*

class Dobotzu(Item):
    def __init__(self, x, y, z, color,d, terrain):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.v_z = 0
        self.flui=3
        self.vie=100
        self.stun=False
        self.electrique=0
        self.temperature=0
        self.armor=True
        self.element='none'
        self.etat='solide'
        self.color = color
        self.pixels=[]
        self.yoso=Yoso(self)
        self.armes=[armes(self)for i in range(10)]
        _pix= [Pixel(0,0,0,"black", self)for i in range(15)]
        self.etoile = Etoile(self, _pix, terrain)
    
    def tour(self, FPS):
        self.yoso.tour()
        self.etoile.tour(FPS)
        if self.armor and self.yoso.element=='terre':
            for i in range(50):
                a=((i*11)+15)%115
                self.pixels[a].color='saddle brown'
        if self.electrique!=0:
            actif=abs(int(self.electrique))
            if self.electrique<0:
                color='goldenrod'
            if self.electrique>0:
                color='turquoise2'
            for i in range(actif):
                a=randint(0,114)
                self.pixels[a].color=color
        if self.temperature>0:
            self.temperature=self.temperature/(2**(FPS/25))
            for i in range(50):
                a=((i*12)+30)%len(self.pixels)
                if i<self.temperature-1:
                    self.pixels[a].color='firebrick4'
    
    def propriete(self,mess):
        self.position (float(mess[3]),
         float(mess[4]),float(mess[5]),
         float(mess[6]), float(mess[7]), 
         int(mess[8]), int(mess[9]), 
         int(mess[10]), int(mess[11]))
        
    def refre(self):
        self.pixels=[]
        self.yoso.refre()
        for ar in self.armes:
            ar.refre()
        
    def position(self,x, y, z,d, vie, stun, el, T, armor):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.vie = vie
        self.stun= stun==1
        self.temperature=T
        self.electrique= el
        self.armor= armor==1
    
    def particules(self, pix, nb1, nb2):
        self.pixels=[pix[i] for i in range(nb1, nb2)]

class armes(Item):
    def __init__(self, dobo):
        self.dobo=dobo
        self.pixels=[]
        self.etat='sol'
        self.yoso=dobo.yoso
        self.actif=0
        self.syncro(dobo)
    
    def refre(self):
        self.pixels=[]
        self.actif=0

    def propriete(self, mess):
        self.actif=1
        self.x=float(mess[3])
        self.y=float(mess[4])
        self.z=float(mess[5])
        self.d=float(mess[6])
        self.v=float(mess[7])

class Etoile(Item):
    def __init__(self, dobo, pixels, terrain):
        self.dobo = dobo
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.pixels = pixels
        self.d = 0
        self.terrain= terrain
        self.z = 0
        self.Mcout=0
        self.t = 0
        self.etat='solide'
        self.type='armes'
        for i in range(len(pixels)):
            pixels[i].item=self
        self.particules=[{'x':0, 'y':0, 't':0, 'a':0, 'p':i}for i in range(len(self.pixels))]

    def tour(self, FPS):
        _temp = create_cercle(5)
        self.t += FPS*2
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = 0
        if self.t>=1:
            _t=self.dobo.stun==0
            for part in self.particules:
                if part['p']%3==1:
                    if part['a']==0 and _t:
                        _t=False
                        self.t-=1
                        part['a']=1
                        pix=self.pixels[part['p']]
                        pix.item=self.terrain
                        part['x']=pix.x
                        part['y']=pix.y
                        part['z']=0
                        part['t']=0
        for i in range(15):
            if self.particules[i]['a']==0:
                self.pixels[i].forme(_temp[i][0],_temp[i][1],0)
            else:
                part=self.particules[i]
                pix=self.pixels[i]
                if part['t']>=5:
                    pix.item=self
                    pix.forme(_temp[i][0],_temp[i][1],0)
                    part['a']=0
                else:
                    part['t']+=FPS*3
                    pix.forme(part['x'], part['y'], part['z'])


        if self.dobo.stun==1:
            for i in range(5):
                x0,y0,z0 = avixyz(5,i*2*pi/5,0)
                self.pixels[i*3].forme(x0,y0,self.dobo.z-7)
                self.d+=FPS/10
