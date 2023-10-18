def recup():
    with open("client/_cache/serveur.txt","r",encoding='UTF-8') as serv:
        serveur = serv.read()
    with open('_cache/nb_joueurs.txt',"r", encoding='UTF-8') as nb:
        com = int(nb.read())
    p=com*230
    return(serveur, p, com)

def r_serv():
    with open('_cache/nb_joueurs.txt',"r", encoding='UTF-8') as nb:
        com = int(nb.read())
        p=com*230
    return(p, com)
serveur, p, com = recup()

