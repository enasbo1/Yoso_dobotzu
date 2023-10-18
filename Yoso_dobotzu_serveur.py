from serveur.fonctionserv import*
print(p)

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

pixels=[0,0]
arbi = Arbitre()
arbi.ecoute(com)
joueurs=arbi.joueur
trad=arbi.trad

for joueur in joueurs:
    pixels[1]=joueur.initial(pixels)
print(pixels[1])
arbi.create()
arbi.start()

online = True
t=time()
#jusque ici ça va
while online:
    T=time()
    FPS=(T-t)*5
    if FPS>1:
        FPS=1
    t=time()
    #try:
    if True:
        envoi(trad, joueurs)
        phy(joueurs, FPS)
#    except:
 #       pass
arbi.serveur.close()
