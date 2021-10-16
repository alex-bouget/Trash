v = 0.7
latence = 0.2

from tkinter import *
import pytopy
from PIL import Image, ImageTk
import random
from threading import Thread
import time
from encode import *
import song


if ifencode("card/name.txt"):
    c = 0
else:
    c = 1

#__________________________________
#          SYSTEM VARIABLE
#__________________________________

fenetre = Tk()
photo = ImageTk.PhotoImage(Image.open("card/png/0.png"))

using_plan = 0
cartestr = [" "," "," ",""]
x = Canvas(fenetre, width=200, height=100)
every_deck = Listbox(x,width=20,height=20,font=('times',13))

music = song.Music()

#__________________________________
#           GAME VARIABLE
#__________________________________

clientc = pytopy.client.Client()
serveurc = pytopy.serveur.Serveur()

forclient = Canvas(fenetre, width=200, height=100)
gamec = Canvas(fenetre, width=200, height=100)
forclient1 = StringVar()
forclient2 = StringVar()

deck_use = 0

photo = ImageTk.PhotoImage(Image.open("card/png/0.png"))

Card_view = Label(gamec, image=photo)

info = StringVar()
info2 = StringVar()
infol1 = Label(gamec, text=info.get())
infol2 = Label(gamec, text=info2.get())

kernel = " "

forotherbutton = 0

buttonk = StringVar()
imme = IntVar()
ennemi_nbmain = IntVar()

user_main=Listbox(gamec,width=20,height=20,font=('times',13))
card_plane=Listbox(gamec,width=20,height=20,font=('times',13))
card_planu=Listbox(gamec,width=20,height=20,font=('times',13))

cartel = Label(gamec, text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])

ennemi_main = Label(gamec, text=str(ennemi_nbmain.get())+" carte ennemi")

#__________________________________
#       DECK CREATOR VARIABLE
#__________________________________

t = Canvas(fenetre, width=200, height=100)
every_card=Listbox(t,width=20,height=20,font=('times',13))
deck=Listbox(t,width=20,height=20,font=('times',13))
everyl = Label(t, text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
deckl = Label(t, text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
deckname = StringVar()
deckname.set("Nouveau Deck")
Card_viever = Label(t, image=photo)
decknamee = Entry(t, textvariable=deckname, width=30)
creator = Canvas(fenetre, width=200, height=100)