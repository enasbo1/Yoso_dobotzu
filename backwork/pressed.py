dico={'space':0,'8':1, '5':2, '6':3, '4':4, 'e':5, 'a':6, 'z':7, 'q':8, 's':9, 'd':10, '0':11, '7':12, '9':13, '+':14}
taille=len(dico)
def is_pressed(Item, x):
    return Item.pressed[dico[x]]