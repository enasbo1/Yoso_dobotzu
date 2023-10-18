from backwork.dddirection import*
from serveur.Myoso import*
from backwork.pressed import taille
from random import randint

def points_feux(part):
    r=''
    for i, par in enumerate(part):
        if i>0:
            r+='('
        r+=str((int(par['x']*1000)/1000)+randint(-2,3))
        r+=')'+str((int(par['y']*1000)/1000)+randint(-2,3))
        r+=')'+str((int(par['z']*1000)/1000)+randint(-2,3))
    return(r)

def points_fix(part):
    r=''
    for i, par in enumerate(part):
        if i>0:
            r+='('
        r+=str(int(par['x']*1000)/1000)
        r+=')'+str(int(par['y']*1000)/1000)
        r+=')'+str(int(par['z']*1000)/1000)
    return(r)

def true():
    return(True)

def tourne_avan(dcam):
    D = -dcam
    return D

def tourne_arrie(dcam):
    D = rot(pi, -dcam)
    return D

def tourne_droite(dcam):
    D = rot(-pi/2, -dcam)
    return D

def tourne_gauche(dcam):
    D = rot(pi/2, -dcam)
    return D

class Dobotzu(Item):
    def __init__(self, x, y, z, color,d, pixels, p_yoso):
        self.x = x
        self.y = y
        self.z = z
        self.d = d
        self.flui=3
        self.chute=True
        self.vie=100
        self.stun=0
        self.boost=1
        self.D=d
        self.p8=False
        self.mort=0
        self.electrique=0
        self.temperature=0
        self.resistance=0
        self.chield=0
        self.man=True
        self.armor=True
        self.etourdi=0
        self.pressed=[False for i in range(taille)]
        self.touchable=1
        self.element='none'
        self.etat='solide'
        self.color = color
        self.masse=1
        self.mun = 0
        self.FPS = 0
        self.E = 40
        self.En = 30
        self.M = 20
        self.Ma = 20
        self.v_z=0
        self.coo=[0,0,0,0]
        self.type = "dobo"
        self.pixel=pixels[0]
        self.pixels=pixels
        self.retard=-5
        self.forme=["dobo"]+pixels+[""]
        self.actif=1
        self.yoso=Yoso(self,p_yoso)
        self.armes=[Armes(self,self.yoso)for i in range(10)]

    def caract(self):
        if self.stun>10:
            stun=1
        else:
            stun=0
        return([int(self.x*1000)/1000,
         int(self.y*1000)/1000,
         int(self.z*1000)/1000,
         int(self.d*1000)/1000,
         int(self.vie*100)/100,
         int(stun),
         int(self.electrique), 
         int(self.temperature), 
         int(self.armor)])
    
    def tour(self, adv, FPS):
        self.FPS=FPS
        if self.electrique!=0:
            self.stun+=abs(self.electrique*FPS/5)
        if self.temperature>0:
            self.chield-=self.temperature*FPS/40
            self.temperature=self.temperature/(2**(FPS/25))
        if self.vie<=0:
            self.vie=0
        if self.masse<1:
            self.masse+=0.05*FPS
        if self.masse>1:
            self.masse-=0.05*FPS
        if self.electrique<-FPS/10:
            self.electrique+=FPS/10
        elif self.electrique>FPS/10:
            self.electrique-=FPS/10
        else:
            self.electrique=0
        if self.stun>=0+FPS/3:
            self.stun-=FPS/3
        else:
            self.stun=0
        if self.stun>=10:
            self.etourdi+=FPS/5
        if self.etourdi>=2:
            self.stun=0
            self.etourdi=0
        if self.stun<10 and self.etourdi>1:
            self.stun=0
            if 0<self.vie<=100-FPS:
                self.vie+=FPS/50
        if self.chute:
            if self.z<-7.6:
                self.v_z+=1*FPS
            if self.z>-7.6 and self.v_z>=0:
                self.z=-7+(self.v_z/10)
                self.v_z=0
            if self.z>=-6+0.5:
                self.v_z=-5*FPS*self.masse
        if self.vie<=0:
            self.stun=20
            self.vie=0
            if self.mort<14:
                self.chute=False
                self.z-=FPS/5
                self.mort+=FPS/7
            else:
                self.chute=False
                self.z=10
        if not self.chute:
            self.v_z=0
        if self.vie>0:
            self.chute=True
            self.mort=0
        self.z+=self.v_z*FPS*10
        if self.Ma<=self.M-FPS/5 and self.En>=2*FPS/5:
            self.Ma+=2*FPS/5
            self.En-=3*FPS/5
        elif self.Ma>self.M-FPS/5:
            self.Ma=20
        if self.En<self.E:
            self.En+=FPS
        else:
            self.En=self.E
        for i in range(len(self.coo)):
            self.coo[i]-=FPS
        self.p8=False
    
    def avance(self, vi, FPS):
        if self.stun<10:
            self.x += avix((vi*FPS)/self.masse, self.d)
            self.y += aviy(-(vi*FPS)/self.masse, self.d)
    
    def test(self):
        reponseE=False
        reponseA=False
        reponse8=False
        if self.stun<10:
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=4
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.retard<-4:
                        reponseE=True
                Mcout=0
                Ecout=2
                if self.En>=Ecout and self.Ma>=Mcout:
                    if  self.coo[2]<0:
                        reponseA=True
                Mcout=0
                Ecout=4
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0:
                        reponse8=True
            if self.yoso.element=='espris':
                Mcout=0
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0:
                        reponseE=True
                Mcout=0
                Ecout=3
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[2].charge==0 :
                        reponseA=True
            if self.yoso.element=='eau':
                Mcout=self.FPS/2
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    reponseA=True
                Mcout=7
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0 and self.coo[2]<0:
                        reponseE=True
                reponse8=True
            if self.yoso.element=='feux':
                Mcout=self.FPS/2
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    reponseA=True
                Mcout=7
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0 and self.coo[2]<0:
                        reponseE=True
                reponse8=True
                if self.armes[2].charge==2:
                    reponse8=False

            if self.yoso.element=='ombre':
                Mcout=5
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[1]<0 :
                        if self.armes[0]:
                            reponseE=True
                Mcout=3
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        if self.armes[0]:
                            reponseA=True

                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        if self.armes[0].charge==0 and not self.pressed[0]:
                            reponse8=True
            if self.yoso.element=='foudre':
                if self.pressed[0]:
                    Mcout=3
                    Ecout=0
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[1]<0 :
                            reponseE=True
                else:
                    Mcout=4
                    Ecout=0
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[1]<0 :
                            reponseE=True
                Mcout=1
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        e=False
                        for i in range(3):
                            if self.armes[i].charge==0:
                                e=True
                        if e:
                            reponseA=True
                Mcout=5
                Ecout=10
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[3]<0 :
                        reponse8=True
            if self.yoso.element=='fer':
                if self.pressed[0]:
                    Mcout=1
                    Ecout=3
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[1]<0 :
                            reponseE=True
                else:
                    Mcout=1
                    Ecout=3
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[2]<0 :
                            reponseE=True
                Mcout=0
                Ecout=3
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        if self.armes[0].charge==0:
                            reponseA=True
                Mcout=5
                Ecout=2
                if self.armes[1].charge==0 and self.coo[3]<0:
                    reponse8=True
        if self.pressed[6]:
            reponseA=False
        if self.pressed[5]:
            reponseE=False
        if self.pressed[1]:
            reponse8=False
        return(reponseE,reponseA,reponse8)

    def competence_e(self, FPS, enemi, cam):
        if self.stun<10:
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=4
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.retard<-4:
                        self.boost=1.5
                        self.retard=1
                        self.En-=Ecout
            if self.yoso.element=='espris':
                Mcout=0
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0:
                        self.armes[1].tele_1([self.yoso.pixels[i]for i in range(100)])
                        self.Ma-=Mcout
            if self.yoso.element=='eau':
                Mcout=7
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0 and self.coo[2]<0:
                        self.armes[1].bule_1([self.yoso.pixel+91, self.yoso.pixel+115],cam.d, cam.v)
                        self.coo[2]=10
                        self.Ma-=Mcout
                        self.En-=Ecout
            if self.yoso.element=='feux':
                Mcout=7
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0 and self.coo[2]<0:
                        self.armes[1].brule_1([self.yoso.pixel+91, self.yoso.pixel+115], cam.d, cam.v)
                        self.coo[2]=10
                        self.Ma-=Mcout
                        self.En-=Ecout
            
            if self.yoso.element=='ombre':
                Mcout=5
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[1]<0 :
                        if self.armes[0]:
                            self.armes[0].atrac_ombre_1([self.yoso.pixels[114-i]for i in range(115)])
                            self.coo[1]=25
                            self.Ma-=Mcout
                            self.En-=Ecout
            if self.yoso.element=='foudre':
                if self.pressed[0]:
                    Mcout=3
                    Ecout=0
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[1]<0 :
                            charge=1
                            self.armes[3].elec_dash([self.yoso.pixel,self.yoso.pixel+35], 'up')
                            for a in range(12):
                                if charge==1:
                                    X=self.x
                                    Y=self.y
                                    Z=self.z-a*5
                                    for adv in enemi:
                                        if charge==1 and adv!=self:
                                            dist=ddis(X, Y, Z, adv.x, adv.y, adv.z)
                                            if dist<50:
                                                adv.aie(3,5,0,-9,self)
                                                charge=2
                            self.z-=60/self.masse
                            self.coo[1]=1
                            self.Ma-=Mcout
                            self.En-=Ecout
                else:
                    Mcout=4
                    Ecout=0
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[1]<0 :
                            charge=1
                            self.armes[3].elec_dash([self.yoso.pixel,self.yoso.pixel+35], 'front')
                            for a in range(33):
                                if charge==1:
                                    X,Y,Z= avixyz(a*2.5, self.d,0)
                                    X+=self.x
                                    Y+=self.y
                                    Z=self.z
                                    for adv in enemi:
                                        if charge==1 and adv!=self:
                                            dist=ddis(X, Y, Z, adv.x, adv.y, adv.z)
                                            if dist<30:
                                                adv.aie(3,5,0,-8,self)
                                                charge=2
                            self.x += avix(80/self.masse, self.d)
                            self.y += aviy(-80/self.masse, self.d)
                            self.coo[1]=1
                            self.Ma-=Mcout
                            self.En-=Ecout
            if self.yoso.element=='fer':
                if self.pressed['space']:
                    Mcout=1
                    Ecout=3
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[1]<0 :
                            charge=1

                            self.z+=60
                            if self.z>-7:
                                self.z=-7
                                for i in range(len(enemi)):
                                    if charge==1:
                                        dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                                        if dist<60:
                                            enemi[i].aie(10,5,0,0,self)
                                            charge=3
                            self.coo[1]=10
                            self.Ma-=Mcout
                            self.En-=Ecout
                else:
                    Mcout=1
                    Ecout=3
                    if self.En>=Ecout and self.Ma>=Mcout:
                        if self.coo[2]<0 :
                            x0,y0,z0 = 0,0,0
                            charge=1
                            if self.armes[0].charge==0:
                                for a in range(34):
                                    if charge==1:
                                        X,Y,Z= avixyz(a*2.5, self.d,0)
                                        X+=self.x
                                        Y+=self.y
                                        Z=self.z
                                        for i in range(len(enemi)):
                                            if charge==1:
                                                dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                                                if dist<40:
                                                    enemi[i].aie(10,3,0,0,self)
                                                    charge=2
                                self.x += avix(80/self.masse, self.d)
                                self.y += aviy(-80/self.masse, self.d)
                                self.coo[2]=8
                                self.Ma-=Mcout
                                self.En-=Ecout
                                self.armes[0].ai_1([self.yoso.pixels[i]for i in range(100)])                                    
        return(self.En, self.Ma)

    def competence_a(self, FPS, enemi, cam):
        if self.stun<10:
            if self.yoso.element=='eau':
                Mcout=FPS/2
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[0].charge==0:
                        self.armes[0].vague_1([self.yoso.pixel+41,self.yoso.pixel+91], cam.d)
                    self.Ma-=Mcout
                    self.En-=Ecout
            if self.yoso.element=='feux':
                Mcout=FPS/2
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[0].charge==0:
                        self.armes[0].flame_1([self.yoso.pixel+41, self.yoso.pixel+91], cam.d)
                    self.Ma-=Mcout
                    self.En-=Ecout
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=2
                if self.En>=Ecout and self.Ma>=Mcout:
                    if  self.coo[2]<0:
                        self.armes[1].frape_1([self.yoso.pixel, self.yoso.pixel+16])
                        self.coo[2]=1
                        self.Ma-=Mcout
                        self.En-=Ecout
            if self.yoso.element=='ombre':
                Mcout=3
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        if self.armes[0]:
                            self.armes[0].lance_ombre_1([self.yoso.pixels[114-i]for i in range(115)])
                            self.coo[2]=5
                            self.Ma-=Mcout
                            self.En-=Ecout
            if self.yoso.element=='foudre':
                Mcout=1
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        e=-1
                        for i in range(3):
                            if self.armes[i].charge==0:
                                e=i
                        if e!=-1:
                            _e=self.yoso.pixel+114-((e*4))
                            self.armes[e].tir_foudre_1([_e-4, _e], cam.d, cam.v)
                            self.coo[2]=0.5
                            self.Ma-=Mcout
                            self.En-=Ecout    
            if self.yoso.element=='espris':
                Mcout=0
                Ecout=3
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[2].charge==0 :
                        self.armes[2].late_esp_1([self.yoso.pixels[100+i]for i in range(10)])
                        self.coo[2]=1.5
                        self.Ma-=Mcout
                        self.En-=Ecout
            if self.yoso.element=='fer':
                Mcout=0
                Ecout=3
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[2]<0 :
                        e=-1
                        for i in range(1):
                            if self.armes[i].charge==0:
                                e=i
                        if e!=-1:
                            self.armes[e].late_fer_1([self.yoso.pixels[i]for i in range(58)])
                            self.coo[2]=1.5
                            self.Ma-=Mcout
                            self.En-=Ecout
    
    def competence_8(self, FPS, enemi, cam):
        if self.stun<10:
            if self.man:
                self.p8 = True
            else:
                self.man=True
            if self.yoso.element=='feux':
                Mcout=FPS*1.5
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    self.armes[2].pyro_1(self.pixels)
                    self.armes[2].goold=True
                    if self.armes[2].charge==1:
                        self.Ma-=Mcout
                        self.En-=Ecout
            if self.yoso.element=='eau':
                Mcout=FPS
                Ecout=-FPS
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.vie<=100-FPS:
                        self.vie+=FPS
                    else:
                        Mcout-=3*FPS/4
                    if self.En>40-FPS:
                        Mcout-=FPS/4
                        Ecout=0
                    self.forme[0]='dobeau'
                    self.Ma-=Mcout
                    self.En-=Ecout
            if self.yoso.element=='ombre':
                Mcout=3
                Ecout=0
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[0].charge==0 and not self.pressed['space']:
                        self.retard=0.5
                        self.armes[0].ombre_1([self.yoso.pixels[i]for i in range(115)])
                        self.armes[0].good=True
                        self.Ma-=Mcout
                        self.En-=Ecout
            if self.yoso.element=='foudre':
                Mcout=5
                Ecout=10
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.coo[3]<0 :
                        self.armes[4].eclair([self.yoso.pixel, self.yoso.pixel+35])
                        self.coo[3]=20
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=4
                if self.En>=Ecout and self.Ma>=Mcout:
                    if self.armes[1].charge==0:
                        self.armes[1].shoot_1(self.armes[2])
                        self.Ma-=Mcout
                        self.En-=Ecout
            if self.yoso.element=='fer':
                Mcout=5
                Ecout=2
                if self.armes[1].charge==0 and self.coo[3]<0:
                    self.armes[1].armure_1([self.yoso.pixels[114-i]for i in range(30)])
                    self.Ma-=Mcout
                    self.En-=Ecout
                if self.armes[1].charge!=0:
                    self.Ma-=FPS
        if self.Ma<=0:
            self.man=False
    
    def saut(self):
        if self.stun<10:
            if self.En>=3 and self.yoso.element!='ombre':
                if self.z>-7.6 and self.coo[0]<0:
                    self.v_z=-2/self.masse
                    self.coo[0]=3
                    self.En-=3

    def aie(self, degats, stun, temperature, charge, enemi):
        if self.temperature<0:
            touchable=self.touchable*(1-self.temperature/50)
        else:
            touchable=self.touchable
        if enemi.stun<10:
            if degats-self.resistance>0:
                self.chield -= (degats-self.resistance)*touchable
            if temperature!=0:
                self.temperature += (temperature[0]-self.temperature)*temperature[1]*touchable
            if charge!=0:
                self.chield -= (abs(charge-self.electrique)/2)*touchable
                self.electrique+=((charge-self.electrique)/4)*touchable
            if self.stun<10:
                self.stun+=stun*touchable
            else:
                self.stun += stun*touchable
            if self.stun>10:
                self.chield -= degats
            if self.yoso.element=='fer':
                if self.armes[1].charge==1:
                    if self.armes[1].competence==self.armes[1].armure_2 and self.armes[1].avance<0.3:
                        enemi.stun+=14
    
    def recul(self, vi, D,  V):
        x,y,z=avixyz(vi*self.touchable, D, V,)
        self.x+=x
        self.y+=y
        self.z+=z
        
    def passif(self, FPS, enemi):
        if self.Ma<0:
            self.Ma=0
        for i in range(len(enemi)):
            dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
            if dist<12 and self.touchable>0 and enemi[i].touchable>0:
                D, V = ddir(self.x, self.y, self.z, 0, 0, enemi[i].x, enemi[i].y, enemi[i].z)
                while 1<dist<12:
                    X,Y,Z=avixyz(1,D,V)
                    enemi[i].x+=X
                    enemi[i].y+=Y
                    enemi[i].z+=Z
                    dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
        if self.retard!=5:
            self.retard-=FPS/5
        self.yoso.tour()
        self.forme[0]='dobo'
        if self.yoso.element=='terre':
            if self.retard<0:
                self.boost=1
            else:
                self.yoso.forme[3]='grey12'
            if self.armor:
                if self.Ma<20:
                    self.En+=2*FPS/5
                self.Ma+=self.chield*2
                self.touchable=0.5
                self.chield=0
                if self.Ma<0:
                    self.armor=False
                    self.vie+=self.Ma
                    self.Ma=0
            else:
                self.En+=FPS
                self.touchable=1
                if self.Ma>10:
                    self.armor=True
        for ar in self.armes:
            ar.tour(enemi, FPS, self.cam.d, self.cam.v)
        dist=ddis(0,0,0,self.x, self.y, self.z)
        if dist>750:
            D, V = ddir(0,0,0,0,0,self.x, self.y, self.z)
            while dist>750:
                X,Y,Z=avixyz(-1, D, V)
                self.x += X
                self.y += Y
                self.z += Z
                dist=ddis(0,0,0,self.x, self.y, self.z)
        self.vie+=self.chield
        self.chield=0
        if self.yoso.element=='espris':
            if self.armes[0].charge!=0:
                man=self.armes[0].puissance
            else:
                man=100
            self.Ma=man/5
            if self.Ma<=20-FPS/5:
                self.En+=2*FPS/5
        if self.stun<10:
            if self.yoso.element=='ombre':
                if self.pressed['space']:
                    Mcout=3*FPS/5
                    Ecout=0
                    if self.En>=Ecout and self.Ma>=Mcout:
                        self.z=7
                        self.chute=False
                        self.v_z=-0.5
                        self.touchable=0
                        self.Ma-=Mcout
                        self.En-=Ecout
                else:
                    self.touchable=1
                    self.chute=True
        else:
            if self.stun>20:
                self.stun=20
        if self.yoso.element=='fer':
            self.Ma-=self.armes[0].Mcout
            self.armes[0].Mcout=0
        return(self.En, self.Ma)


class Armes(Dobotzu):
    def __init__(self, dobo, yoso):
         self.dobo = dobo
         self.yoso = yoso
         self.x = self.dobo.x
         self.y = self.dobo.y
         self.z = self.dobo.z
         self.d = self.dobo.d
         self.v=0
         self.chat = 0
         self.feel = 0
         self.Mcout = 0
         self.type='armes'
         self.charge = 0
         self.actif=0

    def caract(self):
        return([int(self.x*1000)/1000,
         int(self.y*1000)/1000, 
         int(self.z*1000)/1000, 
         int(self.d*1000)/1000,
         int(self.v*1000)/1000])

    def tour(self, enemi, FPS, dcam, vcam):
        if self.charge!=0:
            self.competence(enemi, FPS, dcam, vcam)
            self.actif=1
        else:
            self.actif=0
    
    def stop(self, enemi, FPS, dcam, vacm):
        self.charge=0
      
    def tir_foudre_1(self, pixels, dcam, vcam):
        self.charge = 1
        self.pixels = pixels
        self.forme=['tir_elec']+self.pixels+['']
        self.tim = 0
        self.etat='solide'
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = dcam
        self.v = vcam
        self.competence = self.tir_foudre_2

    def tir_foudre_2(self, enemi, FPS, dcam, vcam):
        self.tim+=FPS/5

        if self.charge==1:
            X,Y,Z= avixyz(100*FPS, self.d,self.v)
            self.x += X
            self.y += Y
            self.z += Z
            self.forme=['tir_elec']+self.pixels+['']
            for a in range(20):
                if self.charge==1:
                    X,Y,Z= avixyz(-a*5, self.d,self.v)
                    X+=self.x
                    Y+=self.y
                    Z+=self.z
                    for i in range(len(enemi)):
                        if self.charge==1 and enemi[i]!=self.dobo:
                            dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                            if dist<10:
                                enemi[i].aie(1,1,0,3,self.dobo)
                                self.charge=2
        if self.tim>0.75:
            self.charge=2
        if self.charge==2:
            self.syncro(self.dobo)
            self.competence = self.stop
    
    def elec_dash(self, pixels, ty):
        self.pixels=pixels
        self.charge=1
        self.syncro(self.dobo)
        self.forme=['traine']+pixels+[ty]
        self.competence = self.stop
    
    def eclair(self, pixels):
        self.syncro(self.dobo)
        self.charge=1
        self.tim = 0
        self.pixels=pixels
        self.forme=['none',0,0,'']
        self.competence=self.eclair2
    
    def eclair2(self, enemi, FPS, dcam, vcam):
        self.tim+=FPS
        if self.tim<=5:
            self.dobo.forme[0]='inv_eclair'
        if self.tim>5 and self.charge==1:
            self.syncro(self.dobo)
            Mcout=5
            Ecout=10
            if self.dobo.En>=Ecout and self.dobo.Ma>=Mcout:
                self.forme=['eclair']+self.pixels+['']
                for i in range(len(enemi)):
                    dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                    if dist<80 and enemi[i]!=self.dobo:
                        enemi[i].aie(3,12,0,-10,self.dobo)
                self.dobo.Ma-=Mcout
                self.dobo.En-=Ecout
                self.charge==2
        if self.tim>7:
            self.competence = self.stop

    """
    def late_fer_1(self, pixels):
        self.charge = 1
        self.pixels = pixels
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
        self.avance = 0
        self.etat='solide'
        self.flui = 6
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = self.dobo.d + pi
        self.v = pi/2
        self.competence = self.late_fer_2
    
    def late_fer_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        if self.charge==1:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self._temp=create_epee(0,self.v,pi/3)
            for i in range(len(self.pixels)):
                self.pixels[i].forme(self._temp[i][0]+9, self._temp[i][1], self._temp[i][2])
            if self.avance<0.5:
                self.d+=pi*(FPS/5)
                self.v-=2*pi*(FPS/5) 
            if self.avance>0.5:
                self.etat='solide'
                self.d = rot(4*pi*(FPS/5),self.d)
                self.v += 3*pi*(FPS/5)
                di=35
                e=-1
                for i in range(len(enemi)):
                    if self.charge==1:
                        dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                        if di>dist:
                            di=dist
                            e=i
                if e!=-1:
                    if -9<self.z-enemi[e].z<5:
                        direc=dir(self.x, self.y, -self.d, enemi[e].x, enemi[e].y)
                        if -pi*FPS*2<direc<=0:
                            enemi[e].aie(20,3,0,0,self.dobo)
                            self.charge=2
                            
        if self.avance>0.75:
            self.charge=2
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            self.yoso.etat='liq'
            for i in range(len(self.pixels)):
                self.pixels[i].x = self.x
                self.pixels[i].y = self.y
                self.pixels[i].z = self.z
                self.pixels[i].item = self.yoso

        if self.avance>1:
            self.charge=0
            self.yoso.etat='solide'

    def ai_1(self, pixels):
        self.charge=1
        self.pixels = pixels
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
        self.avance = 0
        self.etat='solide'
        self.flui = 6
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = self.dobo.d
        self.v = pi/2
        self.competence = self.ai_2
        x0, y0, z0=0,0,0
        for i in range(35):
            self.yoso.pixels[i+58].x+=x0
            self.yoso.pixels[i+58].y-=y0
            self.yoso.pixels[i+58].z+=z0+randint(-10,10)
            x1,y1,z1 = avixyz(-80/35,self.d,0)
            x0=x0+x1
            y0=y0+y1
            z0=z0+z1

    def ai_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        if self.avance<1:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            self.etat='solide'
            self._temp=create_epee(0,-pi/6,pi/6)
            for i in range(len(self._temp)):
                self.pixels[i].forme(self._temp[i][0]+9, self._temp[i][1], self._temp[i][2]+5)
        else:
            self.charge=0
            self.avance=0
            for i in range(len(self.pixels)):
                self.pixels[i].item = self.yoso

    def armure_1(self, pixels):
        self.charge = 1
        self.pixels = pixels
        self.avance = 0
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
            self.pixels[i].color='black'
        self.avance = 0
        self.etat='solide'
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = self.dobo.d
        self.v = pi/2
        self.Mcout=4
        self.competence = self.armure_2
    
    def armure_2(self, enemi, FPS, dcam, vcam):
        if self.dobo.pressed['8']:
            self.dobo.coo[3]=5
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            self.avance+=FPS/5
            self.Mcout +=3*FPS/5
            x0, y0, z0=0,0,0
            for i in range(len(self.pixels)):
                self.pixels[i].forme(x0,y0,z0+randint(-10,7))
                x0,y0,z0 = avixyz(5,randint(-100,100)*pi/100,0)
            if self.avance<0.3:
                self.dobo.resistance=20
                self.dobo.touchable=0.2
                for i in range(len(self.pixels)):
                    self.pixels[i].color='black'
            else:
                self.dobo.resistance=10
                self.dobo.touchable=0.8
                for i in range(len(self.pixels)):
                    self.pixels[i].color='honeydew3'
        else:
            self.dobo.touchable=1
            for i in range(len(self.pixels)):
                self.pixels[i].item=self.yoso
            self.dobo.resistance=0
            self.charge=0
            self.avance=0

    def ombre_1(self, pixels):
        self.pixels = pixels
        if self.charge==0:
            self.feel = 1
            self.stun = 0
            self.masse = 1
            self.charge = 1
            for i in range(len(self.pixels)):
                self.pixels[i].item=self
            self.temps = 0
            self.vie=50
            self.bd = self.dobo.d
            self.etat='solide'
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = 0
            self.d = self.dobo.d
            self.competence = self.ombre_2

    def ombre_2(self, enemi, FPS, dcam, vcam):
        self._temp = create_rond(4)
        self.Mcout=2*FPS
        t=len(self._temp)
        for i in range(len(self.pixels)):
            self.pixels[i].forme(self._temp[i%t][0],self._temp[i%t][1],0)
        e=1
        dcam=dir(self.dobo.x, self.dobo.y, 0, self.x, self.y)
        if self.dobo.pressed['4']:
            self.bd=tourne_gauche(dcam)
            self.avance(15, FPS)
            e=0
        if self.dobo.pressed['6']:
            self.bd=tourne_droite(dcam)
            if e!=0:
                self.avance(15, FPS)
                e=0
        if self.dobo.pressed['5']:
            self.bd=tourne_arrie(dcam)
            if e!=0:
                self.avance(15, FPS)
                e=0
        if self.dobo.pressed['8']:
            self.bd=tourne_avan(dcam)
            if e!=0:
                self.avance(15, FPS)
                e=0
        self.d=tourne(self.d, self.bd, FPS/2)
        if self.dobo.pressed['space']:
            self.charge = 0
            self.feel = 0
            for i in range(len(self.pixels)):
                self.pixels[i].item=self.yoso

    def lance_ombre_1(self, pixels):
        self.pixels = pixels
        self.stun=0
        self.masse=1
        if self.feel==0:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = 0
        self.charge=2
        self.temp = 0
        self.etat='solide'
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
        self.temps = 0
        self.competence = self.lance_ombre_2
        
    def lance_ombre_2(self, enemi, FPS, dcam, vcam):
        self.temp+=FPS/5
        if self.temp<0.8:
            di=100
            self._temp=self._temp = create_rond(4)
            t=len(self._temp)
            for i in range(len(self.pixels)):
                self.pixels[i].forme(self._temp[i%t][0],self._temp[i%t][1],0)
            e=-1
            for i in range(len(enemi)):
                dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                if di>dist:
                    di=dist
                    e=i
            if e!=-1:
                D,V=ddir(self.x, self.y, 0, -self.d, 0, enemi[e].x, enemi[e].y, enemi[e].z)
                _temp=create_trais(20, D, V,0,0,0)
                for i in range(20):
                    self.pixels[i].forme(_temp[i][0], _temp[i][1], _temp[i][2])
                if self.charge==2:
                    if di<25:
                        enemi[e].aie(10,0,0,0,self)
                        self.charge=3
        else:
            if self.feel==0:
                self.charge=0
                for i in range(len(self.pixels)):
                    self.pixels[i].item=self.yoso
            if self.feel==1:
                self.charge=1
                self.competence=self.ombre_2
    
    def atrac_ombre_1(self, pixels):
        self.pixels = pixels
        self.stun=0
        self.masse=1
        if self.feel==0:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = 0
        self.charge=2
        self.temp = 0
        self.etat='solide'
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
        self.temps = 0
        self.competence = self.atrac_ombre_2

    def atrac_ombre_2(self, enemi, FPS, dcam, vcam):
        if self.temps==0:
            self._temp=self._temp = create_rond(4)
            t=len(self._temp)
            for i in range(len(self.pixels)):
                self.pixels[i].forme(self._temp[i%t][0],self._temp[i%t][1],0)
            self.temps+=FPS/5
        else:
            self.temps+=FPS/5
            self.etat='liq'
            self.flui=10
            self._temp=self._temp = create_rond(4)
            t=len(self._temp)
            for i in range(len(self.pixels)):
                self.pixels[i].forme(self._temp[i%t][0],self._temp[i%t][1],0)
            if self.temps<2:
                for i in range(80):
                    X=self.pixels[i].dx+randint(-2,3)
                    Y=self.pixels[i].dy+randint(-2,3)
                    Z=self.pixels[i].dz+randint(-2,3)
                    dist = ddis(0,0,0,X,Y,Z)
                    if dist<1:
                        D=randint(-200,200)*pi/100
                        V=randint(-200,0)*pi/100
                        X, Y, Z = avixyz(50,D,V)
                        self.pixels[i].x+=X
                        self.pixels[i].y+=Y
                        self.pixels[i].z+=Z
                    else:
                        self.pixels[i].forme(0,0,0)
            if self.temps<3:
                for e in range(len(enemi)):
                    dist = ddis(self.x, self.y, 0, enemi[e].x, enemi[e].y, enemi[e].z)
                    D, V = ddir(self.x, self.y, 0, 0, 0, enemi[e].x, enemi[e].y, enemi[e].z)
                    if dist<50:
                        enemi[e].recul(-8*FPS,D,V)
                        if dist<15:
                            enemi[e].aie(FPS,FPS,0,0,self)
            else:
                self.etat='solide'
                if self.feel==0:
                    self.charge=0
                    for i in range(len(self.pixels)):
                        self.pixels[i].item=self.yoso
                if self.feel==1:
                    self.charge=1
                    self.competence=self.ombre_2
    """
    def flame_1(self, pixels, dcam):
        if self.charge==0:
            self.pixels = pixels
            self.taille= pixels[1]-pixels[0]
            self.stun=0
            self.masse=1
            self.charge=1
            self.tx = self.dobo.x
            self.ty = self.dobo.y
            self.tz = self.dobo.z
            self.x = 0
            self.y = 0
            self.z = 0
            self.d = 0
            self.particules=[{'x':self.tx,'y':self.ty,'z':self.tz,'v':0,'t':randint(0,100), 'd':dcam, 'c':0}for i in range(self.taille)]
            self.forme=['fla_point']+pixels+[points_feux(self.particules)]
            self.competence = self.flame_2

    
    def flame_2(self,enemi, FPS, dcam, vcam):
        self.tx = self.dobo.x
        self.ty = self.dobo.y
        self.tz = self.dobo.z
        if self.dobo.pressed[6]:
            for i, part in enumerate(self.particules):
                X,Y,Z=avixyz((100-part['t'])*FPS/4, part['d'], -(part['t']/(pi*100))+part['v'])
                part['x']+=X
                part['y']+=Y
                part['z']+=Z
                part['d']=rot(randint(-10,10)*FPS*pi/50,part['d'])
                part['v']=rot(randint(-10,10)*FPS*pi/50,part['v'])
                if part['t']>=100:
                    self.particules[i] =  {'x':self.dobo.x,'y':self.dobo.y,'z':self.dobo.z,'v':0,'t':0, 'd':dcam, 'c':0}
                part['t']+=FPS*randint(25,50)
                if part['c']==0:
                    for r in enemi:
                        if r!=self.dobo:
                            dist = ddis(part['x'], part['y'], part['z'], r.x, r.y, r.z)
                            if dist<6:
                                r.aie(0.3, 0.2, [50, 0.1], 0,self)
                                part['c']=1
                if part['c']==1:
                    part['x']=self.tx
                    part['y']=self.ty
                    part['z']=self.tz
        else:
            let=True
            for i, part in enumerate(self.particules):
                X,Y,Z=avixyz((100-part['t'])*FPS/4, part['d'], -(part['t']/(pi*100))+part['v'])
                part['x']+=X
                part['y']+=Y
                part['z']+=Z
                part['d']=rot(randint(-10,10)*FPS*pi/50,part['d'])
                part['v']=rot(randint(-10,10)*FPS*pi/50,part['v'])
                if part['t']>=100:
                    self.particules[i] = {'x':self.tx,'y':self.ty,'z':self.tz,'v':0,'t':101, 'd':0, 'c':1}
                else:
                    let=False
                part['t']+=FPS*randint(25,50)
                if part['c']==0:
                    for r in enemi:
                        if r!=self.dobo:
                            dist = ddis(part['x'], part['y'], part['z'], r.x, r.y, r.z)
                            if dist<6:
                                r.aie(0.3, 0.2, [50,0.1], 0,self)
                                part['c']=1
                if part['c']==1:
                    part['x']=self.tx
                    part['y']=self.ty
                    part['z']=self.tz
            if let:
                self.charge=0
            
        self.forme=['fla_point']+self.pixels+[points_feux(self.particules)]
    
    def brule_1(self, pixels, dcam, vcam):
        if self.charge==0:
            self.stun=0
            self.avances=0
            self.masse=1
            self.charge=1
            self.actif=1
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = dcam
            self.v = vcam
            X,Y,Z = avixyz(10, dcam, vcam)
            self.x+=X
            self.y+=Y
            self.z+=Z
            self.forme=['boule_feux']+pixels+['']
            self.pixels=pixels
            self.particules=[{'x':0,'y':0,'z':0,'v':0, 'd':0, 't':randint(5,10)}for i in range(pixels[1]-pixels[0])]
            for i in range(len(self.particules)):
                d=randint(-100,100)*pi/100
                v=randint(-100,100)*pi/100
                self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z']=avixyz(sqrt(randint(25,6400)), d, v)
            self.competence = self.brule_2

    def brule_2(self, enemi, FPS, dcam, vcam):
        self.avances+=FPS/5
        stop=True
        if self.charge==1:
            stop=False
        else:
            for par in self.particules:
                if par['t']>0:
                    par['x']+=randint(-2,3)*FPS
                    par['y']+=randint(-2,3)*FPS
                    par['z']+=randint(-2,3)*FPS
                    if par['z']+self.z>0:
                        par['z']=-self.z
                    par['t']-=FPS*3
                    stop=False
                else:
                    par['x']=0
                    par['y']=0
                    par['z']=0
            r=''
            for i, par in enumerate(self.particules):
                if i>0:
                    r+='('
                r+=str(int(par['x']*1000)/1000)
                r+=')'+str(int(par['y']*1000)/1000)
                r+=')'+str(int(par['z']*1000)/1000)
            self.forme=['fla_point']+self.pixels+[r]
        
        if stop:
            self.charge=0
        
        if self.charge==1:
            if self.avances>1.2 or self.z>=0:
                self.charge=2
            X,Y,Z= avixyz(50*FPS, self.d, self.v)
            self.x += X
            self.y += Y
            self.z += Z
            for a in range(20):
                if self.charge==1:
                    X,Y,Z= avixyz(-a*5, self.d,self.v)
                    X+=self.x
                    Y+=self.y
                    Z+=self.z
                    for adv in enemi:
                        if self.charge==1 and adv!=self.dobo:
                            dist=ddis(X, Y, Z, adv.x, adv.y, adv.z)
                            if dist<10:
                                adv.aie(5,4,[60,1/6],0,self.dobo)
                                self.charge=2
        if self.charge==2:
            for adv in enemi:
                if adv!=self.dobo:
                    dist=ddis(self.x, self.y, self.z, adv.x, adv.y, adv.z)
                    if dist<70:
                        adv.aie(5,4,[60,1/6],0,self)
            self.charge=3
    
    def pyro_1(self, pixels):
        if self.charge==0:
            self.pixels = pixels
            self.stun=0
            self.avance=0
            self.charge=1
            self.goold=True
            self.etat='solide'
            self.d=0
            self.forme=['torche']+self.pixels+['']
            self.good=[true()for i in range(len(self.dobo.pixels))]
            self.competence = self.pyro_2

    def pyro_2(self, enemi, FPS, dcam, vcam):
        self.x=self.dobo.x
        self.y=self.dobo.y
        self.z=self.dobo.z
        if self.goold and self.charge==1:
            self.dobo.touchable=0
            self.forme=['torche']+self.pixels+['']
            for i in enemi:
                if self.charge==1:
                    dist=ddis(self.x, self.y, self.z, i.x, i.y, i.z)
                    if dist<30:
                        i.aie(0, FPS/2, [70,FPS/20], 0, self)
            if self.dobo.pressed[0]:
                self.dobo.v_z=-1
            self.goold=False
        else:
            self.avance+=FPS
            self.charge=2
            self.forme=['brule']+self.pixels+['']
            self.dobo.touchable=1
            if self.avance>=5:
                self.charge=0
    """
    def soul_1(self, pixels):
        if self.charge==0:
            self.stun=0
            self.avance=0
            self.masse=1
            self.charge=1
            self.etat='stop'
            self.x = 0
            self.use=[False,0]
            self.y = 0
            self.z = 0
            self.puissance=100
            self.d = 0
            self.etourd=10
            self.v = 0
            self.pixels=pixels
            for i in range(len(self.pixels)):
                self.pixels[i].item=self
            self.particules=[{'x':self.dobo.x,'y':self.dobo.y,'z':self.dobo.z,'v_x':0, 'v_y':0, 'v_z':0, 'd':0, 't':randint(5,10), 'cible':-1, 'actif':False, 'ch':100}for i in range(len(pixels))]
        self.competence = self.soul_2

    def soul_2(self, enemi, FPS, dcam, vcam):
        self.puissance=100
        if self.use[0]:
            self.use[1]+=FPS
        self.use[0]=False

        if self.stun>10:
            self.etourd-=FPS
            if self.etourd<0:
                self.stun=0
        else:
            self.etourd=7
            for i, p in enumerate(self.particules):
                pix=self.pixels[i]
                if p['actif']:
                    self.puissance-=1
                    if self.dobo.pressed['8']and p['ch']>0:
                        p['ch']-=FPS
                        dist=ddis(p['x'],p['y'], p['z'],self.dobo.x, self.dobo.y, self.dobo.z)
                        D, V=ddir(p['x'],p['y'], p['z'], 0, 0, self.dobo.x, self.dobo.y, self.dobo.z)
                        x, y, z = avixyz(-FPS*1.5, D, V)
                        p['v_x']+=x
                        p['v_y']+=y
                        p['v_z']+=z

                    if self.dobo.pressed['4'] and p['ch']>0:
                        p['ch']-=FPS
                        x, y, z = avixyz(FPS*1.5, dcam, vcam)
                        p['v_x']+=x
                        p['v_y']+=y
                        p['v_z']+=z

                    if self.dobo.pressed['5'] or p['ch']<=0:
                        p['ch']-=FPS
                        D, V=ddir(p['x'],p['y'], p['z'],0,0,self.dobo.x, self.dobo.y, self.dobo.z)
                        Sp = ddis(0,0,0,p['v_x'],p['v_y'], p['v_z'])
                        x, y, z = avixyz(Sp, D, V)
                        dist = ddis(p['v_x'], p['v_y'], p['v_z'], x, y, z)
                        Di, Vi = ddir(p['v_x'],p['v_y'], p['v_z'], 0, 0, x*1.1, y*1.1, z*1.1)
                        x, y, z = avixyz(FPS*1.5, Di, Vi)
                        p['v_x']+=x
                        p['v_y']+=y
                        p['v_z']+=z
                        if ddis(p['x'],p['y'], p['z'],self.dobo.x, self.dobo.y, self.dobo.z)<6:
                            p['actif']=False
                            p['ch']=100
                        if p['ch']<=-50:
                            self.use[0]=True
                            if self.use[1]>=0:
                                self.use[1]-=1
                                p['actif']=False
                                p['ch']=100
                    if self.dobo.pressed['6'] and p['ch']>0:
                        p['ch']-=FPS
                        direc=4
                        for i in enemi:
                            di=dir(self.dobo.x,self.dobo.y,dcam,i.x, i.y)
                            if abs(di)<direc:
                                direc=abs(di)
                                cible=i
                        dist = ddis(p['x'],p['y'], p['z'],cible.x, cible.y, cible.z)
                        D, V = ddir(p['x'],p['y'], p['z'],0,0,cible.x, cible.y, cible.z)
                        Sp = ddis(0,0,0,p['v_x'],p['v_y'], p['v_z'])
                        x, y, z = avixyz(Sp, D, V)
                        dist = ddis(p['v_x'], p['v_y'], p['v_z'], x, y, z)
                        Di, Vi = ddir(p['v_x'],p['v_y'], p['v_z'], 0, 0, x*1.1, y*1.1, z*1.1)
                        x, y, z = avixyz(FPS*1.5, Di, Vi)
                        p['v_x']+=x
                        p['v_y']+=y
                        p['v_z']+=z
                    dist=100
                    for i in range(len(enemi)):
                        di=ddis(p['x'],p['y'], p['z'], enemi[i].x, enemi[i].y, enemi[i].z)
                        if dist>di:
                            dist=di
                            p['cible']=i
                    if p['cible']!=-1:
                        cible=enemi[p['cible']]
                        D, V=ddir(p['x'],p['y'], p['z'],0,0,cible.x, cible.y, cible.z)
                        if p['ch']>0:
                            p['ch']-=FPS
                            x, y, z = avixyz(FPS, D, V)
                            p['v_x']+=x
                            p['v_y']+=y
                            p['v_z']+=z
                        vi=ddis(0,0,0, p['v_x'], p['v_y'], p['v_z'])
                        dist=ddis(p['x'],p['y'], p['z'],cible.x, cible.y, cible.z)
                        do, vo= ddir(0,0,0,0,0, p['v_x'],p['v_y'], p['v_z']) 
                        if dist<6:
                            cible.aie(vi/40, vi/30, 0, 0,self)
                            cible.recul(vi/10, do,  vo)
                            while dist<6:
                                x, y, z = avixyz(-1, D, V)
                                p['x']+=x
                                p['y']+=y
                                p['z']+=z
                                dist=ddis(p['x'],p['y'], p['z'],cible.x, cible.y, cible.z)
                            x, y, z = avixyz(-vi*2, D, V)
                            p['v_x']+=x
                            p['v_y']+=y
                            p['v_z']+=z
        for i, p in enumerate(self.particules):
            pix=self.pixels[i]
            D=randint(-50,50)*pi/50
            V=randint(-50,50)*pi/50
            X,Y,Z=avixyz(FPS, D , V)
            p['v_x']=p['v_x']/(2**(FPS/10))+X
            p['v_y']=p['v_y']/(2**(FPS/10))+Y
            p['v_z']=p['v_z']/(2**(FPS/10))+Z
            p['x']+=p['v_x']*FPS
            p['y']+=p['v_y']*FPS
            p['z']+=p['v_z']*FPS
            if p['z']>0:
                p['z']=0
                p['v_z']=-abs(p['v_z'])
            if p['actif']:
                pix.x=p['x']
                pix.y=p['y']
                pix.z=p['z']
            else:
                pix.x=self.dobo.x
                pix.y=self.dobo.y
                pix.z=self.dobo.z
            
    def tele_1(self, pixels):
        self.help = self.dobo.armes[0]
        if self.help.charge==0:
            self.help.soul_1(pixels)
        self.charge=1
        self.force=0
        self.puissance=int(self.help.puissance/2)
        r=self.puissance
        self.pixels=[]
        for i in range(len(pixels)):
            if self.help.particules[i]['actif']:
                pass
            elif r>0:
                r-=1
                self.pixels=self.pixels+[i]
                self.help.particules[i]['actif']=True
        self.competence=self.tele_2

    def tele_2(self, enemi, FPS, dcam, vcam):
        if self.dobo.pressed['e']:
            if self.force<30:
                self.force+=FPS*2
            else:
                self.force=20
            for i in self.pixels:
                D=randint(-50,50)*pi/50
                V=randint(-50,50)*pi/50
                X,Y,Z=avixyz(self.force/10, D , V)
                self.help.particules[i]['x']=self.dobo.x+aviy(-5,-dcam)+X
                self.help.particules[i]['y']=self.dobo.y+avix(-5,-dcam)+Y
                self.help.particules[i]['z']=self.dobo.z+Z
        else:
            self.charge=0
            if self.force<5:
                for i in self.pixels:
                    p=self.help.particules[i]
                    D=randint(-50,50)*pi/50
                    V=randint(-50,50)*pi/50
                    p['v_x'],p['v_y'], p['v_z']=avixyz(10, D , V)
            else:
                for i in self.pixels:
                    p=self.help.particules[i]
                    D=randint(-20,30)*pi/300
                    V=randint(-25,25)*pi/300
                    p['v_x'],p['v_y'], p['v_z']=avixyz(self.force, dcam+D ,vcam+V)
                    
    def late_esp_1(self, pixels):
        self.charge = 1
        self.pixels = pixels
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
        self.avance = 0
        self.etat='solide'
        self.flui = 6
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = self.dobo.d + pi
        self.v = pi/2
        self.competence = self.late_esp_2

    def late_esp_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        if self.charge==1:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self._temp=create_trais(10,0,self.v,0,0,0)
            for i in range(len(self.pixels)):
                self.pixels[i].forme(self._temp[i][0]+9, self._temp[i][1], self._temp[i][2])
            if self.avance<0.5:
                self.d+=pi*(FPS/5)
                self.v-=2*pi*(FPS/5) 
            if self.avance>0.5:
                self.etat='solide'
                self.d = rot(pi*FPS,self.d)
                self.v += 3*pi*(FPS/5)
                di=35
                e=-1
                for i in range(len(enemi)):
                    if self.charge==1:
                        dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                        if di>=dist:
                            di=dist
                            e=i
                if e!=-1:
                    if -9<self.z-enemi[e].z<5:
                        direc=dir(self.x, self.y, -self.d, enemi[e].x, enemi[e].y)
                        if -pi*FPS*2<direc<=0:
                            enemi[e].aie(15,5,0,0,self.dobo)
                            enemi[e].recul(35,-self.d-pi/2,atan(3/5))
                            self.charge=2
                            
        if self.avance>0.7:
            self.charge=2
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            self.yoso.etat='liq'
            for i in range(len(self.pixels)):
                self.pixels[i].x = self.x
                self.pixels[i].y = self.y
                self.pixels[i].z = self.z
                self.pixels[i].item = self.yoso

        if self.avance>1:
            self.charge=0
            self.yoso.etat='solide'
    """
    def vague_1(self, pixels, dcam):
        if self.charge==0:
            self.pixels = pixels
            self.taille = pixels[1]-pixels[0]
            self.stun=0
            self.masse=1
            self.charge=1
            self.etat='liq'
            self.flui=0
            self.tx = self.dobo.x
            self.ty = self.dobo.y
            self.tz = self.dobo.z
            self.x = 0
            self.y = 0
            self.z = 0
            self.d = 0
            self.particules=[{'x':self.tx,'y':self.ty,'z':self.tz,'v':0,'t':randint(0,100), 'd':dcam+randint(-10,10)*pi/50, 'c':0}for i in range(self.taille)]
            self.forme=['aqua_point']+self.pixels+[points_fix(self.particules)]
            self.competence = self.vague_2
            
    def vague_2(self,enemi, FPS, dcam, vcam):
        if self.dobo.pressed[6]:
            self.tx = self.dobo.x
            self.ty = self.dobo.y
            self.tz = self.dobo.z
            for i, par in enumerate(self.particules):
                X,Y,Z=avixyz((110-par['t'])*FPS/4, par['d'], par['v'])
                par['x']+=X
                par['y']+=Y
                par['z']+=Z
                par['d']=rot(randint(-10,10)*FPS*pi/30,par['d'])
                par['v']=rot(randint(-10,10)*FPS*pi/200,par['v'])
                if par['t']>=100:
                    self.particules[i] = {'x':self.tx,'y':self.ty,'z':self.tz,'v':0,'t':0, 'd':dcam+randint(-10,10)*pi/50, 'c':0}
                par['t']+=FPS*randint(25,30)
                if par['c']==0:
                    for r in enemi:
                        if r!=self.dobo:
                            dist = ddis(par['x'], par['y'], par['z'], r.x, r.y, r.z)
                            if dist<6:
                                r.aie(0.6,0.5, 0, 0,self)
                                r.recul(2, par['d'], par['v'])
                                par['c']=1
                if par['c']==1:
                    par['x'] = self.tx
                    par['y'] = self.ty
                    par['z'] = self.tz
        else:
            let=True
            self.tx = self.dobo.x
            self.ty = self.dobo.y
            self.tz = self.dobo.z
            for i, par in enumerate(self.particules):
                X,Y,Z=avixyz((110-par['t'])*FPS/4, par['d'], par['v'])
                par['x']+=X
                par['y']+=Y
                par['z']+=Z
                par['d']=rot(randint(-10,10)*FPS*pi/30,par['d'])
                par['v']=rot(randint(-10,10)*FPS*pi/200,par['v'])
                if par['t']>=100:
                    self.particules[i] = {'x':self.tx,'y':self.ty,'z':self.tz,'v':0,'t':101, 'd':0, 'c':1}
                else:
                    let=False
                par['t']+=FPS*randint(25,50)
                if self.particules[i]['c']==0:
                    for r in enemi:
                        if r!=self.dobo:
                            dist = ddis(par['x'], par['y'], par['z'], r.x, r.y, r.z)
                            if dist<6:
                                r.aie(0.6,0.5, 0, 0,self)
                                r.recul(2,par['d'],par['v'])
                                par['c']=1
                if par['c']==1:
                    par['x'] = self.tx
                    par['y'] = self.ty
                    par['z'] = self.tz
            if let:
                self.charge=0
        self.forme=['aqua_point']+self.pixels+[points_fix(self.particules)]
        
    def bule_1(self, pixels, dcam, vcam):
        if self.charge==0:
            self.pixels = pixels
            self.taille = pixels[1]-pixels[0]
            self.stun=0
            self.avance=0
            self.masse=1
            self.charge=1
            self.etat='solide'
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = dcam
            self.v = vcam
            self.l_z=-10
            X,Y,Z = avixyz(10, dcam, vcam)
            self.x+=X
            self.y+=Y
            self.z+=Z
            self.forme=['boule_eau']+self.pixels+['']
            self.particules=[{'x':0,'y':0,'z':0,'v':0, 'd':0, 'v_z':0, 't':randint(5,10)}for i in range(self.taille)]
            for i in range(len(self.particules)):
                d=randint(-100,100)*pi/100
                v=randint(-100,100)*pi/100
                self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z']=avixyz(sqrt(randint(25,8100)), d, v)
            self.competence = self.bule_2

    def bule_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        stop=True
        if self.charge==1:
            stop=False
            self.forme = ['boule_eau']+self.pixels+['']
        if self.charge==3:
            for i, par in enumerate(self.particules):
                if self.particules[i]['t']>0:
                    self.particules[i]['x']+=0
                    self.particules[i]['y']+=0
                    self.particules[i]['z']+=self.particules[i]['v_z']*FPS*5
                    self.particules[i]['v_z']+=FPS*5
                    if self.particules[i]['z']>0:
                        self.particules[i]['z']=0
                    self.particules[i]['t']-=FPS*3
                    stop=False
                else:
                    par['x'] = self.dobo.x
                    par['y'] = self.dobo.y
                    par['z'] = self.dobo.z
            self.forme = ['aqua_point']+self.pixels+[points_fix(self.particules)]
        
        if self.charge==4:
            self.charge=0
            stop=False
        
        if stop:
            self.charge=4
        
        if self.charge==1:
            if self.avance>1.2 or self.z>=0:
                self.charge=2
            X,Y,Z= avixyz(50*FPS, self.d,self.v)
            self.x += X
            self.y += Y
            self.z += Z+(self.l_z*FPS)
            self.l_z +=FPS*5
            for a in range(20):
                if self.charge==1:
                    X,Y,Z= avixyz(-a*5, self.d,self.v)
                    X+=self.x
                    Y+=self.y
                    Z+=self.z+self.l_z*FPS/20
                    for adv in enemi:
                        if self.charge==1 and adv!=self.dobo:
                            dist=ddis(X, Y, Z, adv.x, adv.y, adv.z)
                            if dist<10:
                                adv.aie(12,6,0,0,self.dobo)
                                adv.recul(20,self.d,self.v)
                                self.charge=2
        if self.charge==2:
            for i in range(len(enemi)):
                if enemi[i]!=self.dobo:
                    dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                    if dist<80:
                        enemi[i].aie(5,4,0,0,self)
                        D,V=ddir(self.x, self.y, self.z, 0, 0,enemi[i].x, enemi[i].y, enemi[i].z)
                        enemi[i].recul(20,D,V)
            self.tx = self.x
            self.ty = self.y
            self.tz = self.z
            self.x = 0
            self.y = 0
            self.z = 0
            self.d = 0
            for par in self.particules:
                par['x']+=self.tx
                par['y']+=self.ty
                par['z']+=self.tz
            self.forme = ['aqua_point']+self.pixels+[points_fix(self.particules)]
            
            self.charge=3
    
    def frape_1(self, pixels):
        if self.charge==0:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            self.pixels = pixels
            self.charge = 1
            self.tim = 0
            self.avance2=0
            self.forme=['terbaston']+self.pixels+[self.yoso.forme[3]+'(0(0']
            self.competence= self.frape_2

    def frape_2(self, enemi, FPS, dcam, vcam):
        self.syncro(self.dobo)
        self.tim+=FPS
        if self.tim<0.5:
            self.dobo.avance(10*self.dobo.boost,FPS)
            X = self.x+(avix(self.tim*20,self.d)+aviy(5,self.d))
            Y = self.y+(avix(self.tim*20,self.d+pi/2)+aviy(5,self.d+pi/2))
            Z = self.z
            for i in enemi:
                dist=ddis(X, Y, Z, i.x, i.y, i.z)
                if dist<9 and i!=self.dobo:
                    i.aie(8*self.dobo.boost, 3, 0, 0, self.dobo)
                    i.recul(8,-self.d,0)
        elif self.tim<1:
            if self.dobo.pressed[6] and self.charge==1:
                self.charge=2
                self.avance2=0
        else:
            if self.charge!=2:
                self.charge=0
        if self.charge==2:
            self.avance2+=FPS
            if self.avance2<0.5:
                self.dobo.avance(10*self.dobo.boost,FPS)
                X = self.x+(avix(self.avance2*20,self.d)+aviy(-5,self.d))
                Y = self.y+(avix(self.avance2*20,self.d+pi/2)+aviy(-5,self.d+pi/2))
                Z = self.z
                for i in enemi:
                    dist=ddis(X, Y, Z, i.x, i.y, i.z)
                    if dist<9 and i!=self.dobo:
                        i.aie(8*self.dobo.boost, 3, 0, 0, self.dobo)
                        i.recul(8,-self.d,0)
            elif self.avance2>=1:
                self.charge=0
        _t1=str(int(self.tim*100)/100)
        _t2=str(int(self.avance2*100)/100)
        self.forme=['terbaston']+self.pixels+[self.yoso.forme[3]+'('+_t1+'('+_t2]

    def shoot_1(self, arme2):
        if self.charge==0:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.arme2 = arme2
            self.d = 0
            self.pixels = self.yoso.pixels
            self.forme = ['terratape',self.pixels[0], self.pixels[0]+33, self.yoso.forme[3]+'(0']
            self.charge = 1
            self.tim = 0
            self.competence = self.shoot_2

    def shoot_2(self, enemi, FPS, dcam, vcam):
        self.tim += FPS/5
        self.syncro(self.dobo)
        if  self.dobo.stun>10:
            self.competence=self.stop
        if self.tim>0.6:
            if self.charge==1:
                self.arme2.zone1([self.pixels[0]+33, self.pixels[1]])
                self.charge=2
                self.x = self.dobo.x
                self.y = self.dobo.y
                self.z = 0
                self.v_z = 0
                self.d = randint(-100,100)*pi/100
                for i in enemi:
                    if i!=self.dobo:
                        dist=dis(self.x, self.y, i.x, i.y)
                        if dist<90 and i.z>-7.6:
                            i.aie(-((self.dobo.z+5+abs(self.dobo.v_z))*0.7)*self.dobo.boost, 0, 0, 0, self.dobo)
                            i.stun+=20
                            i.recul(16,dir(self.x,self.y,0,i.x,i.y),0)
                            i.v_z=-2
                self.dobo.z=-7
        if self.tim>1:
            self.charge=0
        self.forme[3]= self.yoso.forme[3]+'('+str(int(self.tim*100)/100)
    
    def zone1(self, pixels):
        self.pixels=pixels
        self.syncro(self.dobo)
        self.z=0
        self.charge=1
        self.tim=0
        self.forme=['terrazone']+self.pixels+['']
        self.competence = self.zone2
    
    def zone2(self, enemi, FPS, dcam, vcam):
        self.tim+=FPS/5
        if self.tim>0.4:
            self.competence = self.stop

