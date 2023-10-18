from client.Mdobo import*
from socket import*
from backwork.traduct import Trad
class Comm(Item):
    def __init__(self, pixels, serveur, dobo, cam):
        self.pressed=[False,False, False, False, False, False, False, False, False, False, False, False]
        self.dobo = dobo
        self.cam=cam
        self.trad=Trad()
        self.pixels=pixels
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(serveur)
    
    def commence(self, dobotzu):
        entree = self.client.recv(1024).decode() # <- serveur: J.__init__ 'client est entree, il est le Xeme'
        if entree == "0" or entree=="1":
            print(entree)
            print('enfin (^^)')
            self.nb=int(entree[0])
            adv=[self.nb,abs(self.nb-1)]
            _item=[[],[]]
            for i in range(2):
                _item[0].append("D"+str(adv[i]))
                _item[1].append(self.dobo[i])
                _item[0].append("Y"+str(adv[i]))
                _item[1].append(self.dobo[i].yoso)
                _item[0]=_item[0]+["A"+str(adv[i])+str(y)for y in range(len(self.dobo[i].armes))]
                _item[1]=_item[1]+[y for y in self.dobo[i].armes]
            self.trad.client({_item[0][i]:_item[1][i]for i in range(len(_item[1]))},self.pixels)
            self.client.send(dobotzu.encode()) # -> serveur: J.initial - message,  'choix du perso'
        else:
            print(entree)
            print ('ET MERDE!! (><)')

    def envoi(self):
        question=""
        for i in self.pressed:
            if i:
                question+="1"
            else:
                question+='0'
        self.client.send(question.encode())
    
    def dechiffre(self):
        reponse=self.client.recv(8192).decode()
        self.trad.dechiffre(reponse, self.cam)

