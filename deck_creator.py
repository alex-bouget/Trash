from Card import *
fr = Card()
def create(nb):
    """add a card in the deck"""
    if 'd'+str(nb) in globals():
        exec("d"+str(nb)+".configure(text=str(Tk_crea.card_deck_bdd.count("+str(nb)+")+1))")
    else:
        exec("d"+str(nb)+"= Button(Tk_crea.card_deck2, text=str(Tk_crea.card_deck_bdd.count("+str(nb)+")+1), image=photo"+str(nb)+", command= lambda: destroy("+str(nb)+"), compound='left')",globals())
        exec("d"+str(nb)+".pack()",globals())
    Tk_crea.card_deck.update_idletasks()
    Tk_crea.card_deck.configure(scrollregion=Tk_crea.card_deck.bbox('all'), yscrollcommand=Tk_crea.card_deck_bar.set)
    Tk_crea.card_deck_bdd.append(nb)
    music.play_ambiant("click.wav")
def destroy(nb):
    """remove a card in the deck"""
    if Tk_crea.card_deck_bdd.count(nb) >1:
        exec("d"+str(nb)+".configure(text=str(Tk_crea.card_deck_bdd.count("+str(nb)+")-1))")
    else:
        exec("d"+str(nb)+".destroy()",globals())
        exec("del d"+str(nb), globals())
    Tk_crea.card_deck.update_idletasks()
    Tk_crea.card_deck.configure(scrollregion=Tk_crea.card_deck.bbox('all'), yscrollcommand=Tk_crea.card_deck_bar.set)
    Tk_crea.card_deck_bdd.remove(nb)
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
    value=str(Tk_lector.var_deck_lector_listbox.get(Tk_lector.var_deck_lector_listbox.curselection()))
    try:
        for i in open("deck/"+value, "r").read().split('\n'):
            create(int(i))
        Tk_crea.name.set(value)
        r = 1
    except:
        showwarning(lang[7], lang[8]+"\n"+lang[9]+"\n"+lang[10])
        music.play_ambiant("click.wav")
        for i in Tk_crea.card_deck_bdd:
            if "d"+str(i) in globals():
                exec("d"+str(i)+".destroy()",globals())
                exec("del d"+str(i), globals())
        Tk_crea.card_deck_bdd.clear()
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
    for item in os.listdir("deck"):
        Tk_lector.var_deck_lector_listbox.insert(END, item)
    Tk_lector.var_deck_lector_listbox.bind('<<ListboxSelect>>', set_deck)
def save_deck():
    """save the deck"""
    save = []
    music.play_ambiant("click.wav")
    for i in Tk_crea.card_deck_bdd:
        save.append(str(i))
    if os.path.isfile("deck/"+Tk_crea.name.get()):
        if askokcancel(lang[3], Tk_crea.name.get()+lang[4]+'\n'+lang[5]):
            with open("deck/"+Tk_crea.name.get(), "w") as f:
                f.write('\n'.join(save))
        music.play_ambiant("click.wav")
    else:
        with open("deck/"+Tk_crea.name.get(), "w") as f:
            f.write('\n'.join(save))



Tk_crea = var_creator()
Tk_lector = var_deck_lector()
Tk_lector.var_deck_lector_button.configure(command=starting_deck)
Tk_crea.save_b.configure(command=save_deck)

for i in fr.card_all():
    exec("photo"+str(card_name.index(i))+" = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/"+str(fr.nb_by_name(i))+".png').resize((Tk_crea.px, Tk_crea.py)))")
    exec("e"+str(card_name.index(i))+"= Button(Tk_crea.every_card2, image=photo"+str(card_name.index(i))+", command= lambda: create("+str(card_name.index(i))+"))")
    exec("e"+str(card_name.index(i))+".pack()")
