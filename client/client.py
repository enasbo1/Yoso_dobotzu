from client.Comm import*
from keyboard import is_pressed

def affiche_pixels(toile, FPS, pixels, x, y, cam, plan, obj, vies, bares): #certifié
    cam.place()
    for i in pixels:
        i.position(FPS)
    for i in  plan:
        i.dist(cam.x, cam.y, cam.z)
    plan = devant(plan)
    for v in vies:
        v.dist(cam.x, cam.y, cam.z)
    vies = devant(vies)
    for v in vies:
        if v.dobo.vie<=0:
            v.cache()
        else:
            v.place(cam)
    for p in plan:
        pixels[p.i].pers(x,y,cam.x, cam.y, cam.z, cam.d, cam.v)
        pixels[p.i].affiche(p)
    toile.coords(bares[0],x/2+290,y-25,x/2+290+int(5.8*(cam.dobo.vie-100)),y-8)
    toile.coords(bares[1],x/2-292,y-58,x/2-292+int(7.5*cam.En),y-49)
    toile.coords(bares[2],x/2+43,y-58,x/2+43+int(12.5*cam.Ma),y-49)
    toile.update()

def tour_viseur(toile, cam, viseur, obj, cache, x, y):
    dobo=obj[0]
    tel=True
    for adv in obj:
        if adv!=dobo:
            if dobo.z<-5:
                D, V = ddir(dobo.x, dobo.y, dobo.z, cam.d, cam.v, adv.x, adv.y, adv.z)
            else:
                D = dir(dobo.x, dobo.y, cam.d, adv.x, adv.y)
                V = rot(pi/20, cam.v)
            T=dir(0,0,0,D,V)
            R=dis(0,0,D,V)
            if R<2*pi/ddis(dobo.x, dobo.y, dobo.z, adv.x, adv.y, adv.z):
                C=per_point(x, y, cam.x, cam.y, cam.z, cam.d, cam.v, adv.x, adv.y, adv.z)
                deplace(toile, viseur, C[0], C[1])
                tel=False
    if tel:
        deplace(toile, viseur, x/2+15, y/2+15)
    n=1
    if cam.comp_a:
        toile.coords(cache[n],0,0,0,0)
    else:
        X=70+(n%2*(x-140))
        Y=(y/2)+(60*n)
        toile.coords(cache[n],X-24,Y-24,X+23,Y+23)
    n=0
    if cam.comp_e:
        toile.coords(cache[n],0,0,0,0)
    else:
        X=70+(n%2*(x-140))
        Y=(y/2)+(60*n)
        toile.coords(cache[n],X-24,Y-24,X+23,Y+23)
    n=2
    if cam.comp_8:
        toile.coords(cache[n],0,0,0,0)
    else:
        X=70+(n%2*(x-140))
        Y=(y/2)+(60*n)
        toile.coords(cache[n],X-24,Y-24,X+23,Y+23)

def tour_graph(obj, FPS, bord):
    for dobo in obj:
        dobo.tour(FPS)
    dobo=obj[0]
    for b in bord:
        boo=b[3]!=0
        Ds= dis(0,0,dobo.x,dobo.y)
        Dd= dis(b[1],b[2],dobo.x,dobo.y)
        if boo:
            D,V=ddir(b[1], b[2], b[3], 0, 0, dobo.x, dobo.y, dobo.z)
            do=Dd*Ds/900
            if do>=756:
                do=0
            X,Y,Z=avixyz(do,D,V)
            X+=b[1]
            Y+=b[2]
            Z+=b[3]
            D,V=ddir(0,0,0,0,0,X, Y, Z)
            b[0].x=avix(756,D)
            b[0].y=aviy(756,D)
            X,Y,Z=avixyz(756,D,V)
            b[0].z=Z

def tour_client(comm): #certifié
    comm.pressed=[is_pressed(' ') , is_pressed('8') , is_pressed('5'),
                  is_pressed('6') , is_pressed('4') , is_pressed('e'),
                  is_pressed('a') , is_pressed('z') , is_pressed('q'),
                  is_pressed('s') , is_pressed('d') , is_pressed('0'), 
                  is_pressed('7') , is_pressed('9'), is_pressed('+')]
    comm.envoi()
    #tour serveur
    comm.dechiffre()

def refre(obj):
     for dobo in obj:
        dobo.refre()
