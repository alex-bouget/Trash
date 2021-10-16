v = "0.10"
with open("latence.txt", "r") as r:
    latence = float(r.read())

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
#server = "http://serv001ftpsql.000webhostapp.com/Card/"
server = "http://mescouillessurtonfront.000webhostapp.com/card/"
def down_card():
    with urlopen(server+"card/v.txt") as d:
            r=d.read()
            r=r.decode()
            version=r
    print("download card ("+version+")")
    with urlopen(server+"card/"+r+"/down.txt") as d:
        r=d.read()
        r=r.decode()
        t = r.split('\n')
        for i in t:
            if i == t[0]:
                z = i.split(":/:")
                for b in z:
                    if os.path.isdir(b)==False:
                        os.mkdir(b)
            else:
                m = i.split('-->')
                print("download: "+m[1])
                urlretrieve(server+'card/'+version+"/d/"+m[0], m[1])
    with open("card/v.txt", "w") as d:
        d.write(version)
    if os.path.isfile("save/card.dat"):
        with open("save/card.dat") as arz:
            arz = arz.read()
            if ifencode("card/nb.txt"):
                are = decodefich("card/nb.txt")
                are = are.split('/')
            else:
                with open("card/nb.txt") as t:
                    are = t.read()
                are = are.split('\n/')
            arz = arz.split('\n')
            print(are)
            print(str(len(are))+" != "+str(len(arz)))
            if len(are) > len(arz):
                for i in range(len(are)):
                    try:
                        if arz[i] == "a":
                            pass
                    except:
                        arz.append("0")
                g= '\n'.join(arz)
                with open("save/card.dat", "w") as card_debloque:
                    card_debloque.write(g)

"""
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
"""
def reload_variable():
    global lang
    if not os.path.isfile("save/lang.txt"):
        with open("save/lang.txt", "w") as s:
            s.write("fr")
    with open("save/lang.txt", "r") as s:
        r = s.read()
        if r == "fr.txt":
            r="fr"
        elif r == "en.txt":
            r="en"
    with open("lang/"+r+"/system.txt","r") as s:
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
if os.path.isdir("mods")==False:
    os.mkdir("mods")
if os.path.isdir("save")==False:
    os.mkdir("save")
    with open("save/options.txt", "w") as f:
        f.write('1\n1')
if os.path.isdir("save/options.txt")==False:
    with open("save/options.txt", "w") as f:
        f.write('1\n1')
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

#__________________________________
#         Mod Variable
#__________________________________

for modv1 in os.listdir("mods"):
    if os.path.isfile("mods/"+modv1+"/Scripts/variable.py"):
        with open("mods/"+modv1+"/Scripts/variable.py", "r") as modv2:
            modv3 = modv2.read()
        exec(modv3, globals())