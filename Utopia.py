import game
import deck_creator as deck
from tkinter import * #importation
def play():
    """ouverture de jeu"""
    deck.music.play_ambiant("click") #jouer un son
    deck.music.stop() #arreter la musique
    sa.destroy() #destruction du canvas du menu
    game.start_game()
def crea():
    """ouverture du deck creator """
    deck.music.play_ambiant("click") #jouer un son
    deck.music.stop() #arreter la musique
    sa.destroy() #destruction du canvas du menu
    deck.start_deck_creator()
def change_lang(evt):
    """changer la langue du jeu sur la listbox des settings"""
    value=str(lang_list.get(lang_list.curselection())) #récuperation du nom cliqué sur la listbox
    open("save/lang.txt", "w").write(value) #sauvegarde de la langue
def options():
    """ouverture des options"""
    global lang_list
    deck.music.play_ambiant("click") #jouer un son
    deck.music.stop() #arreter la musique
    sa.destroy() #destruction du canvas du menu
    options_canvas = Canvas(deck.fenetre) #creation du canvas pour les settings
    retour = Button(options_canvas, text=deck.lang[2], command=deck.retour) #boutton retour (detruit la fenetre)
    music_b = Checkbutton(options_canvas, text=deck.lang[34], variable=deck.play, command=deck.musique) #activer les musiques
    ambient_b = Checkbutton(options_canvas, text=deck.lang[35], variable=deck.ambient_v, command=deck.ambient) #activer les son ambient
    lang_list = Listbox(options_canvas) #listbox pour les langues
    lang_list.bind('<<ListboxSelect>>', change_lang)
    for item in deck.os.listdir("lang"): #inserer dans la listbox toutes les langues venant du dossier "lang"
        lang_list.insert(END, item)
    options_canvas.pack()
    music_b.grid()
    ambient_b.grid(row=1)
    lang_list.grid(row=2)
    retour.grid(row=3)
def booster_rcard(common, rituel, rare, mythique, legend):
    """systeme de création d'une carte du booster avec des pourcentages"""
    h = deck.random.random() #création d'un chiffre random
    if h < common: #teste par rapport au chiffre random
        f = '' #endroit où est stocké la rareté de la carte
        while f!="C": #tant que la rareté n'est pas atteint on continue
            x = deck.random.randint(1, len(deck.card_name)-1)
            """
            récupere le numero alétoire d'une de
            toutes les cartes du jeu (sauf la carte 0)
            """
            f = deck.card_rarity[x] #récupération de la rareté
            g = deck.card_nb[x] #récupération du numéro
    elif h < rituel+common:
        f = ''
        while f!="O":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
    elif h < rare+rituel+common:
        f = ''
        while f!="R":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
    elif h < mythique+rare+rituel+common:
        f = ''
        while f!="M":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
    elif h < legend+mythique+rare+rituel+common:
        f = ''
        while f!="L":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
    if len(g.split(deck.mods_nb_enter)) < 2:
        return g
    else:
        return booster_rcard(common, rituel, rare, mythique, legend)
def booster(l):
    """création des 3 cartes du booster par rapport au """
    card_b = []
    if l == "normal": #pour un booster "normal"
        for i in range(3): #récupérer 3 cartes
            card_b.append(booster_rcard(0.4,0.4,0.11,0.06,0.03)) #récupere alétoirement des cartes suivant des pourcentages
    elif l == "rare":
        for i in range(3):
            card_b.append(booster_rcard(0.35,0.25,0.20,0.15,0.05))
    elif l == "mythique":
        for i in range(3):
            card_b.append(booster_rcard(0.30,0.25,0.20,0.15,0.10))
    elif l == "legende":
        for i in range(3):
            card_b.append(booster_rcard(0.25,0.20,0.20,0.20,0.15))
    elif l == "ultra":
        for i in range(3):
            card_b.append(booster_rcard(0,0,0.50,0.30,0.20))
    else:
        return "no"
    return card_b
def depart():
    """ouverture du jeu; menu principale"""
    global sa
    sa = Canvas(deck.fenetre, width=deck.TK_x, height=deck.TK_y) #création du canvas du menu
    sa.pack()
    try:
        exec(deck.serv.urlopen(deck.server+"menu.txt").read().decode(),globals()) #on essaye de recupérer le menu internet
    except:
        try:
            exec(deck.serv.urlopen(deck.server+"menu.txt").read().decode(),globals()) #on réessaye (bug avec urllib)
        except:
            with open("menu.dat", "r") as f: #si impossible de se connecter au serv on récupere le menu hors-ligne
                exec(f.read(),globals())
def open_booster(evt):
    """ouvrir un booster"""
    global C1, C2, C3
    sa.destroy()
    value = str(ki.get(ki.curselection())) #récupérer le nom dans la listbox
    ki.delete(ki.get(0, END).index(value)) #on supprime le nom de la listbox
    yt = []
    for i in booster(value):
        yt.append(i)
    print(yt)
    t = open("save/box.dat", "r").read().split('\n') #récuperé box.dat et split ce qu'il y a écrit
    del t[t.index("normal")] #supprimé le premier "normal" de la liste
    open("save/box.dat", "w").write('\n'.join(t))
    if '\n'.join(t) == "":
        deck.os.remove("save/box.dat") #si il n'y a plus de booster le fichier save/box.dat et détruit
    C1 = deck.ImageTk.PhotoImage(deck.fr.card_model(yt[0])) #récupération des modèles
    CL1.configure(image=C1)
    C2 = deck.ImageTk.PhotoImage(deck.fr.card_model(yt[1]))
    CL2.configure(image=C2)
    C3 = deck.ImageTk.PhotoImage(deck.fr.card_model(yt[2]))
    CL3.configure(image=C3)
    for i in yt:
        if int(deck.card_debloque[int(i)]) == 0: #si la carte n'était pas débloqué
            if i == yt[0]:
                CLL1.configure(text=deck.lang[32]+deck.fr.name_by_nb(i))
            elif i == yt[1]:
                CLL2.configure(text=deck.lang[32]+deck.fr.name_by_nb(i))
            elif i == yt[2]:
                CLL3.configure(text=deck.lang[32]+deck.fr.name_by_nb(i))
            deck.card_debloque[int(i)] = "1" #mis à jour de la base de données des unlock
        else:
            rarity = deck.card_rarity[int(i)] #récupération de la rareté
            if rarity =="C":
                deck.Dolpe.set(deck.Dolpe.get()+10)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"10"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"10"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"10"+deck.lang[33])
            elif rarity == "O":
                deck.Dolpe.set(deck.Dolpe.get()+15)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"15"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"15"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"15"+deck.lang[33])
            elif rarity == "R":
                deck.Dolpe.set(deck.Dolpe.get()+30)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"30"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"30"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"30"+deck.lang[33])
            elif rarity == "M":
                deck.Dolpe.set(deck.Dolpe.get()+75)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"75"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"75"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"75"+deck.lang[33])
            elif rarity == "L":
                deck.Dolpe.set(deck.Dolpe.get()+150)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"150"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"150"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"150"+deck.lang[33])
    recreate_unlock() #recréation de la save
    deck.Change_Dolpe()
def recreate_unlock():
    """récréer la sauvegarde des cartes unlock """
    g= '\n'.join(deck.card_debloque)
    open("save/card.dat", "w").write(g)
def booster_op():
    """ouvrir le menu des boosters"""
    global ki, df, C1, C2, C3, CL1, CL2, CL3, CLL1, CLL2, CLL3
    sa.destroy()
    df = Canvas(deck.fenetre)
    df.pack()
    ki = Listbox(df, font=("times",13), width=20, height=20)
    ki.bind('<<ListboxSelect>>', open_booster)
    ki.grid()
    lo = Button(df, command=deck.retour, text="retour")
    lo.grid(row=1)
    C1 = deck.ImageTk.PhotoImage(deck.fr.card_model("0"))
    CL1 = Label(df, image=C1)
    C2 = deck.ImageTk.PhotoImage(deck.fr.card_model("0"))
    CL2 = Label(df, image=C2)
    C3 = deck.ImageTk.PhotoImage(deck.fr.card_model("0"))
    CL3 = Label(df, image=C3)
    CL1.grid(row=0,column=1)
    CL2.grid(row=0,column=2)
    CL3.grid(row=0,column=3)
    CLL1 = Label(df)
    CLL2 = Label(df)
    CLL3 = Label(df)
    CLL1.grid(row=1,column=1)
    CLL2.grid(row=1,column=2)
    CLL3.grid(row=1,column=3)
    if deck.os.path.isfile("save/box.dat"):
        for i in open("save/box.dat", "r").read().split('\n'):
            ki.insert(END, i)
if __name__ == '__main__':
    depart()
    deck.fenetre.start_game()