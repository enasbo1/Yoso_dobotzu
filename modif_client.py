from backwork.variable import recup
def modif():
    print('que voulez-vous faire:')
    print('0 => ne rien faire et fermer')
    print("1 => entrer une nouvelle ip_serveur")
    print('2 => changer le nombre de joueurs')
    print('3 => données')
    req=str(input(">>> "))
    a=True
    if req=="0":
        a=False
        print('fermeture')
    if req=="1":
        a=False
        ip=str(input("nouvelle ip (0 pour anuler)>> "))
        if ip!="" and ip!="0":
            with open("client/_cache/serveur.txt","w",encoding='UTF-8') as serv:
                serv.write(ip)
            print('| \n| \n')
        modif()
    if req=="2":
        a=False
        ip=str(input("nb de joueurs (0 pour anuler)>> "))
        try:
            int(ip)
            if int(ip)>0:
                if ip!="0":
                    with open("_cache/nb_joueurs.txt","w",encoding='UTF-8') as serv:
                        serv.write(ip)
            else:
                print("le nombre de client est un entier naturel")
        except:
           print("le nombre de client est un entier naturel")
        print('| \n| \n')
        modif()
    if req=='3':
        a=False
        serveur, p, com = recup()
        print('nombre_de_joueur______: ',com)
        print('nombre_de_particules__: ',p)
        print('ip_du_serveur_________: ',serveur)
        print('| \n| \n')
        modif()
    if a:
        print('entree inconnue')
        print('| \n| \n| \n| \n')
        modif()
modif()
