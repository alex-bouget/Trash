from variable import *

userlife = IntVar()
userlife.set(20)
ennemilife = IntVar()
ennemilife.set(20)
userlifel = Label(gamec, text="Votre Vie: "+str(userlife.get()))
ennemilifel = Label(gamec, text="Vie de L'ennemi: "+str(ennemilife.get()))
def change_life(num, nb):
        global ennemilife, userlife
        if num == "e":
            ennemilife.set(ennemilife.get()-int(nb))
            ennemilifel.configure(text="Vie de L'ennemi: "+str(ennemilife.get()))
        else:
            userlife.set(userlife.get()-int(nb))
            userlifel.configure(text="Votre Vie: "+str(userlife.get()))

eclate = IntVar()
eclatu = IntVar()
usereclat = Label(gamec, text="Vos Eclat: "+str(eclatu.get()))
ennemieclat = Label(gamec, text="Eclat ennemi: "+str(eclate.get()))
def change_eclat(num, nb):
    if num == "e":
        eclate.set(eclate.get()+nb)
        ennemieclat.configure(text="Eclat Ennemi: "+str(eclate.get()))
    else:
        eclatu.set(eclatu.get()+nb)
        usereclat.configure(text="Vos Eclat: "+str(eclatu.get()))