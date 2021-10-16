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
from urllib.request import *
from tkinter.messagebox import *
import os

def reload_variable():
    global lang
    if not os.path.isfile("lang.txt"):
        s = open("lang.txt", "w")
        s.write("fr.txt")
        s.close()
    s = open("lang.txt", "r")
    r = s.read()
    s.close()
    s = open("lang/"+r,"r")
    r = s.read()
    lang = r.split('\n')
    s= open("other_code/var.dat", "r")
    exec(s.read(), globals())
if ifencode("card/name.txt"):
    c = 0
else:
    c = 1
def retour():
    fenetre.destroy()
    os.system("cmd /c return.bat")
class obj:
    def __init__(self, x, y, etat, cv="fenetre"):
        self.X = x
        self.Y = y
        self.etat = etat
        self.execute("self.me = "+self.etat+"("+cv+")")
    def create(self):
        self.me.place(x=self.X, y=self.Y)
        try:
            self.photo = ImageTk.PhotoImage(self.photo)
            self.me.configure(image=self.photo)
        except:
            time.sleep(0.1)
    def commande(self, com):
        self.com = com
        self.me.configure(command=self.com)
    def ecrire(self, k):
        self.me.configure(text=k)
    def tvar(self,name):
        self.me.configure(textvariable=name)
    def execute(self, drg):
        exec(drg)
    def imgint(self, img):
        req = Request(img, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req)
        self.photo = Image.open(web_byte)
    def images(self, img):
        self.photo = Image.open(img)
    def resize(self, x, y):
        self.photo = self.photo.resize((x, y), Image.ANTIALIAS)
    def crez(self, x, y):
        if self.etat == "Canvas" or self.etat == "Listbox":
            self.me.configure(width=x, height=y)
    def font(self, ft, tl):
        self.me.configure(font=(ft,tl))
def musique():
    music.play_music = opef.get()
    f = open("options.txt", "w")
    f.write(str(opef.get()))
    f.write('\n')
    f.write(str(g.get()))
    f.close()
def ambient():
    music.ambiant = g.get()
    f = open("options.txt", "w")
    f.write(str(opef.get()))
    f.write('\n')
    f.write(str(g.get()))
    f.close()
#__________________________________
#          SYSTEM VARIABLE
#__________________________________

fenetre = Tk()

photo = ImageTk.PhotoImage(Image.open("card/png/0.png"))

using_plan = 0
cartestr = [" "," "," ",""]

music = song.Music()



#__________________________________
#           GAME VARIABLE
#__________________________________

clientc = pytopy.client.Client()
serveurc = pytopy.serveur.Serveur()

userlife = IntVar()
userlife.set(20)
ennemilife = IntVar()
ennemilife.set(20)

eclate = IntVar()
eclatu = IntVar()

forclient1 = StringVar()
forclient2 = StringVar()

deck_use = 0

photo = ImageTk.PhotoImage(Image.open("card/png/0.png"))


info = StringVar()
info2 = StringVar()

kernel = " "

forotherbutton = 0

buttonk = StringVar()
imme = IntVar()
ennemi_nbmain = IntVar()


#__________________________________
#       DECK CREATOR VARIABLE
#__________________________________
deckname = StringVar()

reload_variable()
deckname.set(lang[1])

#__________________________________
#         TKINTER VARIABLE
#__________________________________

agh = open("options.txt", "r")
agh = agh.read()
agh = agh.split('\n')
opef = IntVar()
opef.set(agh[0])
g = IntVar()
g.set(agh[1])
music.play_music=opef.get()
music.ambiant=g.get()