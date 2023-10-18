from serveur.serveur import*
from serveur.fonctionphy import*
from backwork.Item import*
from time import time
from backwork.variable import p, com
from backwork.pressed import*

def envoi(trad, joueurs):
    message = trad.chiffre_pos()
    message += trad.chiffre_pix()
    for joueur in joueurs:
        joueur.envoie(message+trad.chiffre_cam(joueur.cam))

def phy(joueurs, FPS):
    for joueur in joueurs:
        joueur.dechiffre()
        dobo = joueur.dobo
        adv=[j.dobo for j in joueurs]
        cam=joueur.cam
        dobo.tour(adv, FPS)
        deplacement(dobo, cam, FPS)
        choc(dobo, adv)
        competences(dobo, adv, cam, FPS)
        limite(dobo)
        dobo.passif(FPS, adv)