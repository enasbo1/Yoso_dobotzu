from backwork.Item import*

class Trad: #certifié
    def __init__(self):
        self.dico={
            'none': forme_none,
            'dobo':forme_dobo,
            'feux':forme_feux,
            'eau': forme_eau,
            'foudre':forme_foudre,
            'boule_feux':forme_boule_feux,
            'fla_point':forme_fla_point,
            'torche':forme_torche,
            'brule': forme_brule,
            'aqua_point': forme_aqua_point,
            'boule_eau': forme_boule_eau,
            'dobeau':forme_dobeau,
            'traine': forme_traine,
            'tir_elec': forme_tir_elec,
            'eclair': forme_eclair,
            'inv_eclair': forme_dobo_eclair,
            'terre': forme_terre,
            'terratape': forme_terratape,
            'terbaston': forme_terbaston,
            'terrazone': forme_terrazone
         }
    
    def client(self, item, pixels):
        self.item=item
        self.part= pixels
    
    def serveur(self, item): 
        self.item=item
        self.pos= []
        self.pix= []

    def recup_pos(self):
        for i in list(self.item):
            item=self.item[i]
            if item.actif==1:
                _t=[1, i]+item.caract()
            else:
                _t=[0, i]
            self.pos=self.pos+[_t]

    def recup_pix(self):
        for i in list(self.item):
            item=self.item[i]
            if item.actif==1:
                _t=[i]+item.forme
                self.pix=self.pix+[_t]
        
    def chiffre_pos(self):
        self.recup_pos()
        message="I"
        for m in self.pos:
            message+="/"
            message+="C"
            for tr in m:
                message+=","
                message+=str(tr)
        message+="/I"
        self.pos=[]
        return(message)

    def chiffre_pix(self):
        self.recup_pix()
        message="I"
        for m in self.pix:
            message+="/"
            message+="P"
            for tr in m:
                message+=","
                message+=str(tr)
        message+="/I"
        self.pix=[]
        return(message)

    def chiffre_cam(self, cam):
        _cam=cam.recup_pos()
        message="I/O"
        for tr in _cam:
            message+=","
            message+=str(tr)
        message+="/I"
        self.pix=[]
        return(message)

    def dechiffre(self, message, cam):
        _li=message.split("/")
        #print(message)
        if _li!="":
            for port in _li:
                if port!='':
                    if port[0]=="P":
                        mess=port.split(",")
                        porteur=self.item[mess[1]]
                        if mess[2]!='none':
                            self.config_part(self.dico[mess[2]],int(mess[3]), int(mess[4]), porteur, mess[5].split('('))
                    if port[0]=="C":
                        mess=port.split(",")
                        if int(mess[1])==1:
                            item=self.item[mess[2]]
                            item.propriete(mess)
                    if port[0]=="O":
                        mess=port.split(",")
                        cam.propriete(mess)
                    if port[0]=="S":
                        mess=port.split(',')
                        yoso=self.item[mess[1]]
                        yoso.init(mess[2])
                    if port[0]=="I":
                        pass
        
    def config_part(self, forme, p1, p2, porteur, arg): #ok
        _for=forme(arg)
        for i in range(p1,p2):
            r=i-p1
            part=self.part[i]
            co=_for[r]
            part.item=porteur
            porteur.pixels=porteur.pixels+[part]
            part.forme(co[0], co[1], co[2])
            part.color=co[3]
