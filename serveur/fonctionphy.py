from serveur.serveur import*
from backwork.Item import*
from time import time
from backwork.variable import p, com
from backwork.pressed import*

def deplacement(dobo, cam, FPS):
    a=0
    av=0
    if is_pressed(dobo, 'q'):
        dobo.D = tourne_gauche(cam.d)
        if a==0:
            av=3
            a=-1
    if is_pressed(dobo, 'd'):
        dobo.D = tourne_droite(cam.d)
        if a==0:
            av=3
            a=-1
    if is_pressed(dobo, 's'):
        dobo.D = tourne_arrie(cam.d)
        if a==0:
            av=3
            a=-1
    if is_pressed(dobo, 'z'):
        dobo.D = tourne_avan(cam.d)
        if a==0:
            av=3
            a=-1
    if is_pressed(dobo, '0') and dobo.E>=2*FPS/5:
        av=9
        a-=2
    dobo.avance(av,FPS)
    dobo.d = tourne(dobo.d, dobo.D, FPS)

    r=1
    if is_pressed(dobo, '+'):
        r=0.2
    if is_pressed(dobo, '7'):
        cam.d = rot(-FPS*r, cam.d)
        came=False
    if is_pressed(dobo, '9'):
        cam.d = rot(FPS*r, cam.d)
        came=False
    if is_pressed(dobo, 'space'):
        dobo.saut()

def limite(dobo):
    D=dir(0, 0, 0, dobo.x, dobo.y)
    L=dis(0, 0, dobo.x, dobo.y)
    if L > 756:
        dobo.x = avix(756,D)
        dobo.y = aviy(756,D)

def choc(dobo, adv):
    for ad in adv:
        if ad != dobo:
            L = ddis(ad.x, ad.y, ad.z, dobo.x, dobo.y, dobo.z)
            if L<12:
                D, V = ddir(ad.x, ad.y, ad.z, 0, 0, dobo.x, dobo.y, dobo.z)
                X, Y, Z = avixyz(12-L, D, V)
                dobo.x += X
                dobo.y += Y
                dobo.z += Z

def competences(dobo, adv, cam, FPS):
    if is_pressed(dobo,'e'):
        dobo.competence_e(FPS, adv, cam)
    if is_pressed(dobo,'a'):
        dobo.competence_a(FPS, adv, cam)
    if is_pressed(dobo,'8'):
        dobo.competence_8(FPS, adv, cam)