from tkinter.constants import S
from serveur.Mdobo import*
from serveur.Myoso import*
from backwork.Cam import Cam
import socket as sock
from backwork.traduct import Trad

class Arbitre:
    def __init__(self):
        self.server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.nb=0
        self.port=1266
        self.trad=Trad()
        self.server.bind(("", self.port))
        self.server.listen(self.nb)
        self.joueur=[]
    
    def ecoute(self, nb):
        print('serveur en écoute ----- port= '+str(self.port)+' nb= '+str(nb))
        for i in range(nb):
            Joueur(self, i)
            print(str(i+1)+'e client acuelli')
    
    def create(self):
            _item=[[],[]]
            for i,j in enumerate(self.joueur):
                dobo=j.dobo
                _item[0].append("D"+str(i))
                _item[1].append(dobo)
                _item[0].append("Y"+str(i))
                _item[1].append(dobo.yoso)
                _item[0]=_item[0]+["A"+str(i)+str(y)for y in range(len(dobo.armes))]
                _item[1]=_item[1]+[y for y in dobo.armes]
            self.trad.serveur({_item[0][i]:_item[1][i]for i in range(len(_item[0]))})

    def start(self):
        message='I'
        for i in range(self.nb):
            e='Y'+str(i)
            message+='/S,'+e+','+self.trad.item[e].element
        message+='/I'
        for j in self.joueur:
            j.envoie(message)
    def ajoute(self, joueur):
        self.nb+=1
        self.joueur=self.joueur+ [joueur]

class Joueur:
    def __init__(self, arbitre, nb):
        cli, adrs = arbitre.server.accept()
        self.id = cli
        self.nb=nb
        self.adrs = adrs
        self.arbitre= arbitre
        self.arbitre.ajoute(self)
    
    def initial(self, pixels):
        message=str(self.nb)
        self.id.send(message.encode()) # -> Comm: commence() 'client est entree'
        message=self.id.recv(1024).decode() # <- Comm: commence() 'choix du perso'
        self.element=message
        _p=[pixels[1], pixels[1]+115]
        _y=[pixels[1]+115, pixels[1]+230]
        self.dobo=Dobotzu(25*((self.nb*2)-1), 0 ,-7,"grey", pi/2*(-(self.nb*2)+1), _p, _y)
        self.dobo.yoso.element=self.element
        print(self.element)
        self.cam= Cam(self.dobo)
        self.dobo.cam=self.cam
        return _y[1]
    
    def dechiffre(self):
        message=self.id.recv(1024).decode()
        if message!='':
            for i in range(len(self.dobo.pressed)):
                self.dobo.pressed[i]= message[i]=="1"

    def envoie(self, message):
        self.id.send(message.encode())

