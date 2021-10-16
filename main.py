import game.start as start
import deck_creator as deck
from urllib.request import *
from tkinter import *

sa = Canvas(deck.fenetre, width=1000, height=800)
sa.pack()
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
    def ecrire(self, t):
        self.me.configure(text=t)
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

if __name__ == '__main__':
    try:
        s = urlopen("http://serv001ftpsql.000webhostapp.com/Card/menu.txt")
        s = s.read()
        exec(s.decode())
    except:
        s= open("menu.txt", "r")
        exec(s.read())
    deck.music.play("main theme")
    sa.mainloop()
    deck.music.stop()