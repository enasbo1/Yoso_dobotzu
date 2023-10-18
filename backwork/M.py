from backwork.Item import*
from keyboard import is_pressed

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
    def __init__(self, x, y, z, color,d, ):
        self.x = x
        self.y = y
        self.z = z
        self.flui=3
        self.chute=True
        self.vie=100
        self.stun=0
        self.boost=1
        self.mort=0
        self.electrique=0
        self.temperature=0
        self.resistance=0
        self.chield=0
        self.man=True
        self.armor=True
        self.etourdi=0
        self.pressed={'space':False,'8':False, '5':False, '6':False, '4':False, 'e':False, 'a':False, 'z':False, 'q':False, 's':False, 'd':False, '0':False}
        self.touchable=1
        self.element='none'
        self.etat='solide'
        self.color = color
        self.masse=1
        self.mun = 0
        self.retard=[-1,-1]
        if self.color=='grey10':
            self.tetzu(d)
        else:
            self.dobotzu(d)
        self.arme=[Arme(self,self.yoso)for i in range(10)]
        self.etoile=Etoile(self, [self.pixels[i+115]for i in range(15)])
    
    def tour(self,FPS):
        if self.type == 'yoso':
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
        if self.type == 'dobo':
            dist=ddis(0,0,0,self.x, self.y, self.z)
            if dist>750:
                D, V = ddir(0,0,0,0,0,self.x, self.y, self.z)
                while dist>750:
                    X,Y,Z=avixyz(-1, D, V)
                    self.x += X
                    self.y += Y
                    self.z += Z
                    dist=ddis(0,0,0,self.x, self.y, self.z)
            self.pressed={'space':False,'8':False, '5':False, '6':False, '4':False, 'e':False, 'a':False, 'z':False, 'q':False, 's':False, 'd':False, '0':False}
            for a in range(115):
                if a==51 or a==64:
                    self.pixels[a].color='black'
                else:
                    self.pixels[a].color=self.color
            if self.armor and self.yoso.element=='terre':
                for i in range(50):
                    a=((i*11)+15)%115
                    self.pixels[a].color='saddle brown'
            if self.electrique!=0:
                self.stun+=abs(self.electrique*FPS/5)
                charge=abs(int(self.electrique))
                if self.electrique<0:
                    color='goldenrod'
                if self.electrique>0:
                    color='turquoise2'
                for i in range(charge):
                    a=randint(0,115)
                    self.pixels[a].color=color
            if self.temperature>0:
                self.chield-=self.temperature*FPS/40
                self.temperature=self.temperature/(2**(FPS/25))
                for i in range(50):
                    a=((i*12)+30)%115
                    if i<self.temperature-1:
                        self.pixels[a].color='firebrick4'
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
            for i in range(len(self.coo)):
                self.coo[i]-=FPS
    
    def avance(self, vi, FPS):
        if self.stun<10:
            self.x += avix((vi*FPS)/self.masse, self.d)
            self.y += aviy(-(vi*FPS)/self.masse, self.d)
    
    def test(self, FPS , Edobo, Mdobo):
        reponseE=False
        reponseA=False
        reponse8=False
        if self.stun<10:
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=4
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.retard[0]<-4:
                        reponseE=True
                Mcout=0
                Ecout=2
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if  self.coo[2]<0:
                        reponseA=True
                Mcout=0
                Ecout=4
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0:
                        reponse8=True
            if self.yoso.element=='espris':
                Mcout=0
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0:
                        reponseE=True
                Mcout=0
                Ecout=3
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[2].charge==0 :
                        reponseA=True
            if self.yoso.element=='eau':
                Mcout=FPS/2
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    reponseA=True
                Mcout=7
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0 and self.coo[2]<0:
                        reponseE=True
                reponse8=True
            if self.yoso.element=='feux':
                Mcout=FPS/2
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    reponseA=True
                Mcout=7
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0 and self.coo[2]<0:
                        reponseE=True
                reponse8=True
                if self.arme[2].charge==2:
                    reponse8=False

            if self.yoso.element=='ombre':
                Mcout=5
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[1]<0 :
                        if self.arme[0]:
                            reponseE=True
                Mcout=3
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        if self.arme[0]:
                            reponseA=True

                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        if self.arme[0].charge==0 and not self.pressed['space']:
                            reponse8=True
            if self.yoso.element=='foudre':
                if self.pressed['space']:
                    Mcout=3
                    Ecout=0
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[1]<0 :
                            reponseE=True
                else:
                    Mcout=4
                    Ecout=0
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[1]<0 :
                            reponseE=True
                Mcout=1
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        e=False
                        for i in range(3):
                            if self.arme[i].charge==0:
                                e=True
                        if e:
                            reponseA=True
                Mcout=5
                Ecout=10
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[3]<0 :
                        reponse8=True
            if self.yoso.element=='fer':
                if self.pressed['space']:
                    Mcout=1
                    Ecout=3
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[1]<0 :
                            reponseE=True
                else:
                    Mcout=1
                    Ecout=3
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[2]<0 :
                            reponseE=True
                Mcout=0
                Ecout=3
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        if self.arme[0].charge==0:
                            reponseA=True
                Mcout=5
                Ecout=2
                if self.arme[1].charge==0 and self.coo[3]<0:
                    reponse8=True
        if self.pressed['a']:
            reponseA=False
        if self.pressed['e']:
            reponseE=False
        if self.pressed['8']:
            reponse8=False
        return(reponseE,reponseA,reponse8)
    

    def competence_e(self, FPS, Edobo, Mdobo, enemi, dcam, vcam):
        if self.stun<10:
            self.pressed['e']=True
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=4
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.retard[0]<-4:
                        self.boost=1.5
                        self.retard[0]=1
                        Edobo-=Ecout
            if self.yoso.element=='espris':
                Mcout=0
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0:
                        self.arme[1].tele_1([self.yoso.pixels[i]for i in range(100)])
                        Mdobo-=Mcout
            if self.yoso.element=='eau':
                Mcout=7
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0 and self.coo[2]<0:
                        self.arme[1].bule_1([self.yoso.pixels[91+i]for i in range(24)],dcam, vcam)
                        self.coo[2]=10
                        Mdobo-=Mcout
                        Edobo-=Ecout
            if self.yoso.element=='feux':
                Mcout=7
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0 and self.coo[2]<0:
                        self.arme[1].brule_1([self.yoso.pixels[91+i]for i in range(24)],dcam, vcam)
                        self.coo[2]=10
                        Mdobo-=Mcout
                        Edobo-=Ecout
            if self.yoso.element=='ombre':
                Mcout=5
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[1]<0 :
                        if self.arme[0]:
                            self.arme[0].atrac_ombre_1([self.yoso.pixels[114-i]for i in range(115)])
                            self.coo[1]=25
                            Mdobo-=Mcout
                            Edobo-=Ecout
            if self.yoso.element=='foudre':
                if self.pressed['space']:
                    Mcout=3
                    Ecout=0
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[1]<0 :
                            charge=1
                            x0,y0,z0 = 0,0,0
                            for i in range(35):
                                self.yoso.pixels[i].x+=x0+randint(-10,10)
                                self.yoso.pixels[i].y-=y0+randint(-10,10)
                                self.yoso.pixels[i].z+=z0+randint(-10,10)
                                x1,y1,z1 = avixyz(60/35,self.d,-pi/2)
                                x0=x0+x1
                                y0=y0+y1
                                z0=z0+z1
                            for a in range(12):
                                if charge==1:
                                    X=self.x
                                    Y=self.y
                                    Z=self.z-a*5
                                    for i in range(len(enemi)):
                                        if charge==1:
                                            dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                                            if dist<50:
                                                enemi[i].aie(3,5,0,-9,self)
                                                charge=2
                            self.z-=60/self.masse
                            self.coo[1]=1
                            Mdobo-=Mcout
                            Edobo-=Ecout
                else:
                    Mcout=4
                    Ecout=0
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[1]<0 :
                            x0,y0,z0 = 0,0,0
                            charge=1
                            for i in range(35):
                                self.yoso.pixels[i].x+=x0+randint(-10,10)
                                self.yoso.pixels[i].y-=y0+randint(-10,10)
                                self.yoso.pixels[i].z+=z0+randint(-10,10)
                                x1,y1,z1 = avixyz(80/35,self.d,0)
                                x0=x0+x1
                                y0=y0+y1
                                z0=z0+z1
                            for a in range(33):
                                if charge==1:
                                    X,Y,Z= avixyz(a*2.5, self.d,0)
                                    X+=self.x
                                    Y+=self.y
                                    Z=self.z
                                    for i in range(len(enemi)):
                                        if charge==1:
                                            dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                                            if dist<40:
                                                enemi[i].aie(3,5,0,-8,self)
                                                charge=2
                            self.x += avix(80/self.masse, self.d)
                            self.y += aviy(-80/self.masse, self.d)
                            self.coo[1]=1
                            Mdobo-=Mcout
                            Edobo-=Ecout
            if self.yoso.element=='fer':
                if self.pressed['space']:
                    Mcout=1
                    Ecout=3
                    if Edobo>=Ecout and Mdobo>=Mcout:
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
                            Mdobo-=Mcout
                            Edobo-=Ecout
                else:
                    Mcout=1
                    Ecout=3
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        if self.coo[2]<0 :
                            x0,y0,z0 = 0,0,0
                            charge=1
                            if self.arme[0].charge==0:
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
                                Mdobo-=Mcout
                                Edobo-=Ecout
                                self.arme[0].ai_1([self.yoso.pixels[i]for i in range(100)])                                    
        return(Edobo, Mdobo)

    def competence_a(self, FPS, Edobo, Mdobo, enemi, dcam, vcam):
        if self.stun<10:
            self.pressed['a']=True
            if self.yoso.element=='eau':
                Mcout=FPS/2
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[0].charge==0:
                        self.arme[0].vague_1([self.yoso.pixels[41+i]for i in range(50)])
                    Mdobo-=Mcout
                    Edobo-=Ecout
            if self.yoso.element=='feux':
                Mcout=FPS/2
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[0].charge==0:
                        self.arme[0].flame_1([self.yoso.pixels[41+i]for i in range(50)])
                    Mdobo-=Mcout
                    Edobo-=Ecout
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=2
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if  self.coo[2]<0:
                        self.arme[1].frape_1([self.yoso.pixels[i]for i in range(16)])
                        self.coo[2]=1
                        Mdobo-=Mcout
                        Edobo-=Ecout
            if self.yoso.element=='ombre':
                Mcout=3
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        if self.arme[0]:
                            self.arme[0].lance_ombre_1([self.yoso.pixels[114-i]for i in range(115)])
                            self.coo[2]=5
                            Mdobo-=Mcout
                            Edobo-=Ecout
            if self.yoso.element=='foudre':
                Mcout=1
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        e=-1
                        for i in range(3):
                            if self.arme[i].charge==0:
                                e=i
                        if e!=-1:
                            self.arme[e].tir_foudre_1([self.yoso.pixels[114-((e*4)+i)]for i in range(4)], dcam, vcam)
                            self.coo[2]=0.5
                            Mdobo-=Mcout
                            Edobo-=Ecout    
            if self.yoso.element=='espris':
                Mcout=0
                Ecout=3
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[2].charge==0 :
                        self.arme[2].late_esp_1([self.yoso.pixels[100+i]for i in range(10)])
                        self.coo[2]=1.5
                        Mdobo-=Mcout
                        Edobo-=Ecout
            if self.yoso.element=='fer':
                Mcout=0
                Ecout=3
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[2]<0 :
                        e=-1
                        for i in range(1):
                            if self.arme[i].charge==0:
                                e=i
                        if e!=-1:
                            self.arme[e].late_fer_1([self.yoso.pixels[i]for i in range(58)])
                            self.coo[2]=1.5
                            Mdobo-=Mcout
                            Edobo-=Ecout
        return(Edobo, Mdobo)
    
    def competence_8(self, FPS, Edobo, Mdobo, enemi, dcam, vcam):
        if self.stun<10:
            if self.man:
                self.pressed['8']=True
            else:
                self.man=True
            if self.yoso.element=='feux':
                Mcout=FPS
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    self.arme[2].pyro_1([])
                    self.arme[2].goold=True
                    Mdobo-=Mcout
                    Edobo-=Ecout
            if self.yoso.element=='eau':
                Mcout=FPS
                Ecout=-FPS
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.vie<=100-FPS:
                        self.vie+=FPS
                    else:
                        Mcout-=3*FPS/4
                    if Edobo>40-FPS:
                        Mcout-=FPS/4
                        Ecout=0
                    Mdobo-=Mcout
                    Edobo-=Ecout
            if self.yoso.element=='ombre':
                Mcout=3
                Ecout=0
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[0].charge==0 and not self.pressed['space']:
                        self.retard[0]=0.5
                        self.arme[0].ombre_1([self.yoso.pixels[i]for i in range(115)])
                        self.arme[0].good=True
                        Mdobo-=Mcout
                        Edobo-=Ecout
            if self.yoso.element=='foudre':
                Mcout=5
                Ecout=10
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.coo[3]<0 :
                        self.retard[0]=0.5
                        self.coo[3]=20
            if self.yoso.element=='terre':
                Mcout=0
                Ecout=4
                if Edobo>=Ecout and Mdobo>=Mcout:
                    if self.arme[1].charge==0:
                        self.arme[1].shoot_1([self.yoso.pixels[i]for i in range(115)])
                        Mdobo-=Mcout
                        Edobo-=Ecout
            if self.yoso.element=='fer':
                Mcout=5
                Ecout=2
                if self.arme[1].charge==0 and self.coo[3]<0:
                    self.arme[1].armure_1([self.yoso.pixels[114-i]for i in range(30)])
                    Mdobo-=Mcout
                    Edobo-=Ecout
                if self.arme[1].charge!=0:
                    Mdobo-=FPS
        if Mdobo<=0:
            self.man=False
        return(Edobo, Mdobo)
    
    def saut(self, Edobo):
        if self.stun<10:
            self.pressed['space']=True
            if Edobo>=3 and self.yoso.element!='ombre':
                if self.z>-7.6 and self.coo[0]<0:
                    self.v_z=-2/self.masse
                    self.coo[0]=3
                    Edobo-=3
        return(Edobo)

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
                if self.arme[1].charge==1:
                    if self.arme[1].competence==self.arme[1].armure_2 and self.arme[1].avance<0.3:
                        enemi.stun+=14
    
    def recul(self, vi, D,  V):
        x,y,z=avixyz(vi*self.touchable, D, V,)
        self.x+=x
        self.y+=y
        self.z+=z
        
    def passif(self, FPS, Edobo, Mdobo, enemi, dcam, vcam):
        if Mdobo<0:
            Mdobo=0
        for i in range(len(enemi)):
            dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
            if dist<12 and self.touchable>0 and enemi[i].touchable>0:
                D, V = ddir(self.x, self.y, self.z, 0, 0, enemi[i].x, enemi[i].y, enemi[i].z)
                while dist<12:
                    X,Y,Z=avixyz(1,D,V)
                    enemi[i].x+=X
                    enemi[i].y+=Y
                    enemi[i].z+=Z
                    dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
        for i in range(len(self.arme)):
            if self.arme[i].charge!=0:
                self.arme[i].tour(enemi, FPS, dcam, vcam)
        for i in range(len(self.retard)):
            if self.retard[i]!=5:
                self.retard[i]-=FPS/5
        self.etoile.tour(FPS)
        self.yoso.tour(FPS)
        if self.yoso.element=='terre':
            if self.retard[0]<0:
                self.boost=1
            else:
                for i in range(33):
                    self.yoso.pixels[i].color='grey12'
            if self.armor:
                if Mdobo<20:
                    Edobo+=2*FPS/5
                Mdobo+=self.chield*2
                self.touchable=0.5
                if Mdobo<0:
                    self.armor=False
                    self.vie+=Mdobo
                    Mdobo=0
            else:
                Edobo+=FPS
                self.touchable=1
                self.vie+=self.chield
                if Mdobo>10:
                    self.armor=True
        else:
            self.vie+=self.chield

        self.chield=0
        if self.yoso.element=='espris':
            if self.arme[0].charge!=0:
                man=self.arme[0].puissance
            else:
                man=100
            Mdobo=man/5
            if Mdobo<=20-FPS/5:
                Edobo+=2*FPS/5
        if self.stun<10:
            if self.yoso.element=='ombre':
                if self.pressed['space']:
                    Mcout=3*FPS/5
                    Ecout=0
                    if Edobo>=Ecout and Mdobo>=Mcout:
                        self.z=7
                        self.chute=False
                        self.v_z=-0.5
                        self.touchable=0
                        Mdobo-=Mcout
                        Edobo-=Ecout
                else:
                    self.touchable=1
                    self.chute=True
        else:
            if self.stun>20:
                self.stun=20
        if self.yoso.element=='foudre':
            if self.retard[0]!=5 and self.retard[0]<0:
                Mcout=5
                Ecout=10
                self.retard[0]=5
                if Edobo>=Ecout and Mdobo>=Mcout:
                    x0,y0,z0 = 0,0,0
                    for i in range(35):
                        self.yoso.pixels[i].x=self.x+x0
                        self.yoso.pixels[i].y=self.y+y0
                        self.yoso.pixels[i].z=self.z+z0+randint(-10,10)
                        x0,y0,z0 = avixyz(randint(10,80),randint(-20,20)*(pi/20),0)
                    for i in range(len(enemi)):
                        dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                        if dist<80:
                            enemi[i].aie(3,12,0,-10,self)
                    Mdobo-=Mcout
                    Edobo-=Ecout
        if self.yoso.element=='fer':
            Mdobo-=self.arme[0].Mcout
            self.arme[0].Mcout=0
        return(Edobo, Mdobo)

    def comportement(self, enemi, FPS, dcam, vcam, xcam, ycam, zcam, x, y, toile):
        di=1000
        e=-1
        if self.yoso.element=='none':
            for i in self.arme:
                if i.chat==1:
                    i.degat_2(x,y,xcam,ycam,zcam, dcam, vcam, FPS)
            if self.chield<=-1:
                self.vie+=self.chield
                self.arme[self.mun].degats(self.chield,toile)
                self.mun=(self.mun+1)%len(self.arme)
                self.chield=0
        else:
            self.vie+=self.chield
            self.chield=0
        for i in range(len(enemi)):
            dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
            if enemi[i]!=self:
                if dist<12 and self.touchable>0 and enemi[i].touchable>0:
                    D, V = ddir(self.x, self.y, self.z, 0, 0, enemi[i].x, enemi[i].y, enemi[i].z)
                    while dist<12:
                        X,Y,Z=avixyz(1,D,V)
                        enemi[i].x+=X
                        enemi[i].y+=Y
                        enemi[i].z+=Z
                        dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
        for i in range(len(self.retard)):
            if self.retard[i]!=-1:
                self.retard[i]-=FPS/5
        D,V=ddir(self.x, self.y, self.z, 0, 0, enemi[0].x, enemi[0].y, enemi[0].z)
        di=ddis(self.x, self.y, self.z, enemi[0].x, enemi[0].y, enemi[0].z)
        if self.yoso.element=='fer':
            self.d = tourne(self.d, -D, FPS/2)
            if V<-pi/8:
                r=self.saut(5)
            if di<30:
                r=self.competence_a(FPS, 5, 5, enemi, 0, 0)
            else:
                r=self.avance(5,FPS)
        if self.yoso.element=='none':
            De,Ve=ddir(self.x, self.y, self.z, 0, 0, 200, 0, 0)
            die=dis(self.x, self.y, 200, 0)
            di=ddis(-200, 0, 0, enemi[0].x, enemi[0].y, enemi[0].z)
            if di<25:
                enemi[0].aie(FPS/2, FPS/2, [50, FPS/20], -5, self)
            if die>=5:
                self.avance(5,FPS)
                self.d = tourne(self.d, -De, FPS/2)
            else:
                self.d = tourne(self.d, -D, FPS/2)
            if die<=20:
                self.recul(FPS, De, Ve)
                if self.vie<=100-FPS:
                    self.vie+=FPS
                else:
                    self.vie=100
        if self.yoso.element=='espris':
            self.d = tourne(self.d, -D, FPS/2)
            if V<-pi/8:
                r=self.saut(7)
            if di<30:
                r=self.competence_a(FPS, 5, 5, enemi, 0, 0)
            else:
                r=self.avance(7,FPS)
            if self.retard[0]<0:
                r=self.competence_e(FPS, 10, 10, enemi, 0, 0)
                self.retard[0]=12
            if self.stun<10:
                self.pressed['6']=True
        for i in range(len(self.arme)):
            if self.arme[i].charge!=0:
                self.arme[i].tour([enemi[0]], FPS, self.d, 0)
        self.etoile.tour(FPS)
        self.yoso.tour(FPS)
        self.tour(FPS)

        
class Arme(Dobotzu):
    def __init__(self, dobo, yoso):
         self.dobo = dobo
         self.yoso = yoso
         self.x = self.dobo.x
         self.y = self.dobo.y
         self.z = self.dobo.z
         self.d = self.dobo.d
         self.chat = 0
         self.feel = 0
         self.Mcout = 0
         self.etat='solide'
         self.type='arme'
         self.charge = 0
    
    def tir_foudre_1(self, pixels, dcam, vcam):
        self.charge = 1
        self.pixels = pixels
        for i in range(len(self.pixels)):
            self.pixels[i].item=self
        self.avance = 0
        self.etat='solide'
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = dcam
        self.v = vcam
        self.competence = self.tir_foudre_2

    def tir_foudre_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        if self.charge==1:
            X,Y,Z= avixyz(100*FPS, self.d,self.v)
            self.x += X
            self.y += Y
            self.z += Z
            for i in range(len(self.pixels)):
                self.pixels[i].forme(-i,0,0)
            for a in range(20):
                if self.charge==1:
                    X,Y,Z= avixyz(-a*5, self.d,self.v)
                    X+=self.x
                    Y+=self.y
                    Z+=self.z
                    for i in range(len(enemi)):
                        if self.charge==1:
                            dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                            if dist<10:
                                enemi[i].aie(1,1,0,3,self.dobo)
                                self.charge=2
        if self.avance>0.75:
            self.charge=0
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            for i in range(len(self.pixels)):
                self.pixels[i].x=self.x
                self.pixels[i].y=self.y
                self.pixels[i].z=self.z
                self.pixels[i].item = self.yoso
        if self.charge==2:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            for i in range(len(self.pixels)):
                self.pixels[i].x=self.x
                self.pixels[i].y=self.y
                self.pixels[i].z=self.z
                self.pixels[i].item = self.yoso
    
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
    
    def flame_1(self, pixels):
        if self.charge==0:
            self.pixels = pixels
            self.stun=0
            self.masse=1
            self.charge=1
            self.etat='liq'
            self.flui=0
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            for i in range(len(self.pixels)):
                self.pixels[i].item=self
            self.particules=[{'x':self.x,'y':self.y,'z':self.z,'v':0,'t':randint(0,100), 'd':0, 'c':0}for i in range(len(self.pixels))]
            self.competence = self.flame_2
            
    def flame_2(self,enemi, FPS, dcam, vcam):
        if self.dobo.pressed['a']:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = dcam
            for i in range(len(self.pixels)):
                X,Y,Z=avixyz((100-self.particules[i]['t'])*FPS/4, self.particules[i]['d']+self.d, -(self.particules[i]['t']/(pi*100))+self.particules[i]['v'])
                self.particules[i]['x']+=X
                self.particules[i]['y']+=Y
                self.particules[i]['z']+=Z
                self.particules[i]['d']=rot(randint(-10,10)*FPS*pi/50,self.particules[i]['d'])
                self.particules[i]['v']=rot(randint(-10,10)*FPS*pi/50,self.particules[i]['v'])
                if self.particules[i]['t']>=100:
                    self.particules[i] = {'x':self.x,'y':self.y,'z':self.z,'v':0,'t':0, 'd':0, 'c':0}
                self.particules[i]['t']+=FPS*randint(25,50)
                if self.particules[i]['c']==0:
                    for r in enemi:
                        dist = ddis(self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z'], r.x, r.y, r.z)
                        if dist<6:
                            r.aie(FPS/5,FPS/10, [50,FPS/50], 0,self)
                            self.particules[i]['c']=1
            for i in range(len(self.pixels)):
                if self.particules[i]['c']==0:
                    self.pixels[i].x = self.particules[i]['x']+randint(-2,3)
                    self.pixels[i].y = self.particules[i]['y']+randint(-2,3)
                    self.pixels[i].z = self.particules[i]['z']+randint(-2,3)
                else:
                    self.pixels[i].x=self.x
                    self.pixels[i].y=self.y
                    self.pixels[i].z=self.z
        else:
            let=True
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            for i in range(len(self.pixels)):
                X,Y,Z=avixyz((100-self.particules[i]['t'])*FPS/4, self.particules[i]['d']+self.d, -(self.particules[i]['t']/(pi*100))+self.particules[i]['v'])
                self.particules[i]['x']+=X
                self.particules[i]['y']+=Y
                self.particules[i]['z']+=Z
                self.particules[i]['d']=rot(randint(-10,10)*FPS*pi/50,self.particules[i]['d'])
                self.particules[i]['v']=rot(randint(-10,10)*FPS*pi/50,self.particules[i]['v'])
                if self.particules[i]['t']>=100:
                    self.particules[i] = {'x':self.x,'y':self.y,'z':self.z,'v':0,'t':101, 'd':0, 'c':0}
                else:
                    let=False
                self.particules[i]['t']+=FPS*randint(25,50)
                if self.particules[i]['c']==0:
                    for r in enemi:
                        dist = ddis(self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z'], r.x, r.y, r.z)
                        if dist<6:
                            r.aie(0.1,0.05, [50,FPS/50], 0,self)
                            self.particules[i]['c']=1
            for i in range(len(self.pixels)):
                if self.particules[i]['c']==0:
                    self.pixels[i].x = self.particules[i]['x']+randint(-2,3)
                    self.pixels[i].y = self.particules[i]['y']+randint(-2,3)
                    self.pixels[i].z = self.particules[i]['z']+randint(-2,3)
                else:
                    self.pixels[i].x=self.x
                    self.pixels[i].y=self.y
                    self.pixels[i].z=self.z
            if let:
                self.charge=0
                for i in self.pixels:
                    i.item = self.yoso
                    i.x=self.x
                    i.y=self.y
                    i.z=self.z
    
    def brule_1(self, pixels, dcam, vcam):
        if self.charge==0:
            self.pixels = pixels
            self.stun=0
            self.avance=0
            self.masse=1
            self.charge=1
            self.etat='solide'
            self.flui=0
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = dcam
            self.v = vcam
            X,Y,Z = avixyz(10, dcam, vcam)
            self.x+=X
            self.y+=Y
            self.z+=Z
            for i in range(len(self.pixels)):
                self.pixels[i].item=self
            self.particules=[{'x':0,'y':0,'z':0,'v':0, 'd':0, 't':randint(5,10)}for i in range(len(self.pixels))]
            for i in range(len(self.particules)):
                d=randint(-100,100)*pi/100
                v=randint(-100,100)*pi/100
                self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z']=avixyz(randint(5,60), d, v)
            self.competence = self.brule_2

    def brule_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        stop=True
        for i, r in enumerate(self.pixels):
            if self.charge==1:
                r.forme(randint(-2,3),randint(-2,3),randint(-2,3))
                stop=False
            elif self.particules[i]['t']>0:
                r.forme(self.particules[i]['x'],self.particules[i]['y'],self.particules[i]['z'])
                self.particules[i]['x']+=randint(-2,3)*FPS
                self.particules[i]['y']+=randint(-2,3)*FPS
                self.particules[i]['z']+=randint(-2,3)*FPS
                if self.particules[i]['z']+self.z>0:
                    self.particules[i]['z']=-self.z
                self.particules[i]['t']-=FPS*3
                stop=False
            else:
                r.x=self.yoso.x
                r.y=self.yoso.y
                r.z=self.yoso.z
                r.item = self.yoso
        if stop:
            self.charge=0
        if self.charge==1:
            if self.avance>1.2 or self.z>=0:
                self.charge=2
            X,Y,Z= avixyz(50*FPS, self.d,self.v)
            self.x += X
            self.y += Y
            self.z += Z
            for a in range(20):
                if self.charge==1:
                    X,Y,Z= avixyz(-a*5, self.d,self.v)
                    X+=self.x
                    Y+=self.y
                    Z+=self.z
                    for i in range(len(enemi)):
                        if self.charge==1:
                            dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                            if dist<10:
                                enemi[i].aie(5,4,[60,1/6],0,self.dobo)
                                self.charge=2
        if self.charge==2:
            for i in range(len(enemi)):
                dist=ddis(self.x, self.y, self.z, enemi[i].x, enemi[i].y, enemi[i].z)
                if dist<70:
                    enemi[i].aie(5,4,[60,1/6],0,self)
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
            self.good=[true()for i in range(len(self.dobo.pixels))]
            self.competence = self.pyro_2

    def pyro_2(self, enemi, FPS, dcam, vcam):
        self.x=self.dobo.x
        self.y=self.dobo.y
        self.z=self.dobo.z
        if self.goold and self.charge==1:
            self.dobo.touchable=0
            for r,i in enumerate(self.dobo.pixels):
                X,Y,Z=avixyz(randint(1,10)+randint(1,10),randint(-100,100)*pi/100,randint(-100,100)*pi/100)
                if r%5==0:
                    i.color='dark orange'
                else:
                    i.color='red'
                i.forme(X,Y,Z)
            for i in enemi:
                if self.charge==1:
                    dist=ddis(self.x, self.y, self.z, i.x, i.y, i.z)
                    if dist<30:
                        i.aie(0, FPS/2, [70,FPS/20], 0, self)
            if self.dobo.pressed['space']:
                self.dobo.v_z=-1
            self.goold=False
        else:
            self.avance+=FPS*2
            self.charge=2
            self.dobo.touchable=1
            self._temp = create_dobo()
            finish=True
            for r,i in enumerate(self.dobo.pixels):
                if self.good[r] and r<len(self._temp):
                    i.item=self
                    i.bx = i.item.x+(avix(self._temp[r][0],self.dobo.d)+aviy(self._temp[r][1],self.dobo.d))
                    i.by = i.item.y+(avix(self._temp[r][0],self.dobo.d+pi/2)+aviy(self._temp[r][1],self.dobo.d+pi/2))
                    i.bz = i.item.z+self._temp[r][2]
                    d , v = ddir(i.x , i.y, i.z, 0, 0, i.bx,i.by, i.bz)
                    dist = ddis(i.x , i.y, i.z, i.bx,i.by, i.bz)
                    vi=3+self.avance
                    if dist>vi*FPS:
                        X,Y,Z=avixyz(randint(1,10)+randint(1,10),randint(-100,100)*pi/100,randint(-100,100)*pi/100)
                        if r%5==0:
                            i.color='dark orange'
                        else:
                            i.color='red'
                        i.forme(X,Y,Z)
                        finish=False
                        X, Y, Z = avixyz((vi*FPS),d,v)
                        i.forme((i.x-self.x)+X, (i.y-self.y)+Y, (i.z-self.z)+Z)
                    else:
                        i.item=self.dobo
                        i.forme(self._temp[r][0],self._temp[r][1],self._temp[r][2])
                        self.good[r]=False
                        if r==51 or r==64:
                            i.color='black'
                        else:
                            i.color=self.dobo.color
            if finish:
                self.charge=0

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
        self.help = self.dobo.arme[0]
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

    def vague_1(self, pixels):
        if self.charge==0:
            self.pixels = pixels
            self.stun=0
            self.masse=1
            self.charge=1
            self.etat='liq'
            self.flui=0
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            for i in range(len(self.pixels)):
                self.pixels[i].item=self
            self.particules=[{'x':self.x,'y':self.y,'z':self.z,'v':0,'t':randint(0,100), 'd':0, 'c':0}for i in range(len(self.pixels))]
            self.competence = self.vague_2
            
    def vague_2(self,enemi, FPS, dcam, vcam):
        if self.dobo.pressed['a']:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = dcam
            for i in range(len(self.pixels)):
                X,Y,Z=avixyz((110-self.particules[i]['t'])*FPS/4, self.particules[i]['d']+self.d, self.particules[i]['v'])
                self.particules[i]['x']+=X
                self.particules[i]['y']+=Y
                self.particules[i]['z']+=Z
                self.particules[i]['d']=rot(-self.particules[i]['d']/2*FPS,self.particules[i]['d'])
                self.particules[i]['v']=rot(randint(-10,10)*FPS*pi/200,self.particules[i]['v'])
                if self.particules[i]['t']>=100:
                    self.particules[i] = {'x':self.x,'y':self.y,'z':self.z,'v':0,'t':0, 'd':randint(-10,10)*pi/50, 'c':0}
                self.particules[i]['t']+=FPS*randint(25,30)
                if self.particules[i]['c']==0:
                    for r in enemi:
                        dist = ddis(self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z'], r.x, r.y, r.z)
                        if dist<6:
                            r.aie(0.2,0.2, 0, 0,self)
                            r.recul(1.1,self.particules[i]['d']+dcam,self.particules[i]['v'])
                            self.particules[i]['c']=1
                if self.particules[i]['c']==0:
                    self.pixels[i].x = self.particules[i]['x']
                    self.pixels[i].y = self.particules[i]['y']
                    self.pixels[i].z = self.particules[i]['z']
                else:
                    self.pixels[i].x=self.x
                    self.pixels[i].y=self.y
                    self.pixels[i].z=self.z
        else:
            let=True
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            for i in range(len(self.pixels)):
                X,Y,Z=avixyz((110-self.particules[i]['t'])*FPS/4, self.particules[i]['d']+self.d, -(self.particules[i]['t']/(pi*100))+self.particules[i]['v'])
                self.particules[i]['x']+=X
                self.particules[i]['y']+=Y
                self.particules[i]['z']+=Z
                self.particules[i]['d']=rot(randint(-10,10)*FPS*pi/30,self.particules[i]['d'])
                self.particules[i]['v']=rot(randint(-10,10)*FPS*pi/200,self.particules[i]['v'])
                if self.particules[i]['t']>=100:
                    self.particules[i] = {'x':self.x,'y':self.y,'z':self.z,'v':0,'t':101, 'd':0, 'c':0}
                else:
                    let=False
                self.particules[i]['t']+=FPS*randint(25,50)
                if self.particules[i]['c']==0:
                    for r in enemi:
                        dist = ddis(self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z'], r.x, r.y, r.z)
                        if dist<6:
                            r.aie(0.2,0.2, 0, 0,self)
                            r.recul(2,self.particules[i]['d']+dcam,self.particules[i]['v'])
                            self.particules[i]['c']=1
            for i in range(len(self.pixels)):
                if self.particules[i]['c']==0:
                    self.pixels[i].x = self.particules[i]['x']
                    self.pixels[i].y = self.particules[i]['y']
                    self.pixels[i].z = self.particules[i]['z']
                else:
                    self.pixels[i].x=self.x
                    self.pixels[i].y=self.y
                    self.pixels[i].z=self.z
            if let:
                self.charge=0
                for i in self.pixels:
                    i.item = self.yoso
                    i.x=self.x
                    i.y=self.y
                    i.z=self.z
        
    def bule_1(self, pixels, dcam, vcam):
        if self.charge==0:
            self.pixels = pixels
            self.stun=0
            self.avance=0
            self.masse=1
            self.charge=1
            self.etat='solide'
            self.flui=0
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
            for i in range(len(self.pixels)):
                self.pixels[i].item=self
            self.particules=[{'x':0,'y':0,'z':0,'v':0, 'd':0, 'v_z':0, 't':randint(5,10)}for i in range(len(self.pixels))]
            for i in range(len(self.particules)):
                d=randint(-100,100)*pi/100
                v=randint(-100,100)*pi/100
                self.particules[i]['x'], self.particules[i]['y'], self.particules[i]['z']=avixyz(randint(5,60), d, v)
            self.competence = self.bule_2

    def bule_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        stop=True
        for i, r in enumerate(self.pixels):
            if self.charge==1:
                r.forme(randint(-2,3),randint(-2,3),randint(-2,3))
                stop=False
            elif self.particules[i]['t']>0:
                r.forme(self.particules[i]['x'],self.particules[i]['y'],self.particules[i]['z'])
                self.particules[i]['x']+=0
                self.particules[i]['y']+=0
                self.particules[i]['z']+=self.particules[i]['v_z']*FPS*5
                self.particules[i]['v_z']+=FPS*5
                if self.particules[i]['z']+self.z>0:
                    self.particules[i]['z']=-self.z
                self.particules[i]['t']-=FPS*3
                stop=False
            else:
                r.x=self.yoso.x
                r.y=self.yoso.y
                r.z=self.yoso.z
                r.item = self.yoso
        if stop:
            self.charge=0
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
                    Z+=self.z
                    for i in range(len(enemi)):
                        if self.charge==1:
                            dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                            if dist<10:
                                enemi[i].aie(10,6,0,0,self.dobo)
                                enemi[i].recul(20,self.d,self.v)
                                self.charge=2
        if self.charge==2:
            for i in range(len(enemi)):
                dist=ddis(X, Y, Z, enemi[i].x, enemi[i].y, enemi[i].z)
                if dist<70:
                    enemi[i].aie(5,4,0,0,self)
                    D,V=ddir(self.x,self.y,self.z,0,0,enemi[i].x,enemi[i].y,enemi[i].z)
                    enemi[i].recul(20,D,V)
            self.charge=3
    
    def frape_1(self, pixels):
        if self.charge==0:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = self.dobo.d
            self.pixels = pixels
            self.charge = 1
            self.avance = 0
            self.competence= self.frape_2

    def frape_2(self, enemi, FPS, dcam, vcam):
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = self.dobo.z
        self.d = self.dobo.d
        self.avance+=FPS
        if self.avance<0.5:
            self.dobo.avance(10*self.dobo.boost,FPS)
            X = self.x+(avix(self.avance*20,self.d)+aviy(5,self.d))
            Y = self.y+(avix(self.avance*20,self.d+pi/2)+aviy(5,self.d+pi/2))
            Z = self.z
            for i in enemi:
                dist=ddis(X, Y, Z, i.x, i.y, i.z)
                if dist<9:
                    i.aie(8*self.dobo.boost, 3, 0, 0, self.dobo)
                    i.recul(8,-self.d,0)
            for i in range(8):
                self.pixels[i].forme((i//2)+self.avance*20,5+i%2,(i//4)+1)
        elif self.avance<1:
            if self.dobo.pressed['a'] and self.charge==1:
                self.charge=2
                self.avance2=0
            for i in range(8):
                self.pixels[i].forme((i//2)+10-((self.avance-0.5)*20),5+i%2,(i//4)+1)
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
                    if dist<9:
                        i.aie(8*self.dobo.boost, 3, 0, 0, self.dobo)
                        i.recul(8,-self.d,0)
                for i in range(8):
                    self.pixels[i+8].forme((i//2)+self.avance2*20,-5-i%2,(i//4)+1)
            elif self.avance2<1:
                for i in range(8):
                    self.pixels[i+8].forme((i//2)+10-((self.avance2-0.5)*20),-5-i%2,(i//4)+1)
            else:
                self.charge=0

    def shoot_1(self, pixels):
        if self.charge==0:
            self.x = self.dobo.x
            self.y = self.dobo.y
            self.z = self.dobo.z
            self.d = 0
            self.pixels = pixels
            self.etat='solide'
            self.charge = 1
            self.avance = 0
            self.competence= self.shoot_2

    def shoot_2(self, enemi, FPS, dcam, vcam):
        self.avance+=FPS/5
        if self.avance<0.5:
            X = (self.avance*20)-((self.avance*4)**2)
            Y = 5-((self.avance*4)**2)
            Z = -(self.avance*4)**2
        elif self.avance<0.6:
            X = 6
            Y = 1
            Z = -4
        else:
            X = 6
            Y = 1
            Z = 7
            if self.charge==1:
                self.charge=2
                self.x = self.dobo.x
                self.y = self.dobo.y
                self.z = 0
                self.v_z = 0
                for p in self.pixels:
                    p._rand=randint(-10,10)
                self.d = randint(-100,100)*pi/100
                for i in enemi:
                    dist=dis(self.x, self.y, i.x, i.y)
                    if dist<100 and i.z>-7.6:
                        i.aie(-((self.dobo.z+5+abs(self.dobo.v_z))*0.7)*self.dobo.boost, 0, 0, 0, self.dobo)
                        i.stun+=20
                        i.recul(16,dir(self.x,self.y,0,i.x,i.y),0)
                        i.v_z=-2
                self.dobo.z=-7
        if self.charge==2:
            for i,p in enumerate(self.pixels):
                if i>=33:
                    p.item=self
                    p.forme(avix((i/11.5)**2,i*pi/2.5)+avix(p._rand,(i*pi/2.5)+pi/2),aviy((i/11.5)**2,i*pi/2.5)+aviy(p._rand,(i*pi/2.5)+pi/2),0)
        if self.avance<1:
            for i in range(8):
                self.pixels[i].forme((i//2)+X,i%2+Y,(i//4)+Z)
                self.pixels[i+8].forme((i//2)+X,i%2-Y,(i//4)+Z)
        else:
            for p in self.pixels:
                p.item=self.yoso
            self.yoso.terre()
            self.charge=0
    
    def degats(self,x,toile):
        if self.chat==1:
            toile.delete(self.affiche)
        D=randint(-100,100)*pi/100
        self.x=self.dobo.x+avix(5,D)
        self.y=self.dobo.y+aviy(5,D)
        self.z=self.dobo.z
        self.chat=1
        self.toile=toile
        self.avance=0
        self.affiche=toile.create_text(-10,-10, text=str(int(x)))

    def degat_2(self,x,y,xcam,ycam,zcam, dcam, vcam, FPS):
        self.avance+=FPS/5
        xper, yper= per_point(x, y, xcam, ycam, zcam, dcam, vcam, self.x, self.y, self.z-(self.avance*5))
        self.toile.coords(self.affiche, xper, yper)
        if self.avance>2:
            self.toile.delete(self.affiche)
            self.chat=0
        
    def tour(self, enemi, FPS, dcam, vcam):
        self.competence(enemi, FPS, dcam, vcam)

class Etoile(Item):
    def __init__(self, dobo, pixels):
        self.dobo = dobo
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.pixels = pixels
        self.d = 0
        self.z = 0
        self.Mcout=0
        self.etat='solide'
        self.type='arme'
        for i in range(len(pixels)):
            pixels[i].item=self

    def tour(self, FPS):
        self._temp = create_cercle(5)
        self.x = self.dobo.x
        self.y = self.dobo.y
        self.z = 0
        for i in range(15):
            self.pixels[i].forme(self._temp[i][0],self._temp[i][1],0)
        if self.dobo.stun>=10:
            if self.dobo.vie>0:
                self.d+=FPS/2
                if self.dobo.z-7<=0:
                    Z=self.dobo.z-7
                else:
                    Z=0
                for i in range(5):
                    x0,y0,z0 = avixyz(5,i*2*pi/5,0)
                    self.pixels[i*3].forme(x0,y0,Z)
            if self.dobo.vie<=0:
                n=int(self.dobo.mort*115/14)
                for i in range(n):
                    self.dobo.yoso.pixels[i*51%len(self.dobo.yoso.pixels)].visible=False
                    self.dobo.pixels[i*51%115].visible=False
