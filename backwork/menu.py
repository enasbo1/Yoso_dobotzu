from client.versus import*

def details(choix, toile, lab, x, y):
    cont=True
    exist=True
    lab.place(x=x,y=y)
    if choix==0:
        image=PhotoImage(file = "images/detail_feux.png")
        exist=False
    if choix==1:
        image=PhotoImage(file = "images/detail_eau.png")
        exist=False
    if choix==2:
        image=PhotoImage(file = "images/detail_foudre.png")
        exist=False
    if choix==3:
        image=PhotoImage(file = "images/detail_terre.png")
        exist=False
    if choix==4:
        image=PhotoImage(file = "images/detail_ombre.png")
        exist=False
    if choix==5:
        image=PhotoImage(file = "images/detail_fer.png")
        exist=False
    if choix==6:
        image=PhotoImage(file = "images/detail_espris.png")
        exist=False
    if exist:
        image=PhotoImage(file = "images/detail_.png")
    page=toile.create_image( x/2, y/2,image = image)
    start=True
    while start:
        if is_pressed('a'):
            start=False
        if is_pressed('p') and exist:
            start=False
            cont=False
        toile.update()
    toile.delete(page)
    lab.place(x=10,y=10)
    return(cont)

start = True
def menu(x,y,toile, lab, serveur):
    lab.place(x=10,y=10)
    toile.create_rectangle(300,200,x,y,fill='dark green')
    obj = []
    obj.append(M.Dobotzu(25,0,-7,"grey",pi/2))
    cam=Cam(obj[0])
    pixel = []
    for i in range(len(obj)):
        pixel += obj[i].pixels
        if obj[i].type=='dobo':
            pixel += obj[i].yoso.pixels
    plan = [Aff(i, pixel, i, toile)for i in range(len(pixel))]

    choix= 0
    nb = 8
    tope=[toile.create_rectangle(10+100*(i%((x-20)/110)),50+140*(i//((x-20)/110)),100+100*(i%((x-20)/110)),180+140*(i//((x-20)/110)))for i in range(nb)]
    img = [PhotoImage(file = "images/feux.png"),
           PhotoImage(file = "images/eau.png"),
           PhotoImage(file = "images/foudre.png"),
           PhotoImage(file = "images/terre.png"),
           PhotoImage(file = "images/ombre.png"),
           PhotoImage(file = "images/fer.png"),
           PhotoImage(file = "images/espris.png"),
           PhotoImage(file = "images/croix.png")]
    image=PhotoImage(file = "images/touches.png")
    aff_image = [toile.create_image( 55+100*(i%((x-20)/110)), 115+140*(i//((x-20)/110)),image = img[i])for i in range(len(img))]
    toile.create_image(150, 450 ,image = image)
    tou=-1
    t=time()
    start = True
    cont= True
    while start and cont:
        toile.update()
        T=time()
        if T-t<0.02:
            sleep(0.02-(T-t))
            FPS=0.1
        else:
            FPS=(T-t)*5
        t=time()
        if is_pressed('q'):
            if tou<0:
                choix -= 1
                choix = choix % nb
            tou=2
        if is_pressed('d'):
            if tou<0:
                choix += 1
                choix = choix % nb
            tou=2
        if is_pressed('s'):
            if tou<0:
                choix += int((x-20)/110)+1
                choix = choix % nb
            tou=2
        if is_pressed('z'):
            if tou<0:
                choix -= int((x-20)/110)
                choix = choix % nb
            tou=2
        tou-=1
        for i in range(nb):
            if i == choix:
                toile.itemconfig(tope[i], fill='blue')
            else:
                toile.itemconfig(tope[i], fill='white')
        if choix!=7:
            if is_pressed('0'):
                start=False
                nombre=0
            if is_pressed('1'):
                start=False
                nombre=1
            if is_pressed('2'):
                start=False
                nombre=2
            if is_pressed('3'):
                start=False
                nombre=3
            if is_pressed('4'):
                start=False
                nombre=4
            if is_pressed('6'):
                start=False
                nombre=6
            if is_pressed('7'):
                start=False
                nombre=7
        if is_pressed('5'):
            cont=details(choix, toile, lab, x, y)
        if choix == 0:
            obj[0].yoso.feux()
        if choix == 1:
            obj[0].yoso.eau()
        if choix == 2:
            obj[0].yoso.foudre()
        if choix == 3:
            obj[0].yoso.terre()
        if choix == 4:
            obj[0].yoso.ombre()
        if choix == 5:
            obj[0].yoso.fer()
        if choix == 6:
            obj[0].yoso.espris()
        for i in  range(len(plan)):
            plan[i].dist(0,0,-10)
        plan = devant(plan)
        obj[0].d=rot(0.1*FPS,obj[0].d)
        obj[0].etoile.tour(FPS)
        obj[0].yoso.tour(FPS)
        for i in range(len(obj)):
            obj[i].tour(FPS)
        for i in range(len(plan)):
            pixel[plan[i].i].position(FPS)
            pixel[plan[i].i].pers(550,500, 0.2, 0.1,-10 ,0 ,pi/50 )
            pixel[plan[i].i].affiche_1(plan[i],330,120) 
    toile.delete(ALL)
    lab.place(x=x,y=-40)
    if cont:
        if nombre==7:
            versus(choix, x, y, toile, serveur)
        else:
            prim.jeux(choix, x, y, toile, nombre)
        menu(x, y, toile, lab, serveur)
