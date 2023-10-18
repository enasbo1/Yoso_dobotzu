from backwork.variable import r_serv
def modif():
    print('que voulez-vous faire:')
    print('0 => ne rien faire et fermer')
    print('1 => changer le nombre de joueurs')
    print('2 => informations')
    req=str(input(">>> "))
    a=True
    if req=="0":
        a=False
    if req=="1":
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
        print('|\n|\n ')
        modif()
    if req=='2':
        a=False
        p, com = r_serv()
        print('nombre_de_joueur______: ',com)
        print('nombre_de_particules__: ',p)
        print('|\n|\n')
        modif()
    if a:
        print('entree inconnue')
        print('|\n|\n|\n|\n')
        modif()
modif()
