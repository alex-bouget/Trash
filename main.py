import game
import deck_creator as deck
from tkinter import *
deck.fenetre.title("Utopia "+str(deck.v))
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
        req = deck.serv.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = deck.serv.urlopen(req)
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
    game.start_game()
def crea():
    deck.music.play_ambiant("click")
    deck.music.stop()
    sa.destroy()
    deck.start_deck_creator()
def change_lang(evt):
    value=str(g.get(g.curselection()))
    with open("save/lang.txt", "w") as s:
        s.write(value)
def options():
    global d, g
    deck.music.play_ambiant("click")
    deck.music.stop()
    sa.destroy()
    d = Canvas(deck.fenetre)
    er = Button(d, text=deck.lang[2], command=deck.retour)
    c = Checkbutton(d, text=deck.lang[34], variable=deck.play, command=deck.musique)
    z = Checkbutton(d, text=deck.lang[35], variable=deck.ambient_v, command=deck.ambient)
    g = Listbox(d)
    g.bind('<<ListboxSelect>>', change_lang)
    for item in deck.os.listdir("lang"):
        g.insert(END, item)
    d.pack()
    c.grid()
    z.grid(row=1)
    g.grid(row=2)
    er.grid(row=3)
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
def depart():
    global sa
    sa = Canvas(deck.fenetre, width=1000, height=800)
    sa.pack()
    try:
        s = deck.serv.urlopen(deck.server+"menu.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        try:
            s = deck.serv.urlopen(deck.server+"menu.txt")
            s = s.read()
            exec(s.decode(),globals())
        except:
            with open("menu.dat", "r") as f:
                exec(f.read(),globals())
def open_booster(evt):
    global C1, C2, C3
    sa.destroy()
    value = str(ki.get(ki.curselection()))
    ki.delete(ki.get(0, END).index(value))
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
                CLL1.configure(text=deck.lang[32]+i)
            elif i == yt[1]:
                CLL2.configure(text=deck.lang[32]+i)
            elif i == yt[2]:
                CLL3.configure(text=deck.lang[32]+i)
            deck.card_debloque[deck.card_name.index(i)] = "1"
        else:
            rarity = deck.card_rarity[deck.card_name.index(i)]
            if rarity =="C":
                deck.Dolpe.set(deck.Dolpe.get()+10)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"10"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"10"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"10"+deck.lang[33])
            elif rarity == "O":
                deck.Dolpe.set(deck.Dolpe.get()+15)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"15"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"15"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"15"+deck.lang[33])
            elif rarity == "R":
                deck.Dolpe.set(deck.Dolpe.get()+30)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"30"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"30"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"30"+deck.lang[33])
            elif rarity == "M":
                deck.Dolpe.set(deck.Dolpe.get()+75)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"75"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"75"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"75"+deck.lang[33])
            elif rarity == "L":
                deck.Dolpe.set(deck.Dolpe.get()+150)
                if i == yt[0]:
                    CLL1.configure(text=deck.lang[32]+"150"+deck.lang[33])
                elif i == yt[1]:
                    CLL2.configure(text=deck.lang[32]+"150"+deck.lang[33])
                elif i == yt[2]:
                    CLL3.configure(text=deck.lang[32]+"150"+deck.lang[33])
    recreate_unlock()
    deck.Change_Dolpe()
def recreate_unlock():
    g= '\n'.join(deck.card_debloque)
    with open("save/card.dat", "w") as card_debloque:
        card_debloque.write(g)
def booster_op():
    global ki, df, C1, C2, C3, CL1, CL2, CL3, CLL1, CLL2, CLL3
    sa.destroy()
    df = Canvas(deck.fenetre)
    df.pack()
    ki = Listbox(df, font=("times",13), width=20, height=20)
    ki.bind('<<ListboxSelect>>', open_booster)
    ki.grid()
    lo = Button(df, command=deck.retour, text="retour")
    lo.grid(row=1)
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
            ki.insert(END, i)
if __name__ == '__main__':
    depart()
    deck.fenetre.mainloop()