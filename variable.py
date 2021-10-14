from tkinter import *
import pytopy
from PIL import Image, ImageTk
import random
from threading import Thread
import time

fenetre = Tk()

using_plan = 0
cartestr = [" "," "," ",""]
x = Canvas(fenetre, width=200, height=100)
every_deck = Listbox(x,width=20,height=20,font=('times',13))

#__________________________________
#             GAME VARIABLE
#__________________________________

clientc = pytopy.client.Client()
serveurc = pytopy.serveur.Serveur()

root = Canvas(fenetre, width=200, height=100)
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
decknamee = Entry(t, textvariable=deckname, width=30)
creator = Canvas(fenetre, width=200, height=100)