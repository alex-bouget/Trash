v = 0.9
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
server = "http://serv001ftpsql.000webhostapp.com/Card/"
def down_card():
    with urlopen(server+"card/v.txt") as d:
            r=d.read()
            r=r.decode()
            version=r
    print("download card ("+version+")")
    with urlopen(server+"card/"+r+"/down.txt") as d:
        r=d.read()
        r=r.decode()
    e=r.split('\n')
    s=0
    ss=0
    j=""
    for i in e:
        if i == "%image":#MODELE
                s=1
        elif s==1:
            if ss==0:
                j=i
                if os.path.isdir("card/png_"+j)==False:
                    os.mkdir("card/png_"+j)
                ss=1
            elif i=="end":
                s==0
                ss=0
                j=""
            else:
                print("download model "+j+": "+i)
                urlretrieve(server+"card/"+version+"/d/png_"+j+"/"+i,"card/png_"+j+"/"+i)#FIN MODELE
        elif i == "%langS":
            s=2
            if os.path.isdir("langS")==False:
                os.mkdir("langS")
        elif s==2:
            if i=="end":
                s==0
                ss=0
                j=""
            else:
                print("download pattern: "+i)
                urlretrieve(server+"card/"+version+"/d/langS/"+i,"langS/"+i)
        else:
            print("download "+i)
            urlretrieve(server+"card/"+version+"/d/"+i,"card/"+i)
    with open("card/v.txt", "w") as d:
        d.write(version)
if os.path.isfile("card/v.txt"):
    g = open("card/v.txt","r")
    g=g.read()
    try:
        d=urlopen(server+"card/v.txt")
        r=d.read()
        r=r.decode()
        if g != r:
            down_card()
    except:
        pass
else:
    if os.path.isdir("card")==False:
        os.mkdir("card")
    down_card()
def reload_variable():
    global lang
    if not os.path.isfile("save/lang.txt"):
        with open("save/lang.txt", "w") as s:
            s.write("fr.txt")
    with open("save/lang.txt", "r") as s:
        r = s.read()
    with open("lang/"+r,"r") as s:
        r = s.read()
    lang = r.split('\n')
    with open("other_code/var.dat", "r") as s:
        exec(s.read(), globals())
if ifencode("card/nb.txt"):
    c = 0
else:
    c = 1
if os.path.isdir("deck")==False:
    os.mkdir("deck")
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
    with open("save/options.txt", "w") as f:
        f.write(str(opef.get())+'\n'+str(g.get()))
def ambient():
    music.ambiant = g.get()
    with open("save/options.txt", "w") as f:
        f.write(str(opef.get())+'\n'+str(g.get()))
#__________________________________
#          SYSTEM VARIABLE
#__________________________________
if os.path.isfile("save/Dell.dat")==False:
    with open("save/Dell.dat", "w") as s:
        s.write("0")

fenetre = Tk()

Dolpe = IntVar()
def Change_Dolpe():
    with open("save/Dell.dat", "w") as s:
        s.write(str(Dolpe.get()))
with open("save/Dell.dat", "r") as s:
    Dolpe.set(int(s.read()))
using_plan = 0
cartestr = [" "," "," ",""]

music = song.Music()

#__________________________________
#           GAME VARIABLE
#__________________________________

clientc = pytopy.Client()

userlife = IntVar()
userlife.set(20)
ennemilife = IntVar()
ennemilife.set(20)

eclate = IntVar()
eclatu = IntVar()

forclient1 = StringVar()
forclient2 = StringVar()

deck_use = 0

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
photo = ""
deckname.set(lang[1])

#__________________________________
#         TKINTER VARIABLE
#__________________________________

g = IntVar()
opef = IntVar()

with open("save/options.txt", "r") as agh:
    agh = agh.read()
    agh = agh.split('\n')
    opef.set(agh[0])
    g.set(agh[1])
music.play_music=opef.get()
music.ambiant=g.get()