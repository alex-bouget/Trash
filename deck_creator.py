from Card import *
fr = Card() #récupération de la BDD
def create(nb):
    """add a card in the deck"""
    if str(nb) in Tk_crea.card_deck_bdd: #tester si une carte du meme type à déja été mise
        exec("d"+str(nb)+".configure(text=str(Tk_crea.card_deck_bdd.count('"+str(nb)+"')+1))") #rajout d'un nombre sur cette carte
    else:
        #création d'un Boutton pour l'image
        exec("d"+str(nb)+"= Button(Tk_crea.card_deck2, text=str(Tk_crea.card_deck_bdd.count('"+str(nb)+"')+1), image=photo"+str(nb)+", command= lambda: destroy('"+str(nb)+"'), compound='left')",globals())
        exec("d"+str(nb)+".pack()",globals())
    Tk_crea.card_deck.update_idletasks() #update le frame
    Tk_crea.card_deck.configure(scrollregion=Tk_crea.card_deck.bbox('all'), yscrollcommand=Tk_crea.card_deck_bar.set) #recalcule la grandeur de scroll du frame
    Tk_crea.card_deck_bdd.append(str(nb)) #ajout de la carte dans la BDD du deck
    music.play_ambiant("click.wav")
def destroy(nb):
    """remove a card in the deck"""
    if Tk_crea.card_deck_bdd.count(nb) >1: #teste si il n'y a qu'une carte du meme type
        exec("d"+str(nb)+".configure(text=str(Tk_crea.card_deck_bdd.count('"+str(nb)+"')-1))") #enleve un nombre sur cette carte
    else:
        exec("d"+str(nb)+".destroy()",globals()) #destruction du boutton
        exec("del d"+str(nb), globals())
    Tk_crea.card_deck.update_idletasks() #update le frame
    Tk_crea.card_deck.configure(scrollregion=Tk_crea.card_deck.bbox('all'), yscrollcommand=Tk_crea.card_deck_bar.set) #recalcule la grandeur de scroll du frame
    Tk_crea.card_deck_bdd.remove(nb) #suppression de la carte dans la BDD du deck
    music.play_ambiant("click.wav")
def start_creator():
    """start creator"""
    Tk_crea.place_creator()
    Tk_crea.every_card.create_window(0, 0, anchor='nw', window=Tk_crea.every_card2)
    Tk_crea.every_card.update_idletasks()
    Tk_crea.every_card.configure(scrollregion=Tk_crea.every_card.bbox('all'), yscrollcommand=Tk_crea.every_card_bar.set)
    Tk_crea.card_deck.create_window(0, 0, anchor='nw', window=Tk_crea.card_deck2)
    Tk_crea.card_deck.update_idletasks()
    Tk_crea.card_deck.configure(scrollregion=Tk_crea.card_deck.bbox('all'), yscrollcommand=Tk_crea.card_deck_bar.set)
def set_deck(evt):
    value=str(Tk_lector.var_deck_lector_listbox.get(Tk_lector.var_deck_lector_listbox.curselection())) #récuperation du nom du deck
    try:
        for i in open("deck/"+value, "r").read().split('\n'): #création des cartes déja présent dans le deck
            create(int(i))
        Tk_crea.name.set(value) #ajout du nom du deck
        r = 1
    except:
        #si le deck est corrompu ou qu'une carte n'existe pas
        showwarning(lang[7], lang[8]+"\n"+lang[9]+"\n"+lang[10])
        music.play_ambiant("click.wav")
        for i in Tk_crea.card_deck_bdd: #pour tout les cartes dans la BDD du deck si elle n'ont pas déja été détruite sont détruit
            if "d"+str(i) in globals():
                exec("d"+str(i)+".destroy()",globals())
                exec("del d"+str(i), globals())
        Tk_crea.card_deck_bdd.clear() #suppression de toute la liste
    if r == 1:
        starting_deck()
def starting_deck():
    """open creator with lector"""
    music.play_ambiant("click.wav")
    Tk_lector.var_deck_lector.destroy()
    start_creator()
def start_deck_creator():
    """starting deck creator"""
    Tk_lector.place_lector()
    for item in os.listdir("deck"): #récuperation de tout les deck
        Tk_lector.var_deck_lector_listbox.insert(END, item)
    Tk_lector.var_deck_lector_listbox.bind('<<ListboxSelect>>', set_deck)
def save_deck():
    """save the deck"""
    temp = []
    for i in Tk_crea.card_deck_bdd:
        temp.append(str(i))
    music.play_ambiant("click.wav")
    if os.path.isfile("deck/"+Tk_crea.name.get()): #si le deck existe déja
        if askokcancel(lang[3], Tk_crea.name.get()+lang[4]+'\n'+lang[5]): #demandé si on veut écrasé l'ancien deck
            open("deck/"+Tk_crea.name.get(), "w").write('\n'.join(temp)) #écriture
        music.play_ambiant("click.wav")
    else:
        open("deck/"+Tk_crea.name.get(), "w").write('\n'.join(temp)) #écriture



Tk_crea = var_creator() #récupération des menus complexes
Tk_lector = var_deck_lector()
Tk_lector.var_deck_lector_button.configure(command=starting_deck)
Tk_crea.save_b.configure(command=save_deck)

print(fr.card_all())
for i in card_nb: #création des modèles des cartes débloqué et des cartes moddés
    if i in fr.card_all() or i.split(mods_nb_enter)[0] in os.listdir("mods") or i.split(mods_nb_enter)[0]+".zip" in os.listdir("mods"):
        exec("photo"+str(i)+" = ImageTk.PhotoImage(fr.card_model('"+str(i)+"').resize((Tk_crea.px, Tk_crea.py)))")
        exec("e"+str(i)+"= Button(Tk_crea.every_card2, image=photo"+str(i)+", command= lambda: create('"+str(i)+"'))")
        exec("e"+str(i)+".pack()")