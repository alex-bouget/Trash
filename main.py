import game.start as start
import deck_creator as deck
from urllib.request import *
from tkinter import *

deck.fenetre.title("Card_Game "+str(deck.v))

class obj:
    def __init__(self, x, y, etat, cv="sa"):
        self.X = x
        self.Y = y
        self.etat = etat
        self.execute("self.me = "+self.etat+"("+cv+")")
    def create(self):
        self.me.place(x=self.X, y=self.Y)
        try:
            self.photo = deck.ImageTk.PhotoImage(self.photo)
            self.me.configure(image=self.photo)
        except:
            deck.time.sleep(0.1)
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
        self.photo = deck.Image.open(web_byte)
    def images(self, img):
        self.photo = deck.Image.open(img)
    def resize(self, x, y):
        self.photo = self.photo.resize((x, y), deck.Image.ANTIALIAS)
    def crez(self, x, y):
        if self.etat == "Canvas" or self.etat == "Listbox":
            self.me.configure(width=x, height=y)
    def font(self, ft, tl):
        self.me.configure(font=(ft,tl))

def play():
    deck.music.play_ambiant("click")
    deck.music.stop()
    sa.destroy()
    start.open_game_system()
def crea():
    deck.music.play_ambiant("click")
    deck.music.stop()
    sa.destroy()
    deck.open_creator()
def options():
    global d
    deck.music.play_ambiant("click")
    deck.music.stop()
    sa.destroy()
    d = Canvas(deck.fenetre)
    er = Button(d, text="retour", command=optionsret)
    c = Checkbutton(d, text="musique", variable=deck.opef, command=deck.musique)
    z = Checkbutton(d, text="bruit", variable=deck.g, command=deck.ambient)
    d.pack()
    c.pack()
    z.pack()
    er.pack()
def optionsret():
    d.destroy()
    depart()
def depart():
    global sa
    sa = Canvas(deck.fenetre, width=1000, height=800)
    sa.pack()
    try:
        s = urlopen("http://serv001ftpsql.000webhostapp.com/Card/menu.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        s= open("other_code/menu.dat", "r")
        exec(s.read(),globals())
    deck.music.play("main theme")
    sa.mainloop()
    deck.music.stop()

if __name__ == '__main__':
    depart()