from backwork.Item import Item

class Yoso(Item):
    def __init__(self, dobo , pixels):
        self.syncro(dobo)
        self.flui=3
        self.dobo=dobo
        self.element="none"
        self.etat='solide'
        self.type = "yoso"
        self.forme=["none"]+pixels+[""]
        self.pixels = pixels
        self.pixel = pixels[0]
        self.actif = 1
        self.silo = {'feux':'',
                     'eau':'',
                     'foudre':'',
                     'terre':'saddle brown'}
        
    def tour(self):
        self.forme[0] = self.element
        self.forme[1] = self.pixels[0]
        self.forme[2] = self.pixels[1]
        self.forme[3] = self.silo[self.element]
        self.syncro(self.dobo)

    def caract(self):
        return([int(self.x*1000)/1000,
         int(self.y*1000)/1000, 
         int(self.z*1000)/1000, 
         int(self.d*1000)/1000])
