from backwork.M import*
from backwork.Cam import Cam
from backwork.affiche_pix import*
from time import time
from time import sleep
 
def jeux(choix, x, y, toile, nombre):
    amg = PhotoImage(file = "images/chargement.png")
    rat=toile.create_image(x/2,y/2, image=amg)
    toile.update()
    sleep(1)
    
    obj = []
    dobo=Dobotzu(25,0,-7,"grey",0)
    cam=Cam(dobo)
    horison=toile.create_rectangle(0,y/2-(cam.v*4*x/pi),x,y,fill="green4",width = 0)
    if 0<nombre<4:
        fou=[Dobotzu(200,(i-(nombre/2))*50,-7,"grey10",0)for i in range(nombre)]
        tclass='fer'
    elif nombre==4:
        fou=[Dobotzu(200,0,-7,"dark khaki",0)]
        tclass='espris'
    if nombre==6:
        fou=[Dobotzu(200,(i-1)*50,-7,"grey10",0)for i in range(2)]
        tclass='fer'
        score=0
        kill = toile.create_text(20,10,text=str(score))
    if nombre==0:
        fou=[Dobotzu(200,0,-7,"white",pi)]
        tclass='none'
    obj.append(dobo)
    for tetzu in fou:
        obj.append(tetzu)
    bord=[]
    for i in range(30):
        D=(i-60)*pi/15
        bord=bord+[[Item(avix(756,D),aviy(756,D),0,"black","nuage",pi/2),avix(756,D),aviy(756,D),0]]
        obj.append(bord[i][0])
    for i in range(70):
        D=randint(-500,500)*pi/500
        L=(randint(1,40)**2)/20
        bord=bord+[[Item(avix(756,D),aviy(756,D),-L,"black","nuage",pi/2),avix(756,D),aviy(756,D),-L]]
        obj.append(bord[i+30][0])
    pixel = []
    for i in range(len(obj)):
        pixel += obj[i].pixels
        if obj[i].type=='dobo':
            pixel += obj[i].yoso.pixels
    plan = [Aff(i, pixel, i, toile)for i in range(len(pixel))]
    
    X=300
    Y=40
    toile.create_rectangle((x/2)-X-1,y-(Y*2)-1,(x/2)+X,y,fill='white')
    img=PhotoImage(file = "images/reserve.png")
    toile.create_image(x/2,y-Y, image=img)
    fouvie=[Vie(i, fou, toile, x,y)for i in range(len(fou))]
    vie = toile.create_rectangle(0,0,0,0, fill='white')
    stam=toile.create_rectangle(0,0,0,0, fill='grey')
    mana=toile.create_rectangle(0,0,0,0, fill='blue2')
    quiter=PhotoImage(file = "images/quit.png")
    part=toile.create_image(x-55,20, image=quiter)
    competence=[PhotoImage(file = "images/"+str(choix)+"/compA.png"),PhotoImage(file = "images/"+str(choix)+"/compE.png"),PhotoImage(file = "images/"+str(choix)+"/comp8.png")]
    affcomp=[toile.create_image(70+(i%2*(x-140)),(y/2)+(60*i), image=p)for i,p in enumerate(competence)]
    cache=[toile.create_rectangle(0,0,0,0, fill='grey')for i in competence]
    point = PhotoImage(file = "images/pointeur.png")
    pointeur = toile.create_image(0,0, image=point)
    Ddobo, Edobo, Mdobo = 0 ,30 , 20
    t=time()
    a, d= 0,0
    cible=0
    viseur=create_cible(toile, x/2+15, y/2+15)
    start, actif=True, False
    while start:
        T=time()
        if T-t>0.1:
            FPS=0.5
        else:
            FPS=(T-t)*5
        t=time()

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
        if nombre==6:
            toile.itemconfig(kill, text='kill :' + str(score))
        for i in fouvie:
            i.dist(cam.x, cam.y, cam.z)
        fouvie = devant(fouvie)
        for i, tetzuvie in enumerate(fouvie):
            tetzu=fou[tetzuvie.i]
            tetzu.yoso.etat='solide'
            if tclass=='fer':
                tetzu.yoso.fer()
            if tclass=='espris':
                tetzu.yoso.cauchemard()
            if tclass=='none':
                tetzu.yoso.none()
            enemi=[dobo]
            enemi+=[fou[a]for a in range(len(fou))]
            tetzu.comportement(enemi, FPS, cam.d, cam.v, cam.x, cam.y, cam.z, x, y, toile)
            if tetzu.vie==0:
                toile.coords(tetzuvie.barre,-1,-1,-1,-1)
                toile.coords(tetzuvie.font,-1,-1,-1,-1)
                if nombre==6:
                    if tetzu.mort>=14:
                        tetzu.vie=100
                        tetzu.x=randint(-100,100)
                        tetzu.y=randint(-100,100)
                        tetzu.z=-100
                        score+=1
                        for pix in tetzu.pixels:
                            pix.visible=True
                        for pix in tetzu.yoso.pixels:
                            pix.visible=True
            else:
                C=per_point(x, y, cam.x, cam.y, cam.z, cam.d, cam.v, tetzu.x, tetzu.y, tetzu.z-10)
                toile.coords(tetzuvie.barre,C[0]-50, C[1]-4,C[0]-50+int(tetzu.vie),C[1]+5)
                toile.coords(tetzuvie.font,C[0]-51, C[1]-5,C[0]+50,C[1]+5)
            toile.coords(vie,x/2+290,y-25,x/2+290+int(5.8*(dobo.vie-100)),y-8)
            toile.coords(stam,x/2-292,y-58,x/2-292+int(7.5*Edobo),y-49)
            toile.coords(mana,x/2+43,y-58,x/2+43+int(12.5*Mdobo),y-49)
        enemi=[fou[i]for i in range(len(fou))]
        if is_pressed('q'):
            dobo.pressed['q']=True
            Ddobo = tourne_gauche(cam.d)
            if a==0:
                dobo.avance(3,FPS)
                a=-1
        if is_pressed('d'):
            dobo.pressed['d']=True
            Ddobo = tourne_droite(cam.d)
            if a==0:
                dobo.avance(3,FPS)
                a=-1
        if is_pressed('s'):
            dobo.pressed['s']=True
            Ddobo = tourne_arrie(cam.d)
            if a==0:
                dobo.avance(3,FPS)
                a=-1
        if is_pressed('z'):
            dobo.pressed['z']=True
            Ddobo = tourne_avan(cam.d)
            if a==0:
                obj[0].avance(3,FPS)
                a=-1
        if is_pressed('0') and Edobo>=2*FPS/5:
            dobo.pressed['0']=True
            dobo.avance(6,FPS)
            dobo.yoso.flui=11
            a-=2
        else:
            dobo.yoso.flui=5
        if choix == 0:
            dobo.yoso.feux()
        if choix == 1:
            dobo.yoso.eau()
        if choix == 2:
            dobo.yoso.foudre()
        if choix == 3:
            dobo.yoso.terre()
            dobo.yoso.etat='solide'
        if choix == 4:
            dobo.yoso.ombre()
            dobo.yoso.etat='solide'
        if choix == 5:
            dobo.yoso.fer()
            dobo.yoso.etat='solide'
        if choix == 6:
            dobo.yoso.espris()
        came=True
        if is_pressed('+'):
            r=2/3
        else:
            r=1
        if is_pressed('7'):
            cam.d = rot(-FPS*r**3, cam.d)
            came=False
        if is_pressed('9'):
            cam.d = rot(FPS*r**3, cam.d)
            came=False
        if is_pressed('*'):
            if cam.z<-10:
                cam.v = rot(-(FPS/5)*r, cam.v)
            came=False
        if is_pressed('1'):
            cam.v = rot((FPS/5)*r, cam.v)
            came=False
        if is_pressed('5'):
            dobo.pressed['5']=True
        if is_pressed('4'):
            dobo.pressed['4']=True
        if is_pressed('6'):
            dobo.pressed['6']=True
        if is_pressed('p'):
            start=False
        
        if is_pressed(' '):
            Edobo=dobo.saut(Edobo)
        if is_pressed('e'):
            Edobo, Mdobo= dobo.competence_e(FPS,Edobo, Mdobo, enemi, cam.d, cam.v)
        if is_pressed('a'):
            Edobo, Mdobo= dobo.competence_a(FPS,Edobo, Mdobo, enemi, cam.d, cam.v)
        if is_pressed('8'):
            Edobo, Mdobo= dobo.competence_8(FPS,Edobo, Mdobo, enemi, cam.d, cam.v)
        dobo.d = tourne(dobo.d, Ddobo, FPS)
        if is_pressed('-'):
            if d<0:
                cible+=1
                if cible==len(enemi):
                    actif=False
                if cible>len(enemi):
                    cible=0
                    actif=True
                while actif and enemi[cible].vie<=0:
                    cible+=1
                    if cible==len(enemi):
                        actif=False
                    if cible>len(enemi):
                        cible=0
                        actif=True
            d=1
        if actif:
            tetzu=fou[cible]
            if tetzu.vie!=0:
                C=per_point(x, y, cam.x, cam.y, cam.z, cam.d, cam.v, tetzu.x, tetzu.y, tetzu.z-10)
                toile.coords(pointeur,C[0], C[1]-6)
            else:
                actif=False
        else:
            toile.coords(pointeur,-50,-50)
        d-=0.5
        X,Y,Z = avixyz(-100,cam.d,cam.v)
        X += obj[0].x
        Y += obj[0].y
        Z += obj[0].z
        cam.x = X+avix(10,cam.d-pi/2)
        cam.y = Y+aviy(10,cam.d-pi/2)
        cam.z = -abs(Z)-10
        ecra=False
        if dobo.z>-1:
            Z=-1
            erca=True
        else:
            Z=dobo.z
        tel=True
        if actif and came:
            if dobo.z<-5:
                if ecra:
                    D, V = ddir(cam.x, cam.y, cam.z, cam.d, cam.v-pi/20, enemi[cible].x, enemi[cible].y, enemi[cible].z)
                else:
                    D, V = ddir(dobo.x, dobo.y, dobo.z, cam.d, cam.v, enemi[cible].x, enemi[cible].y, enemi[cible].z)
            else:
                D = dir(dobo.x, dobo.y, cam.d, enemi[cible].x, enemi[cible].y)
                V = rot(pi/20, cam.v)
            T=dir(0,0,0,D,V)
            R=dis(0,0,D,V)
            if R<2*pi/ddis(dobo.x, dobo.y, dobo.z, enemi[cible].x, enemi[cible].y, enemi[cible].z):
                C=per_point(x, y, cam.x, cam.y, cam.z, cam.d, cam.v, tetzu.x, tetzu.y, tetzu.z)
                deplace(toile, viseur, C[0], C[1])
                tel=False
            if R>FPS/4:
                cam.d=rot(avix(FPS/8,T),cam.d)
                cam.v=rot(aviy(FPS/8,T),cam.v)
            else:
                cam.d=rot(D,cam.d)
                cam.v=rot(V,cam.v)
        if tel:
            deplace(toile, viseur, x/2+15, y/2+15)
        if cam.v<-pi/3:
            cam.v=-pi/3
        if cam.v>pi/3:
            cam.v=pi/3
        Edobo, Mdobo = dobo.passif(FPS, Edobo, Mdobo, enemi, cam.d, cam.v)
        a, b, c = dobo.test(FPS, Edobo, Mdobo)
        n=1
        if a:
            toile.coords(cache[n],0,0,0,0)
        else:
            X=70+(n%2*(x-140))
            Y=(y/2)+(60*n)
            toile.coords(cache[n],X-24,Y-24,X+23,Y+23)
        n=0
        if b:
            toile.coords(cache[n],0,0,0,0)
        else:
            X=70+(n%2*(x-140))
            Y=(y/2)+(60*n)
            toile.coords(cache[n],X-24,Y-24,X+23,Y+23)
        n=2
        if c:
            toile.coords(cache[n],0,0,0,0)
        else:
            X=70+(n%2*(x-140))
            Y=(y/2)+(60*n)
            toile.coords(cache[n],X-24,Y-24,X+23,Y+23)
        affiche_pixels(toile, FPS, pixel, x, y, cam, plan)
        for i in range(len(obj)):
            obj[i].tour(FPS)
        toile.coords(horison,0,y/2-(cam.v*4*x/pi),x,y)
        Edobo+=a*FPS/5
        a=0
        if Mdobo<=20-FPS/5 and Edobo>=2*FPS/5:
            Mdobo+=2*FPS/5
            Edobo-=3*FPS/5
        elif Mdobo>20-FPS/5:
            Mdobo=20
        if Edobo<=40-FPS:
            Edobo+=4*FPS/5
        else:
            Edobo=40
        toile.coords(rat,-x,-y)
        toile.update()
    toile.delete(part)
