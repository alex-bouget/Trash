"""ennemi_nbmain : nombre de carte dans la main de l'ennemi (Invar)
ennemi_main : endroit ou est montre le nombre de carte dans la main de l'ennemi (label)
user main : main de l'utilisateur (listbox) limite a 9
imme : etat du jeu en mode multi (serveur ou client)
userlife : vie de l'utilisateur
ennemilife : vie de l'ennemi
card_plane_var : variables pour l'utilisateur
card_plane : Board de l'ennemi
card_planu_var : variables pour l'utilisateur
card_planu : Board de l'utilisateur
clientc : variable pour l'utilisateur client
serveurc : variable pour l'utilisateur serveur
fr : classe des cartes
fenetre : fenetre principale de Tkinter
root : Canvas de depart
forclient1 : variable ou est stocke l'adresse ip du serveur
forclient : Canvas pour le client
gamec : Canvas de Combat
info : info donne entre les joueurs"""
from card import *

fr = Card() #classe pour les cartes
card_plane_var = board_card('ennemi') #classe pour le board ennemi
card_planu_var = board_card("user") #classe pour votre board

class Kernel(Thread):
    """Thread donnant les phase de jeu
    et communication avec le serv (a moitiÃ©)
    %VAR% = Kernel(depart)
    depart = "yes" ou "no" """
    def __init__(self, depart):
        Thread.__init__(self)
        self.depart = depart #donne la persone qui commence
        self.suite = 0 #continuer en enlevent les boucle
        self.card_att = " " #carte attaquante (pour les fonction defense
        self.defd = 0
        self.click = 0
        self.tour = 0
        self.nb_pioche = 0 #numero de carte pioche
    def pioche(self):
        """piocher une carte"""
        try:
            user_main.me.insert(END, str(deck_use[self.nb_pioche])) #montrer la carte dans la listbox
        except:
            self.change_info(2, lang[25]) #vous ne pouvez plus piocher
        self.nb_pioche = self.nb_pioche+1 #rajoute 1 carte piocher
    def send(self, msg):
        """envoyer des message au serveur"""
        clientc.client_send(msg)
    def receive(self):
        """recevoir des message du serveur"""
        return clientc.client_receive()
    def change_info(self, num, string):
        """changer les infos
        self.change_info(num, string)
        num = 1 ou 2 (numero du label)
        string = "" (message)"""
        if num == 1:
            info.set(string)
            infol1.me.configure(text=info.get())
        else:
            info2.set(string)
            infol2.me.configure(text=info2.get())
    def change_main(self, nb):
        """Changer le nombre de carte ennemi dans le label
        self.change_main(nb)
        nb = nombre de carte
        """
        global ennemi_nbmain
        ennemi_nbmain.set(int(nb)) #changer la variable
        ennemi_main.me.configure(text=str(ennemi_nbmain.get())+lang[3]) #ecrire dans le label
    def change_button(self, string):
        """changer le texte du bouton
        self.change_button(string)
        string = texte"""
        buttonk.set(string) #variable pour savoir ce qu'il y a ecrit dans le bouton (voir utilisation a button_click)
        buttonb.me.configure(text=buttonk.get()) #mettre le texte dans le bouton
    def vpp(self):
        """Votre Phase Principale
        boucle d'attente pour que l'utilisateur choisisse
        """
        self.change_info(1, lang[26]) #met l'info de la Phase principale
        change_eclat("u", 1) #rajoute 1 eclat
        self.change_button(lang[27]) #met la possibilite de jouer des cartes
        forotherbutton = 0 #utilisation du 2eme bouton (suivant)
        while self.suite == 0: #boucle d'attente
            time.sleep(0.1)
        self.send("Phase Fini") #donne a l'ennemi la possibilite de passer la phase
    def epp(self):
        """Phase Principale
        boucle d'attente et de traitement des informations recue"""
        self.change_info(1, lang[28]) #met l'info de la Phase principale ennemi
        change_eclat("e", 1) #rajoute 1 eclat a l'ennemi
        self.change_button(" ") #n'ecris rien dans le boutton (pour le bloque)
        forotherbutton = 1 #bloque le boutton suivant
        while self.suite == 0: #boucle d'attente
            recu = self.receive() #attendre des info du serveur
            if recu == "Phase Fini": #arreter la boucle
                self.suite = 1
            elif recu == "pose terrain":
                """pose terrain est envoyer quand l'ennemi pose une carte
                suite des recu :
                    pose terrain ---> numero de la carte jouer ---> nombre de carte dans la main de l'ennemi"""
                fr.set_newcard_by_nb(self.receive()) #recuperer les infos de la carte
                change_eclat("e", -int(fr.card_cout)) #enlever les eclats ennemi
                card_plane_var.new_card(fr.card_used) #rajouter une carte dans les variables
                self.change_main(self.receive()) #changer le nombre de carte dans la main de l'ennemi
                music.play_ambiant("pose") #joue un son
                self.change_info(2, lang[54]+fr.card_name) #donne l'info de la carte jouer
    def va(self):
        """ Votre Phase d'attaque"""
        self.change_info(1, lang[29]) #donne l'info
        self.change_button(lang[30]) #donne le droit d'attaquer
        forotherbutton = 0 #debloque suivant (pour pas jouer)
        while self.suite == 0: #boucle d'attente
            time.sleep(0.1)
        self.send("fin") #donne a l'ennemi la possibilite de passer la phase
    def ea(self):
        """ Phase d'attaque ennemi"""
        self.change_info(1, lang[31]) #donne l'info
        self.change_button(" ") #bloque les boutons
        forotherbutton = 1
        while self.suite == 0: #boucle
            recu = self.receive()
            if recu == "att":
                """ une carte attaque
                suite des recu:
                    att --> numero de la carte
                """
                self.card_att = fr.name_by_nb(self.receive()) #recuperer le nom de la carte
                music.play_ambiant("attaque")
            elif recu == "fin": #arreter la boucle
                self.suite = 1
    def defv(self):
        """ Votre Phase de defense"""
        self.change_info(1, lang[44]) #donne l'info de la phase
        self.change_info(2, self.card_att+lang[32]) #donne quels carte nous attaque
        self.change_button(lang[33]) #debloque boutton
        forotherbutton = 0
        if len(card_planu_var.names) == 0: #si vous n'avez pas de cartes
            fr.set_newcard_by_name(self.card_att) #recuperer les infos de la carte
            change_life("u", fr.card_att) #enlever de la vie
            self.send(fr.card_att) #envoyer l'attaque de la carte
        else:
            if self.click == 1:
                self.suite = 1
            while self.suite == 0: #boucle d'attente
                time.sleep(0.1)
            if self.click == 0: #si vous defendez
                attb = card_plane_var.atts[card_plane_var.names.index(self.card_att)] #recuperer l'attaque de l'attaquant
                card_plane_var.att_carte(self.card_att, card_planu_var.atts[card_planu_var.names.index(fr.card_name)]) #attaquer l'attaquant
                card_planu_var.att_carte(fr.card_name, attb) #attaquer le defendeur
                self.send("fin")
            else:
                fr.set_newcard_by_name(self.card_att) #recuperer les infos de la carte
                change_life("u", fr.card_att) #enlever de la vie
                self.send("fin")
                time.sleep(latence)
                self.send(fr.card_att) #envoyer l'attaque
        self.card_att = " "
    def defe(self):
        """Phase de defense de l'adversaire"""
        self.change_info(1, lang[34])
        self.change_button(" ")#bloquer les boutton
        forotherbutton = 1
        if len(card_plane_var.names) == 0: #si l'ennemi n'a pas de carte
            change_life("e", self.receive())
        else:
            lol=0
            while self.suite == 0: #boucle
                recu = self.receive()
                if recu == "fin":
                    self.suite = 1
                    if lol == 0:
                        change_life("e", self.receive()) #enlever de la vie a l'ennemi
                elif recu =="def":
                    """une carte defend
                    suite des recu:
                        def ---> numero de carte"""
                    lol = 1 #pour ne pas enlever de la vie
                    #pour la suite voir defv()
                    recu = fr.name_by_nb(self.receive())
                    attb = card_planu_var.atts[card_planu_var.names.index(self.card_att)]
                    card_planu_var.att_carte(self.card_att, card_plane_var.atts[card_plane_var.names.index(recu)])
                    card_plane_var.att_carte(recu, attb)
                    music.play_ambiant("defendre")
        self.card_att = " "
    def run(self):
        """commencer le Thread"""
        music.play("combat", True)
        if self.depart == "no":
            for i in range(7):
                self.pioche()
            self.tour = 1
            self.send(user_main.me.index(END))
            self.change_main(self.receive())
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
            self.change_main(self.receive())
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
        if userlife.get() <= 0:
            print(lang[35])
            create_booster()
        elif ennemilife.get() <=0:
            print(lang[36])
            for i in range(4):
                print(lang[49]+create_booster()+lang[50])
        exit
    for modv1 in os.listdir("mods"):
        if os.path.isfile("mods/"+modv1+"/Scripts/Kernel.py"):
            with open("mods/"+modv1+"/Scripts/Kernel.py", "r") as modv2:
                modv3 = modv2.read()
            exec(modv3)
def create_booster():
    """creer des booster"""
    s = []
    if os.path.isfile("save/box.dat"):
        s = open("save/box.dat", "r")
        s = s.read()
        s = s.split('\n')
    x = open("save/box.dat", "w")
    t = random.random()
    if t > 0.50:
        s.append("normal")
        s = '\n'.join(s)
        x.write(s)
        x.close()
        return "normal"
    elif t > 0.30:
        s.append("rare")
        s = '\n'.join(s)
        x.write(s)
        x.close()
        return "rare"
    elif t > 0.15:
        s.append("mythique")
        s = '\n'.join(s)
        x.write(s)
        x.close()
        return "mythique"
    elif t > 0.04:
        s.append("legende")
        s = '\n'.join(s)
        x.write(s)
        x.close()
        return "legende"
    elif t > 0.01:
        s.append("ultra")
        s = '\n'.join(s)
        x.write(s)
        x.close()
        return "ultra"
    else:
        create_booster()
def ret():
    """retourner au menu"""
    if not kernel.isAlive():
        music.stop()
        clientc.client_close()
        retour()
    else:
        showwarning(lang[37], lang[38]+"\n"+lang[42]+"\n"+lang[43])
def button_click():
    """boutton d'evenement cliquez"""
    value=buttonk.get() #recuperez l'evenement
    if value == lang[27]: #poser des carte
        if fr.card_used != 0: #si la carte pris n'est pas " "
            if eclatu.get() >= int(fr.card_cout): #si on peut payer la carte
                global using_plan
                if using_plan == 1: #si on a pris une carte dans notre main
                    music.play_ambiant("pose")
                    klimaze = fr.card_used
                    card_planu_var.new_card(klimaze)
                    change_eclat("u", -int(fr.card_cout))
                    photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/0.png'))
                    Card_view.me.configure(image=photo)
                    using_plan = 0
                    kernel.send("pose terrain")
                    time.sleep(latence)
                    kernel.send(klimaze)
                    time.sleep(latence)
                    kernel.send(user_main.me.index(END))
                    kernel.change_info(2, lang[55]+fr.name_by_nb(klimaze))
    elif value == lang[30]: #attaque
        if fr.card_used != 0:
            if using_plan == 3:
                music.play_ambiant("attaque")
                kernel.send("att")
                time.sleep(latence)
                kernel.send(fr.card_used)
                kernel.card_att = fr.card_name
                time.sleep(latence)
                kernel.suite = 1
    elif value == lang[33]: #defense
        if fr.card_used != 0:
            if using_plan == 3:
                music.play_ambiant("defendre")
                kernel.defd = 1
                kernel.send("def")
                time.sleep(latence)
                kernel.send(fr.card_used)
                time.sleep(latence)
                kernel.suite = 1
    else:
        for modv1 in os.listdir("mods"):
            if os.path.isfile("mods/"+modv1+"/Scripts/button_click.py"):
                with open("mods/"+modv1+"/Scripts/button_click.py", "r") as modv2:
                    modv3 = modv2.read()
                exec(modv3, globals())
def mainselect(evt):
    global photo
    global using_plan
    value=str(user_main.me.get(user_main.me.curselection()))
    try:
        photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/'+fr.nb_by_name(value)+'.png'))
    except:
        for sei in os.listdir("mods"):
            if os.path.isfile("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"):
                photo = ImageTk.PhotoImage(Image.open("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"))
    Card_view.me.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 1
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def)]
    cartel.me.configure(text=cartestr[0]+lang[2]+cartestr[1]+"/"+cartestr[2])
def plane(evt):
    global photo
    global using_plan
    value=str(card_plane.me.get(card_plane.me.curselection()))
    try:
        photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/'+fr.nb_by_name(value)+'.png'))
    except:
        for sei in os.listdir("mods"):
            if os.path.isfile("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"):
                photo = ImageTk.PhotoImage(Image.open("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"))
    Card_view.me.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 2
    forwait = card_plane_var.names.index(value)
    cartestr = [str(card_plane_var.names[forwait]), str(card_plane_var.atts[forwait]), str(card_plane_var.defs[forwait])]
    cartel.me.configure(text=cartestr[0]+lang[2]+cartestr[1]+"/"+cartestr[2])
def planu(evt):
    global photo
    global using_plan
    value=str(card_planu.me.get(card_planu.me.curselection()))
    try:
        photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/'+fr.nb_by_name(value)+'.png'))
    except:
        for sei in os.listdir("mods"):
            if os.path.isfile("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"):
                photo = ImageTk.PhotoImage(Image.open("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"))
    Card_view.me.configure(image=photo)
    fr.set_newcard_by_name(value)
    using_plan = 3
    forwait = card_planu_var.names.index(value)
    cartestr = [str(card_planu_var.names[forwait]), str(card_planu_var.atts[forwait]), str(card_planu_var.defs[forwait])]
    cartel.me.configure(text=cartestr[0]+lang[3]+cartestr[1]+"/"+cartestr[2])
def game_kernel():
    global kernel
    fenetre.title("client "+str(v))
    clientc.client_send("ok")
    if clientc.client_receive() == "ok":
        depart = random.random()
        clientc.client_send(depart)
        if float(depart) > float(clientc.client_receive()):
            kernel = Kernel("no")
            kernel.start()
        else:
            kernel = Kernel("yes")
            kernel.start()
    else:
        exit
def game():
    try:
        s = urlopen(server+"start3.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        if c == 1:
            s= open("other_code/start3.dat", "r")
            exec(s.read())
        else:
            s=decodefich("other_code/start3.dat")
            exec(s)
    for modv1 in os.listdir("mods"):
        if os.path.isfile("mods/"+modv1+"/Scripts/start3.py"):
            with open("mods/"+modv1+"/Scripts/start3.py", "r") as modv2:
                modv3 = modv2.read()
            exec(modv3, globals())
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
    try:
        s = urlopen(server+"start2.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        if c == 1:
            s= open("other_code/start2.dat", "r")
            exec(s.read())
        else:
            s=decodefich("other_code/start2.dat")
            exec(s)
    for modv1 in os.listdir("mods"):
        if os.path.isfile("mods/"+modv1+"/Scripts/start2.py"):
            with open("mods/"+modv1+"/Scripts/start2.py", "r") as modv2:
                modv3 = modv2.read()
            exec(modv3, globals())
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
    deck_us = fichier.read()
    deck_us = deck_us.split('\n')
    deck_use = []
    hgjtdf=0
    for i in deck_us:
        try:
            if card_debloque[int(i)] != "1":
                showerror(lang[52], lang[53]+fr.name_by_nb(i))
                hgjtdf=1
                ret()
        except:
            if hgjtdf==1:
                ret()
            else:
                pass
        try:
            deck_use.append(fr.name_by_nb(i))
        except:
            showerror(lang[45], lang[47]+'\n'+lang[48])
            ret()
    random.shuffle(deck_use)
    client_ouvre()
def open_game_system():
    try:
        s = urlopen(server+"start1.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        if c == 1:
            s= open("other_code/start1.dat", "r")
            exec(s.read())
        else:
            s=decodefich("other_code/start1.dat")
            exec(s)
    for item in os.listdir("deck"):
        every_deck.me.insert(END, item)
    for modv1 in os.listdir("mods"):
        if os.path.isfile("mods/"+modv1+"/Scripts/start1.py"):
            with open("mods/"+modv1+"/Scripts/start1.py", "r") as modv2:
                modv3 = modv2.read()
            exec(modv3, globals())
try:
    s = urlopen(server+"start0.txt")
    s = s.read()
    exec(s.decode(),globals())
except:
    if c == 1:
        s= open("other_code/start0.dat", "r")
        exec(s.read())
    else:
        s=decodefich("other_code/start0.dat")
        exec(s)
for modv1 in os.listdir("mods"):
    if os.path.isfile("mods/"+modv1+"/Scripts/start0.py"):
        with open("mods/"+modv1+"/Scripts/start0.py", "r") as modv2:
            modv3 = modv2.read()
        exec(modv3, globals())