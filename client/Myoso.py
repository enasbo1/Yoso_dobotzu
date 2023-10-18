from backwork.Item import Item

class Yoso(Item):
    def __init__(self, dobo):
        self.syncro(dobo)
        self.flui=30
        self.dobo=dobo
        self.etat='solide'
        self.type = "yoso"
        self.actif=1
        self.fx=0
        self.element = 'none'
        self.fy=0
        self.fz=0
        self.pixels=[]
        self.elem={'none':['solide',0,0,0],
                   'feux':['fix',-6,0,2],
                   'eau':['fix',1,0,-2.5],
                   'foudre':['fou',-6,0,1],
                   'terre':['solide',0,0,0]
                   }

    def init(self, entree):
        self.element = entree
        self.fx = self.elem[entree][1]
        self.fy = self.elem[entree][2]
        self.fz = self.elem[entree][3]
    
    def tour(self):
        self.syncro(self.dobo)

    def refre(self):
        self.pixels=[]
        self.etat = self.elem[self.element][0]
    
    def propriete(self,mess):
        self.x = float(mess[3])
        self.y = float(mess[4])
        self.z = float(mess[4])
        self.d = float(mess[5])
