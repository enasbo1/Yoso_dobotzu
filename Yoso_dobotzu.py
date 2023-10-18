from backwork.menu import*
from backwork.variable import serveur
x=850
y=700
fenetre=Tk()
fenetre.title("Yoso dobotzu")
fenetre.geometry(str(x)+'x'+str(y))
toile = Canvas(fenetre, width = x, height = y, bg="white")
toile.place(x=0,y=0)
lab = Label(fenetre, text = 'choisis ton dobotzu' ,fg = 'white',bg = 'blue', font=20,  width = 92, height = 1)
lab.place(x=10,y=10)

serveur = (str(serveur), 1266)

menu(x, y, toile, lab, serveur)
