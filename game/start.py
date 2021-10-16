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

import card
from variable import *
from game.lifeclat import *
from os import listdir

fr = card.Card()
card_plane_var = card.board_card('ennemi')
card_planu_var = card.board_card("user")

class Kernel(Thread):
    def __init__(self, etat, depart):
        Thread.__init__(self)
        self.etat = etat
        self.depart = depart
        self.suite = 0
        self.card_att = " "
        self.defd = 0
        self.click = 0
        self.tour = 0
        self.nb_pioche = 0
    def pioche(self):
        try:
            user_main.me.insert(END, str(deck_use[self.nb_pioche]))
        except:
            self.change_info(2, "Vous ne pouvez plus pioche")
        self.nb_pioche = self.nb_pioche+1
    def send(self, msg):
        if self.etat == 1:
            serveurc.server_send(msg)
        else:
            clientc.client_send(msg)
    def receive(self):
        if self.etat == 1:
            return serveurc.server_receive()
        else:
            return clientc.client_receive()
    def change_info(self, num, string):
        if num == 1:
            info.set(string)
            infol1.me.configure(text=info.get())
        else:
            info2.set(string)
            infol2.me.configure(text=info2.get())
    def change_main(self, nb):
        global ennemi_nbmain
        ennemi_nbmain.set(int(nb))
        ennemi_main.me.configure(text=str(ennemi_nbmain.get())+" carte ennemi")
    def change_button(self, string):
        buttonk.set(string)
        buttonb.me.configure(text=buttonk.get())
    def vpp(self):
            self.change_info(1, "Votre Phase Principale")
            change_eclat("u", 1)
            self.change_button("Jouez cette carte")
            forotherbutton = 0
            while self.suite == 0:
                time.sleep(0.1)
            self.send("Phase Fini")
    def epp(self):
        self.change_info(1, "Phase Principale Ennemi")
        change_eclat("e", 1)
        self.change_button(" ")
        forotherbutton = 1
        while self.suite == 0:
            recu = self.receive()
            if recu == "Phase Fini":
                self.suite = 1
            elif recu == "pose terrain":
                recu = self.receive()
                fr.set_newcard_by_name(recu)
                change_eclat("e", -int(fr.card_cout))
                card_plane_var.new_card(fr.card_name)
                recu = self.receive()
                self.change_main(recu)
                music.play_ambiant("pose")
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
            recu = self.receive()
            if recu == "att":
                recu = self.receive()
                self.card_att = recu
                music.play_ambiant("attaque")
            elif recu == "fin":
                self.suite = 1
    def defv(self): #notre defense
        self.change_info(1, "DEFENDRE")
        self.change_info(2, self.card_att+" vous attaque")
        self.change_button("Defendre avec cette carte")
        forotherbutton = 0
        if len(card_planu_var.names) == 0:
            fr.set_newcard_by_name(self.card_att)
            change_life("u", fr.card_att)
            self.send(fr.card_att)
        else:
            if self.click == 1:
                self.suite = 1
            while self.suite == 0:
                time.sleep(0.1)
            if self.click == 0:
                if self.defd == 1:
                    attb = card_plane_var.atts[card_plane_var.names.index(self.card_att)]
                    card_plane_var.att_carte(self.card_att, card_planu_var.atts[card_planu_var.names.index(fr.card_name)])
                    card_planu_var.att_carte(fr.card_name, attb)
                    self.send("fin")
                else:
                    fr.set_newcard_by_name(self.card_att)
                    change_life("u", fr.card_att)
                    self.send("fin")
                    time.sleep(latence)
                    self.send(fr.card_att)
            else:
                fr.set_newcard_by_name(self.card_att)
                change_life("u", fr.card_att)
                self.send("fin")
                time.sleep(latence)
                self.send(fr.card_att)
                self.send('stop')
        self.card_att = " "
    def defe(self): #defense par l'adversaire
        self.change_info(1, "L'Ennemi doit choisir la defense")
        self.change_button(" ")
        forotherbutton = 1
        if len(card_plane_var.names) == 0:
            recu = self.receive()
            change_life("e", recu)
        else:
            lol=0
            while self.suite == 0:
                recu = self.receive()
                if recu == "fin":
                    self.suite = 1
                    if lol == 0:
                        recu = self.receive()
                        change_life("e", recu)
                elif recu =="def":
                    lol = 1
                    recu = self.receive()
                    attb = card_planu_var.atts[card_planu_var.names.index(self.card_att)]
                    card_planu_var.att_carte(self.card_att, card_plane_var.atts[card_plane_var.names.index(recu)])
                    card_plane_var.att_carte(recu, attb)
                    music.play_ambiant("defendre")
                elif recu =="stop":
                    self.suite = 1
        self.card_att = " "
    def run(self): #systeme general
        music.play("combat", True)
        if self.depart == "no":
            for i in range(7):
                self.pioche()
            self.tour = 1
            self.send(user_main.me.index(END))
            recu = self.receive()
            self.change_main(recu)
            self.vpp()
            self.suite = 0
            self.epp()
            self.suite = 0
            while userlife.get() > 0 and ennemilife.get() > 0:
                self.tour = self.tour+1
                self.pioche()
                self.vpp()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                if len(card_planu_var.names) != 0:
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
                self.change_main(ennemi_nbmain.get()+1)
                self.epp()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                if len(card_plane_var.names) != 0:
                    self.ea()
                self.suite = 0
                self.change_info(2," ")
                if self.card_att != " ":
                    self.defv()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
        else:
            self.tour = 1
            for i in range(7):
                self.pioche()
            self.send(user_main.me.index(END))
            recu = self.receive()
            self.change_main(recu)
            self.epp()
            self.suite = 0
            self.vpp()
            self.suite = 0
            while userlife.get() > 0 and ennemilife.get() > 0:
                self.change_main(ennemi_nbmain.get()+1)
                self.epp()
                self.suite = 0
                self.click = 0
                self.change_info(2," ")
                if len(card_plane_var.names) != 0:
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
                self.tour = self.tour+1
                self.pioche()
                self.vpp()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
                if len(card_planu_var.names) != 0:
                    self.va()
                self.suite = 0
                self.change_info(2," ")
                if self.card_att != " ":
                    self.defe()
                self.suite = 0
                self.change_info(2," ")
                self.click = 0
        exit

def button_click():
    value=buttonk.get()
    if value == "Jouez cette carte":
        if fr.card_used != 0:
            if eclatu.get() >= int(fr.card_cout):
                global using_plan
                if using_plan == 1:
                    music.play_ambiant("pose")
                    klimaze = fr.card_name
                    card_planu_var.new_card(klimaze)
                    change_eclat("u", -int(fr.card_cout))
                    photo = ImageTk.PhotoImage(Image.open('card/png/0.png'))
                    Card_view.me.configure(image=photo)
                    using_plan = 0
                    kernel.send("pose terrain")
                    kernel.send(klimaze)
                    time.sleep(latence)
                    kernel.send(user_main.me.index(END))
    elif value == "Attaquez avec cette carte":
        if fr.card_used != 0:
            if using_plan == 3:
                music.play_ambiant("attaque")
                kernel.send("att")
                time.sleep(latence)
                kernel.send(fr.card_name)
                kernel.card_att = fr.card_name
                time.sleep(latence)
                kernel.suite = 1
    elif value == "Defendre avec cette carte":
        if fr.card_used != 0:
            if using_plan == 3:
                music.play_ambiant("defendre")
                kernel.defd = 1
                kernel.send("def")
                time.sleep(latence)
                kernel.send(fr.card_name)
                time.sleep(latence)
                kernel.suite = 1
def mainselect(evt):
    global photo
    global using_plan
    value=str(user_main.me.get(user_main.me.curselection()))
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_view.me.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 1
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def)]
    cartel.me.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])
def plane(evt):
    global photo
    global using_plan
    value=str(card_plane.me.get(card_plane.me.curselection()))
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_view.me.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 2
    forwait = card_plane_var.names.index(value)
    cartestr = [str(card_plane_var.names[forwait]), str(card_plane_var.atts[forwait]), str(card_plane_var.defs[forwait])]
    cartel.me.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])
def planu(evt):
    global photo
    global using_plan
    value=str(card_planu.me.get(card_planu.me.curselection()))
    photo = ImageTk.PhotoImage(Image.open('card/png/'+fr.nb_by_name(value)+'-'+value+'.png'))
    Card_view.me.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 3
    forwait = card_planu_var.names.index(value)
    cartestr = [str(card_planu_var.names[forwait]), str(card_planu_var.atts[forwait]), str(card_planu_var.defs[forwait])]
    cartel.me.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2])
def game_kernel():
    global kernel
    if imme.get() == 2:                            #client
        fenetre.title("client "+str(v))
        clientc.client_send("ok")
        sincro = clientc.client_receive()
        if sincro == "ok":
            depart = random.random()
            clientc.client_send(depart)
            departg = clientc.client_receive()
            if float(depart) > float(departg):
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
def game():
    s= open("other_code/start3.dat", "r")
    exec(s.read())
    game_kernel()
def client_play():
    music.play_ambiant("click")
    forclient.me.destroy()
    clientc.client_open(forclient1.get(), forclient2.get())
    clientc.client_send(str(v))
    vw = clientc.client_receive()
    if vw == str(v):
        game()
    else:
        exit
def client_ouvre():
    imme.set(2)
    s= open("other_code/start2.dat", "r")
    exec(s.read())
    fenetre.mainloop()
def other_button():
    if forotherbutton == 1:
        time.sleep(0.1)
    elif forotherbutton == 0:
        music.play_ambiant("click")
        kernel.suite = 1
        kernel.click = 1
def set_deck(evt):
    global deck_use
    music.play_ambiant("click")
    value=str(every_deck.me.get(every_deck.me.curselection()))
    fichier = open("deck/"+value)
    deck_use = fichier.read()
    deck_use = deck_use.split('\n')
    random.shuffle(deck_use)
    client_ouvre()
def open_game_system():
    s= open("other_code/start1.dat", "r")
    exec(s.read())
s= open("other_code/start0.dat", "r")
exec(s.read())