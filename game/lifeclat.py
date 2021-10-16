from variable import *

def change_life(num, nb):
        global ennemilife, userlife
        if num == "e":
            ennemilife.set(ennemilife.get()-int(nb))
            ennemilifel.ecrire(lang[5]+str(ennemilife.get()))
        else:
            userlife.set(userlife.get()-int(nb))
            userlifel.ecrire(lang[4]+str(userlife.get()))

def change_eclat(num, nb):
    if num == "e":
        eclate.set(eclate.get()+nb)
        ennemieclat.ecrire(lang[7]+str(eclate.get()))
    else:
        eclatu.set(eclatu.get()+nb)
        usereclat.ecrire(lang[6]+str(eclatu.get()))