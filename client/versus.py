import backwork.M as M
import client.elements as li
from client.client import*
from time import time, sleep
import backwork.jeux as prim
from backwork.Cam import Cam
from backwork.variable import p

def versus(choix, x, y, toile, serveur):
    #try:
        n_choix = choix
        choix = li.elements[choix]
        amg = PhotoImage(file = "images/chargement.png")
        rat=toile.create_image(x/2,y/2, image=amg)
        toile.update()
        
        global p
        graph=[]

        terrain=Item(0,0,0,"white","none",0)
        obj=[Dobotzu(25,0,-7,"blue",pi, terrain)for i in range(2)]
        cam=Cam(obj[0])

        for dobo in obj:
            graph=graph+dobo.etoile.pixels

        horison=toile.create_rectangle(0,y/2-(cam.v*4*x/pi),x,y,fill="green4",width = 0)
        
        bord=[]
        for i in range(30):
            D = (i-60)*pi/15
            point = Item(avix(756,D),aviy(756,D),0,"black","nuage",pi/2)
            bord = bord+[[point, avix(756,D) , aviy(756,D), 0]]
            graph = graph+ point.pixels
        for i in range(70):
            D = randint(-500,500)*pi/500
            L = (randint(1,40)**2)/20
            point = Item(avix(756,D),aviy(756,D),-L,"black","nuage",pi/2)
            bord = bord+[[point, avix(756,D), aviy(756,D), -L]]
            graph = graph + point.pixels

        pixels=[Pixel( 0, 0, 0,"black",terrain) for i in range(p)]
        part=pixels + graph
        vies=[Vie(0, [obj[1]], toile, x, y)]
        plan=[Aff(i, part, i, toile)for i in range(len(part))]
        viseur=create_cible(toile, x/2+15, y/2+15)

        X=300
        Y=40
        toile.create_rectangle((x/2)-X-1,y-(Y*2)-1,(x/2)+X,y,fill='white')
        img=PhotoImage(file = "images/reserve.png")
        toile.create_image(x/2, y-Y, image=img)
        vie = toile.create_rectangle(0,0,0,0, fill='white')
        stam=toile.create_rectangle(0,0,0,0, fill='grey')
        mana=toile.create_rectangle(0,0,0,0, fill='blue2')
        bares=[vie, stam, mana]
        competence=[PhotoImage(file = "images/"+str(n_choix)+"/compA.png"),PhotoImage(file = "images/"+str(n_choix)+"/compE.png"),PhotoImage(file = "images/"+str(n_choix)+"/comp8.png")]
        affcomp=[toile.create_image(70+(i%2*(x-140)),(y/2)+(60*i), image=p)for i,p in enumerate(competence)]
        cache=[toile.create_rectangle(0,0,0,0, fill='grey')for i in competence]

        toile.delete(rat)
        amg = PhotoImage(file = "images/attente_serveur.png")
        ser=toile.create_image(x/2,y/2, image=amg)
        toile.update()

        com = Comm(pixels, serveur, obj, cam)
        
        toile.delete(ser)
        amg = PhotoImage(file = "images/attente_client.png")
        cl=toile.create_image(x/2,y/2, image=amg)
        toile.update()
        toile.delete(cl)
        
        com.commence(choix)
        com.dechiffre()

        t=time()
        start=True
        while start:  
            T=time()
            FPS=T-t
            if FPS>1:
                FPS=1
            t=time()
            tour_client(com)
            tour_graph(obj, FPS, bord)
            toile.coords(horison,0,y/2-(cam.v*4*x/pi),x,y)
            tour_viseur(toile, cam, viseur, obj, cache, x, y)
            affiche_pixels(toile, FPS, part, x, y, cam, plan, obj, vies, bares)
            refre(obj)
"""    except:
        amg = PhotoImage(file = "images/erreur.png")
        rat=toile.create_image(x/2,y/2, image=amg)
        toile.update()
"""
