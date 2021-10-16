from variable import *

def change_life(num, nb):
        global ennemilife, userlife
        if num == "e":
            ennemilife.set(ennemilife.get()-int(nb))
            ennemilifel.ecrire("Vie de L'ennemi: "+str(ennemilife.get()))
        else:
            userlife.set(userlife.get()-int(nb))
            userlifel.ecrire("Votre Vie: "+str(userlife.get()))

def change_eclat(num, nb):
    if num == "e":
        eclate.set(eclate.get()+nb)
        ennemieclat.ecrire("Eclat Ennemi: "+str(eclate.get()))
    else:
        eclatu.set(eclatu.get()+nb)
        usereclat.ecrire("Vos Eclat: "+str(eclatu.get()))