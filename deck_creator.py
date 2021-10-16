from tkinter import *
import card
from variable import *
from os import path
from os import listdir
from tkinter.messagebox import *

fr = card.Card()


def deckselect(evt):
    global photo, using_plan
    value=str(deck.me.get(deck.me.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout)]
    deckl.me.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_viever.me.configure(image=photo)
    using_plan = 1
def everyselect(evt):
    global photo, using_plan
    value=str(every_card.me.get(every_card.me.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout)]
    everyl.me.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_viever.me.configure(image=photo)
    using_plan = 2
def ajoute():
    if using_plan == 2:
        music.play_ambiant("click")
        deck.me.insert(END, fr.card_name)
def enleve():
    if using_plan == 1:
            music.play_ambiant("click")
            deck.me.delete(deck.me.get(0, END).index(fr.card_name))
def create_deck():
    music.play_ambiant("click")
    s = open("other_code/deck_creator2.dat", "r")
    exec(s.read())
    s.close()
def set_deck(evt):
    music.play_ambiant("click")
    value=str(every_deck.me.get(every_deck.me.curselection()))
    fichier = open("deck/"+value)
    syst = fichier.read()
    syst = syst.split('\n')
    for i in syst:
        deck.me.insert(END, i)
    x.me.destroy()
    aze = value.split('.')
    deckname.set(aze[0])
    create_deck()
def change_deck():
    music.play_ambiant("click")
    s = open("other_code/deck_creator3.dat", "r")
    exec(s.read())
    s.close()
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
    s = open("other_code/deck_creator1.dat", "r")
    exec(s.read())
    s.close()

s = open("other_code/deck_creator0.dat", "r")
exec(s.read())
s.close()