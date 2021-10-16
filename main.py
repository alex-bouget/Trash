import game.start as start
import deck_creator as deck
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
        req = deck.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = deck.urlopen(req)
        self.photo = deck.Image.open(web_byte)
    def images(self, img):
        self.photo = deck.Image.open(img)
    def resize(self, x, y):
        self.photo = self.photo.resize((x, y), deck.Image.ANTIALIAS)
    def crez(self, x, y):
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
def change_lang(evt):
    value=str(g.get(g.curselection()))
    with open("save/lang.txt", "w") as s:
        s.write(value)
    deck.reload_variable()
def options():
    global d, g
    deck.music.play_ambiant("click")
    deck.music.stop()
    sa.destroy()
    d = Canvas(deck.fenetre)
    er = Button(d, text=deck.lang[14], command=deck.retour)
    c = Checkbutton(d, text=deck.lang[15], variable=deck.opef, command=deck.musique)
    z = Checkbutton(d, text=deck.lang[16], variable=deck.g, command=deck.ambient)
    g = Listbox(d)
    g.bind('<<ListboxSelect>>', change_lang)
    for item in deck.os.listdir("lang"):
        g.insert(END, item)
    d.pack()
    c.grid()
    z.grid(row=1)
    g.grid(row=2)
    er.grid(row=3)
def depart():
    global sa
    sa = Canvas(deck.fenetre, width=1000, height=800)
    sa.pack()
    try:
        s = deck.urlopen(deck.server+"menu.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        s= open("other_code/menu.dat", "r")
        exec(s.read(),globals())
    deck.music.play("main theme")
    sa.mainloop()
    deck.music.stop()
def booster_rcard(common, rituel, rare, mythique, legend):
    h = deck.random.random()
    if h < common:
        f = ''
        while f!="C":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
        return deck.fr.name_by_nb(g)
    elif h < rituel+common:
        f = ''
        while f!="O":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
        return deck.fr.name_by_nb(g)
    elif h < rare+rituel+common:
        f = ''
        while f!="R":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
        return deck.fr.name_by_nb(g)
    elif h < mythique+rare+rituel+common:
        f = ''
        while f!="M":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
        return deck.fr.name_by_nb(g)
    elif h < legend+mythique+rare+rituel+common:
        f = ''
        while f!="L":
            x = deck.random.randint(1, len(deck.card_name)-1)
            f = deck.card_rarity[x]
            g = deck.card_nb[x]
        return deck.fr.name_by_nb(g)
    else:
        return booster_rcard(common, rituel, rare, mythique, legend)
def booster(l):
    s = []
    if l == "normal":
        for i in range(3):
            s.append(booster_rcard(0.4,0.4,0.11,0.06,0.03))
        t = open("save/box.dat", "r")
        t = t.read()
        t = t.split('\n')
        del t[t.index("normal")]
        x = open("save/box.dat", "w")
        x.write('\n'.join(t))
        x.close()
    elif l == "rare":
        for i in range(3):
            s.append(booster_rcard(0.35,0.25,0.20,0.15,0.05))
        t = open("save/box.dat", "r")
        t = t.read()
        t = t.split('\n')
        del t[t.index("rare")]
        x = open("save/box.dat", "w")
        x.write('\n'.join(t))
        x.close()
    elif l == "mythique":
        for i in range(3):
            s.append(booster_rcard(0.30,0.25,0.20,0.15,0.10))
        t = open("save/box.dat", "r")
        t = t.read()
        t = t.split('\n')
        del t[t.index("mythique")]
        x = open("save/box.dat", "w")
        x.write('\n'.join(t))
        x.close()
    elif l == "legende":
        for i in range(3):
            s.append(booster_rcard(0.25,0.20,0.20,0.20,0.15))
        t = open("save/box.dat", "r")
        t = t.read()
        t = t.split('\n')
        del t[t.index("legende")]
        x = open("save/box.dat", "w")
        x.write('\n'.join(t))
        x.close()
    elif l == "ultra":
        for i in range(3):
            s.append(booster_rcard(0,0,0.50,0.30,0.20))
        t = open("save/box.dat", "r")
        t = t.read()
        t = t.split('\n')
        del t[t.index("ultra")]
        x = open("save/box.dat", "w")
        x.write('\n'.join(t))
        x.close()
    else:
        return "no"
    if '\n'.join(t) == "":
        deck.os.remove("save/box.dat")
    return s
def recreate_unlock():
    g= '\n'.join(deck.card_debloque)
    with open("save/card.dat", "w") as card_debloque:
        card_debloque.write(g)
def open_booster(evt):
    global C1, C2, C3
    value = str(ki.me.get(ki.me.curselection()))
    ki.me.delete(ki.me.get(0, END).index(value))
    yt = booster(value)
    C1 = deck.ImageTk.PhotoImage(deck.Image.open("card/png_"+deck.lang[0]+"/"+deck.fr.nb_by_name(yt[0])+".png"))
    CL1.configure(image=C1)
    C2 = deck.ImageTk.PhotoImage(deck.Image.open("card/png_"+deck.lang[0]+"/"+deck.fr.nb_by_name(yt[1])+".png"))
    CL2.configure(image=C2)
    C3 = deck.ImageTk.PhotoImage(deck.Image.open("card/png_"+deck.lang[0]+"/"+deck.fr.nb_by_name(yt[2])+".png"))
    CL3.configure(image=C3)
    for i in yt:
        if int(deck.card_debloque[deck.card_name.index(i)]) == 0:
            if i == yt[0]:
                CLL1.configure(text=deck.lang[36]+i)
            elif i == yt[1]:
                CLL2.configure(text=deck.lang[36]+i)
            elif i == yt[2]:
                CLL3.configure(text=deck.lang[36]+i)
            deck.card_debloque[deck.card_name.index(i)] = "1"
        else:
            rarity = deck.card_rarity[deck.card_name.index(i)]
            if rarity =="C":
                deck.Dolpe.set(deck.Dolpe.get()+10)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[36]+"10"+deck.lang[51])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[36]+"10"+deck.lang[51])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[36]+"10"+deck.lang[51])
            elif rarity == "O":
                deck.Dolpe.set(deck.Dolpe.get()+15)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[36]+"15"+deck.lang[51])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[36]+"15"+deck.lang[51])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[36]+"15"+deck.lang[51])
            elif rarity == "R":
                deck.Dolpe.set(deck.Dolpe.get()+30)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[36]+"30"+deck.lang[51])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[36]+"30"+deck.lang[51])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[36]+"30"+deck.lang[51])
            elif rarity == "M":
                deck.Dolpe.set(deck.Dolpe.get()+75)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[36]+"75"+deck.lang[51])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[36]+"75"+deck.lang[51])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[36]+"75"+deck.lang[51])
            elif rarity == "L":
                deck.Dolpe.set(deck.Dolpe.get()+150)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[36]+"150"+deck.lang[51])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[36]+"150"+deck.lang[51])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[36]+"150"+deck.lang[51])
    recreate_unlock()
    deck.Change_Dolpe()
def booster_op():
    global ki, df, C1, C2, C3, CL1, CL2, CL3, CLL1, CLL2, CLL3
    sa.destroy()
    df = Canvas(deck.fenetre)
    df.pack()
    ki = obj(0,0, "Listbox", "df")
    ki.font("times",13)
    ki.crez(20,20)
    ki.me.bind('<<ListboxSelect>>', open_booster)
    ki.me.grid()
    lo = obj(0, 0, "Button", "df")
    lo.commande(deck.retour)
    lo.ecrire("retour")
    lo.me.grid(row=1)
    C1 = deck.ImageTk.PhotoImage(deck.Image.open("card/png_"+deck.lang[0]+"/0.png"))
    CL1 = Label(df, image=C1)
    C2 = deck.ImageTk.PhotoImage(deck.Image.open("card/png_"+deck.lang[0]+"/0.png"))
    CL2 = Label(df, image=C2)
    C3 = deck.ImageTk.PhotoImage(deck.Image.open("card/png_"+deck.lang[0]+"/0.png"))
    CL3 = Label(df, image=C3)
    CL1.grid(row=0,column=1)
    CL2.grid(row=0,column=2)
    CL3.grid(row=0,column=3)
    CLL1 = Label(df)
    CLL2 = Label(df)
    CLL3 = Label(df)
    CLL1.grid(row=1,column=1)
    CLL2.grid(row=1,column=2)
    CLL3.grid(row=1,column=3)
    if deck.os.path.isfile("save/box.dat"):
        with open("save/box.dat", "r") as s:
            r = s.read()
            r = r.split('\n')
        for i in r:
            ki.me.insert(END, i)

if __name__ == '__main__':
    depart()