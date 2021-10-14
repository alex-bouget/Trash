v = 0.1
latence = 5
#  ennemi_nbmain : nombre de carte dans la main de l'ennemi (Invar)
#  ennemi_main : endroit ou est montre le nombre de carte dans la main de l'ennemi (label)
#  user main : main de l'utilisateur (listbox) limite a 9
#  imme : etat du jeu en mode multi (serveur ou client)
#  userlife : vie de l'utilisateur
#  ennemilife : vie de l'ennemi
#  card_plane_var : variables pour l'utilisateur
#  card_plane : Board de l'ennemi
#  card_planu_var : variables pour l'utilisateur
#  card_planu : Board de l'utilisateur
#  clientc : variable pour l'utilisateur client
#  serveurc : variable pour l'utilisateur serveur
#  fr : classe des cartes
#  fenetre : fenetre principale de Tkinter
#  root : Canvas de depart
#  forclient1 : variable ou est stocke l'adresse ip du serveur
#  forclient : Canvas pour le client
#  gamec : Canvas de Combat
#  info : info donne entre les joueurs

from tkinter import *
import pytopy
import card
from PIL import Image, ImageTk
import random
from threading import Thread
import time

fr = card.Card()

fenetre = Tk()




clientc = pytopy.client.Client()
serveurc = pytopy.serveur.Serveur()


root = Canvas(fenetre, width=200, height=100)
forclient = Canvas(fenetre, width=200, height=100)
gamec = Canvas(fenetre, width=200, height=100)
forclient1 = StringVar()
forclient2 = StringVar()
root.pack()


photo = ImageTk.PhotoImage(Image.open("card/png/0.png"))

Card_view = Label(gamec, image=photo)

info = StringVar()
info2 = StringVar()
infol1 = Label(gamec, text=info.get())
infol2 = Label(gamec, text=info2.get())

forotherbutton = 0

buttonk = StringVar()
userlife = IntVar()
userlife.set(20)
ennemilife = IntVar()
ennemilife.set(20)
imme = IntVar()
ennemi_nbmain = IntVar()
user_main=Listbox(gamec,width=20,height=20,font=('times',13))
card_plane=Listbox(gamec,width=20,height=20,font=('times',13))
card_planu=Listbox(gamec,width=20,height=20,font=('times',13))
eclate = IntVar()
eclatu = IntVar()
a = 1
while a != fr.card_tout:
    user_main.insert(END, fr.name_by_nb(a))
    a = a+1
class Kernel(Thread):
    def __init__(self, etat, depart):
        Thread.__init__(self)
        self.etat = etat
        self.depart = depart
        self.suite = 0
        self.card_att = " "
        self.defd = 0
        self.click = 0
    def send(self, msg):
        if self.etat == 1:
            serveurc.server_send(msg)
        else:
            clientc.client_send(msg)
    def change_info(self, num, string):
        if num == 1:
            info.set(string)
            infol1.configure(text=info.get())
        else:
            info2.set(string)
            infol2.configure(text=info2.get())
    def change_main(self, nb):
        global ennemi_nbmain
        ennemi_nbmain.set(int(nb))
        ennemi_main.configure(text=str(ennemi_nbmain.get())+" carte ennemi")
    def change_button(self, string):
        buttonk.set(string)
        buttonb.configure(text=buttonk.get())
    def change_life(self, num, nb):
        global ennemilife, userlife
        if num == "e":
            ennemilife.set(ennemilife.get()-int(nb))
            ennemilifel.configure(text="Vie de L'ennemi: "+str(ennemilife.get()))
        else:
            userlife.set(userlife.get()-int(nb))
            userlifel.configure(text="Votre Vie: "+str(userlife.get()))
    def change_eclat(self, num, nb):
        if num == "e":
            eclate.set(eclate.get()+nb)
            ennemieclat.configure(text="Eclat Ennemi: "+str(eclate.get()))
        else:
            eclatu.set(eclatu.get()+nb)
            usereclat.configure(text="Vos Eclat: "+str(eclatu.get()))
    def vpp(self):
            self.change_info(1, "Votre Phase Principale")
            self.change_eclat("u", 1)
            self.change_button("Jouez cette carte")
            forotherbutton = 0
            while self.suite == 0:
                time.sleep(0.1)
            if self.etat == 1:
                serveurc.server_send("Phase Fini")
            else:
                clientc.client_send("Phase Fini")
    def epp(self):
        self.change_info(1, "Phase Principale Ennemi")
        self.change_eclat("e", 1)
        self.change_button(" ")
        forotherbutton = 1
        while self.suite == 0:
            if self.etat == 1:
                recu = serveurc.server_receive()
            else:
                recu = clientc.client_receive()
            if recu == "Phase Fini":
                self.suite = 1
            elif recu == "pose terrain":
                if self.etat == 1:
                    recu = serveurc.server_receive()
                else:
                    recu = clientc.client_receive()
                fr.set_newcard_by_name(recu)
                self.change_eclat("e", -int(fr.card_cout))
                card_plane_var.new_card(fr.card_name)
                if self.etat == 1:
                    recu = serveurc.server_receive()
                else:
                    recu = clientc.client_receive()
                self.change_main(recu)
    def va(self):
        self.change_info(1, "Votre Phase D'Attaque")
        self.change_button("Attaquez avec cette carte")
        forotherbutton = 0
        while self.suite == 0:
            time.sleep(0.1)
        self.send("fin")
    def ea(self):
        self.change_info(1, "Phase D'Attaque Ennemi")
        self.change_button(" ")
        forotherbutton = 1
        while self.suite == 0:
            if self.etat == 1:
                recu = serveurc.server_receive()
            else:
                recu = clientc.client_receive()
            if recu == "att":
                if self.etat == 1:
                    recu = serveurc.server_receive()
                else:
                    recu = clientc.client_receive()
                self.card_att = recu
            elif recu == "fin":
                self.suite = 1
    def defv(self):
        self.change_info(1, "DEFENDRE")
        self.change_info(2, self.card_att+" vous attaque")
        self.change_button("Defendre avec cette carte")
        forotherbutton = 0
        if len(card_planu_var.names) == 0:
            fr.set_newcard_by_name(self.card_att)
            self.change_life("u", fr.card_att)
            self.send(fr.card_att)
        else:
            if self.click == 1:
                self.suite = 1
            while self.suite == 0:
                time.sleep(0.1)
            if self.click == 0:
                if self.defd == 1:
                    carte_def = card_planu_var.names.index(fr.card_name)
                    carte_att = card_plane_var.names.index(self.card_att)
                    card_plane_var.defs[carte_att] = str(int(card_plane_var.defs[carte_att])-int(card_planu_var.atts[carte_def]))
                    card_planu_var.defs[carte_def] = str(int(card_planu_var.defs[carte_def])-int(card_plane_var.atts[carte_att]))
                    if int(card_plane_var.defs[carte_att]) <= 0:
                        card_plane.delete(card_plane.get(0, END).index(self.card_att))
                        del card_plane_var.atts[carte_att]
                        del card_plane_var.defs[carte_att]
                        del card_plane_var.names[carte_att]
                    if int(card_planu_var.defs[carte_def]) <= 0:
                        card_planu.delete(card_planu.get(0, END).index(fr.card_name))
                        del card_planu_var.atts[carte_def]
                        del card_planu_var.defs[carte_def]
                        del card_planu_var.names[carte_def]
                    self.send("fin")
                else:
                    fr.set_newcard_by_name(self.card_att)
                    self.change_life("u", fr.card_att)
                    self.send("fin")
                    time.sleep(latence)
                    self.send(fr.card_att)
            else:
                fr.set_newcard_by_name(self.card_att)
                self.change_life("u", fr.card_att)
                self.send("fin")
                time.sleep(latence)
                self.send(fr.card_att)
                self.send('stop')
        self.card_att = " "
    def defe(self):
        self.change_info(1, "L'Ennemi doit choisir la defense")
        self.change_button(" ")
        forotherbutton = 1
        if len(card_plane_var.names) == 0:
            if self.etat == 1:
                recu = serveurc.server_receive()
            else:
                recu = clientc.client_receive()
            self.change_life("e", recu)
        else:
            lol=0
            while self.suite == 0:
                if self.etat == 1:
                    recu = serveurc.server_receive()
                else:
                    recu = clientc.client_receive()
                if recu == "fin":
                    self.suite = 1
                    if lol == 0:
                        if self.etat == 1:
                            recu = serveurc.server_receive()
                        else:
                            recu = clientc.client_receive()
                        self.change_life("e", recu)
                elif recu =="def":
                    lol = 1
                    if self.etat == 1:
                        recu = serveurc.server_receive()
                    else:
                        recu = clientc.client_receive()
                    carte_def = card_plane_var.names.index(recu)
                    carte_att = card_planu_var.names.index(self.card_att)
                    card_planu_var.defs[carte_att] = str(int(card_planu_var.defs[carte_att])-int(card_plane_var.atts[carte_def]))
                    card_plane_var.defs[carte_def] = str(int(card_plane_var.defs[carte_def])-int(card_planu_var.atts[carte_att]))
                    if int(card_planu_var.defs[carte_att]) <= 0:
                        card_planu.delete(card_planu.get(0, END).index(self.card_att))
                        del card_planu_var.atts[carte_att]
                        del card_planu_var.defs[carte_att]
                        del card_planu_var.names[carte_att]
                    if int(card_plane_var.defs[carte_def]) <= 0:
                        card_plane.delete(card_plane.get(0, END).index(recu))
                        del card_plane_var.atts[carte_def]
                        del card_plane_var.defs[carte_def]
                        del card_plane_var.names[carte_def]
                elif recu =="stop":
                    self.suite = 1
        self.card_att = " "
    def run(self):
        if self.depart == "no":
            self.send(user_main.index(END))
            if self.etat == 1:
                recu = serveurc.server_receive()
            else:
                recu = clientc.client_receive()
            self.change_main(recu)
            self.vpp()
            self.suite = 0
            self.epp()
            self.suite = 0
            while userlife.get() > 0 and ennemilife.get() > 0:
                self.vpp()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                self.va()
                self.suite = 0
                self.change_info(2," ")
                if self.card_att != " ":
                    self.defe()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                if userlife.get() <= 0:
                    break
                elif ennemilife.get() <= 0:
                    break
                self.epp()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                self.ea()
                self.suite = 0
                self.change_info(2," ")
                if self.card_att != " ":
                    self.defv()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
            exit

        else:
            self.send(user_main.index(END))
            if self.etat == 1:
                recu = serveurc.server_receive()
            else:
                recu = clientc.client_receive()
            self.change_main(recu)
            self.epp()
            self.suite = 0
            self.vpp()
            self.suite = 0
            while userlife.get() > 0 and ennemilife.get() > 0:
                self.epp()
                self.suite = 0
                self.click = 0
                self.change_info(2," ")
                self.ea()
                self.suite = 0
                self.change_info(2," ")
                if self.card_att != " ":
                    self.defv()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                if userlife.get() <= 0:
                    break
                elif ennemilife.get() <= 0:
                    break
                self.vpp()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                self.va()
                self.suite = 0
                self.change_info(2," ")
                if self.card_att != " ":
                    self.defe()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
            exit


class board_card:
    def __init__(self, user):
        self.names = []
        self.defs = []
        self.atts = []
        self.user = user
    def new_card(self, name):
        fr.set_newcard_by_name(name)
        self.names.append(name)
        self.defs.append(fr.card_def)
        self.atts.append(fr.card_att)
        if self.user == "user":
            card_planu.insert(END, name)
            user_main.delete(user_main.get(0, END).index(name))
        else:
            card_plane.insert(END, name)


card_plane_var = board_card('ennemi')
card_planu_var = board_card("user")
kernel = " "
def button_click():
    value=buttonk.get()
    if value == "Jouez cette carte":
        if fr.card_used != 0:
            if eclatu.get() >= int(fr.card_cout):
                global using_plan
                if using_plan == 1:
                    klimaze = fr.card_name
                    card_planu_var.new_card(klimaze)
                    kernel.change_eclat("u", -int(fr.card_cout))
                    photo = ImageTk.PhotoImage(Image.open('card/png/0.png'))
                    Card_view.configure(image=photo)
                    using_plan = 0
                    kernel.send("pose terrain")
                    kernel.send(klimaze)
                    time.sleep(latence)
                    kernel.send(user_main.index(END))
    elif value == "Attaquez avec cette carte":
        if fr.card_used != 0:
            if using_plan == 3:
                kernel.send("att")
                time.sleep(latence)
                kernel.send(fr.card_name)
                kernel.card_att = fr.card_name
                time.sleep(latence)
                kernel.suite = 1
    elif value == "Defendre avec cette carte":
        if fr.card_used != 0:
            if using_plan == 3:
                kernel.defd = 1
                kernel.send("def")
                time.sleep(latence)
                kernel.send(fr.card_name)
                time.sleep(latence)
                kernel.send("fin")
                kernel.suite = 1





using_plan = 0
cartestr = [" "," "," "]
cartel = Label(gamec, text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])



def mainselect(evt):
    global photo
    global using_plan
    value=str(user_main.get(user_main.curselection()))
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_view.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 1
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def)]
    cartel.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])
def plane(evt):
    global photo
    global using_plan
    value=str(card_plane.get(card_plane.curselection()))
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_view.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 2
    forwait = card_plane_var.names.index(value)
    cartestr = [str(card_plane_var.names[forwait]), str(card_plane_var.atts[forwait]), str(card_plane_var.defs[forwait])]
    cartel.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])
def planu(evt):
    global photo
    global using_plan
    value=str(card_planu.get(card_planu.curselection()))
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_view.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 3
    forwait = card_planu_var.names.index(value)
    cartestr = [str(card_planu_var.names[forwait]), str(card_planu_var.atts[forwait]), str(card_planu_var.defs[forwait])]
    cartel.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])


def game_kernel():
    global kernel
    if imme.get() == 1:                              #serveur
        fenetre.title("serveur")
        serveurc.server_send("ok")
        sincro = serveurc.server_receive()
        if sincro == "ok":
            depart = random.random()
            serveurc.server_send(depart)
            if float(depart) > 0.5:
                kernel = Kernel(imme.get(), "yes")
                kernel.start()
            else:
                kernel = Kernel(imme.get(), "no")
                kernel.start()
        else:
            exit
    elif imme.get() == 2:                            #client
        fenetre.title("client")
        clientc.client_send("ok")
        sincro = clientc.client_receive()
        if sincro == "ok":
            depart = clientc.client_receive()
            if float(depart) > 0.5:
                kernel = Kernel(imme.get(), "no")
                kernel.start()
            else:
                kernel = Kernel(imme.get(), "yes")
                kernel.start()
        else:
            exit
    else:
        clientc.client_send('bug')
        serveurc.server_send('bug')
        exit
userlifel = Label(gamec, text="Votre Vie: "+str(userlife.get()))
ennemilifel = Label(gamec, text="Vie de L'ennemi: "+str(ennemilife.get()))
usereclat = Label(gamec, text="Vos ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©clat: "+str(eclatu.get()))
ennemieclat = Label(gamec, text="Eclat ennemi: "+str(eclate.get()))
ennemi_main = Label(gamec, text=str(ennemi_nbmain.get())+" carte ennemi")
def game():
    gamec.pack()
    user_main.bind('<<ListboxSelect>>', mainselect)
    card_plane.bind('<<ListboxSelect>>', plane)
    card_planu.bind('<<ListboxSelect>>', planu)
    ennemil = Label(gamec, text="Board de l'Ennemi")
    userl = Label(gamec, text="Votre Board")
    ennemi_main.grid(row=0,column=0)
    user_main.grid(row=1,column=0)
    userl.grid(row=0,column=1)
    card_planu.grid(row=1,column=1)
    ennemil.grid(row=0,column=2)
    cartel.grid(row=0,column=3)
    card_plane.grid(row=1,column=2)
    Card_view.grid(row=1,column=3)
    infol1.grid(row=2,column=0)
    userlifel.grid(row=2,column=1)
    ennemilifel.grid(row=2,column=2)
    infol2.grid(row=3,column=0)
    usereclat.grid(row=3,column=1)
    ennemieclat.grid(row=3,column=2)
    buttonb.grid(row=2,column=3)
    otherbutton.grid(row=3,column=3)
    game_kernel()


buttonb = Button(gamec, text=buttonk.get(), command=button_click)

def client_play():
    forclient.destroy()
    clientc.client_open(forclient1.get(), forclient2.get())
    clientc.client_send(str(v))
    vw = clientc.client_receive()
    if vw == str(v):
        game()
    else:
        exit

def serveur_ouvre():
    root.destroy()
    imme.set(1)
    serveurc.server_open()
    vw = serveurc.server_receive()
    if vw == str(v):
        serveurc.server_send(str(v))
        game()
    else:
        serveurc.server_send(str(v))
        exit


def client_ouvre():
    root.destroy()
    imme.set(2)
    forclient.pack()
    c1 = Label(forclient, text="Mettez l'adresse ip de l'hote")
    c2 = Entry(forclient, textvariable=forclient1)
    c3 = Label(forclient, text="Mettez le port de l'hote")
    c4 = Entry(forclient, textvariable=forclient2)
    c5 = Button(forclient, text="        se connecter         ",command=client_play)
    c1.grid(row=0, column=0)
    c2.grid(row=0, column=1)
    c3.grid(row=1)
    c4.grid(row=1, column=1)
    c5.grid(row=2)
    fenetre.mainloop()
    exit
def other_button():
    if forotherbutton == 1:
        time.sleep(0.1)
    elif forotherbutton == 0:
        kernel.suite = 1
        kernel.click = 1

otherbutton = Button(gamec, text='suivant', command=other_button)
serveur = Button(root, text="creer une partie", command=serveur_ouvre)
client = Button(root, text="rejoindre une partie", command=client_ouvre)

serveur.pack()
client.pack()

fenetre.mainloop()
exit