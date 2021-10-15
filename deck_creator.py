from tkinter import *
import card
from variable import *
from os import path
from os import listdir
from tkinter.messagebox import *

fr = card.Card()


def deckselect(evt):
    global photo, using_plan
    value=str(deck.get(deck.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout)]
    deckl.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_viever.configure(image=photo)
    using_plan = 1
def everyselect(evt):
    global photo, using_plan
    value=str(every_card.get(every_card.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout)]
    everyl.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_viever.configure(image=photo)
    using_plan = 2
def ajoute():
    if using_plan == 2:
        music.play_ambiant("click")
        deck.insert(END, fr.card_name)
def enleve():
    if using_plan == 1:
            music.play_ambiant("click")
            deck.delete(deck.get(0, END).index(fr.card_name))
def create_deck():
    music.play_ambiant("click")
    creator.destroy()
    t.pack()
    everyl.grid(row=0, column=0)
    every_card.grid(row=1,column=0)
    t1.grid(row=2, column=0)
    decknamee.grid(row=0,column=1)
    deckl.grid(row=0,column=2)
    deck.grid(row=1,column=2)
    t3.grid(row=2, column=1)
    t2.grid(row=2,column=2)
    Card_viever.grid(row=1,column=3)
    every_card.bind('<<ListboxSelect>>', everyselect)
    deck.bind('<<ListboxSelect>>', deckselect)
    for i in range(fr.card_tout):
        every_card.insert(END, fr.name_by_nb(i+1))
def set_deck(evt):
    music.play_ambiant("click")
    value=str(every_deck.get(every_deck.curselection()))
    fichier = open("deck/"+value)
    syst = fichier.read()
    syst = syst.split('\n')
    for i in syst:
        deck.insert(END, i)
    x.destroy()
    aze = value.split('.')
    deckname.set(aze[0])
    create_deck()
def change_deck():
    music.play_ambiant("click")
    creator.destroy()
    x.pack()
    every_deck.bind('<<ListboxSelect>>', set_deck)
    every_deck.pack()
    for item in listdir("deck"):
        every_deck.insert(END, item)
def create():
    fichier = open("deck/"+deckname.get()+".txt", "w")
    systeme = []
    for i in deck.get(0, END):
        systeme.append(i)
    fichier.write('\n'.join(systeme))
    fichier.close()
def finish():
    music.play_ambiant("click")
    if path.isfile("deck/"+deckname.get()+".txt"):
        if askokcancel("sauvegarde", deckname.get()+" existe deja\nvoulez vous le remplacez ?"):
            music.play_ambiant("click")
            create()
        else:
            music.play_ambiant("click")
    else:
        create()
def open_creator():
    creator.pack()
    l1.grid(row=0)
    l2.grid(row=1)

t1 = Button(t, text="ajouter cette carte", command=ajoute)
t2 = Button(t, text="enlever cette carte", command=enleve)
t3 = Button(t, text="Sauvegarder le deck", command=finish)
l1 = Button(creator, text="Creer Un deck", command=create_deck)
l2 = Button(creator, text="Changer Un deck", command=change_deck)