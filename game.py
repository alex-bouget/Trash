from Card import *

fr = Card()
Tk_game = var_game()
Tk_lector = var_deck_lector()
Tk_serv = var_serv()
ME = ['']

def board_ennemi(nb):
    if kernel.myturn == 1:
        if Tk_game.info1.get() == lang[40]:
            kernel.depart = str(nb)
            kernel.turn = False
def board_user(nb):
    global ME
    if ME[0] == str(nb):
        if Tk_game.info1.get() == lang[26]:
            kernel.card_att = str(nb)
            kernel.send(str(nb))
            time.sleep(latence)
            kernel.turn = False
        elif Tk_game.info1.get() == lang[28]:
            kernel.send(str(nb))
            kernel.card_def = str(nb)
            kernel.defs = True
            time.sleep(latence)
            kernel.turn = False
        ME = [""]
        Tk_game.reload_var()
    else:
        ME = [str(nb)]
        Tk_game.ME.configure(text=fr.name_by_nb(nb)+","+str(user_board_bdd.atts[user_board_bdd.nb.index(nb)])+"/"+str(user_board_bdd.defs[user_board_bdd.nb.index(nb)]))


def main_user(nb):
    nb = str(nb)
    if Tk_game.info1.get() == lang[22]:
        if int(fr.cout_carte_nb(nb)) <= int(eclat_user.get()):
            user_main_bdd.delete_card(nb)
            eclat_user.set(int(int(eclat_user.get())-int(fr.cout_carte_nb(nb))))
            kernel.send(str(nb))
            kernel.change_info(2, lang[24]+fr.name_by_nb(str(nb)))
            kernel.rt_si_t_a_compris = nb
            Tk_game.reload_var()
    Tk_game.reload_var()
def main_ennemi(nb):
    pass
def other_button():
    if kernel.myturn == 1:
        kernel.myturn = 0
        kernel.turn = False
ennemi_board_bdd = board_card("ennemi", Tk_game.board_ennemi2, Tk_game, board_ennemi)
user_board_bdd = board_card("user", Tk_game.board_user2, Tk_game, board_user)
user_main_bdd = main(Tk_game.user_main2, Tk_game, main_user)
ennemi_main_bdd = main(Tk_game.ennemi_main2, Tk_game, main_ennemi)
Tk_game.suivant.configure(command=other_button)

class Kernel(Thread):
    """Thread donnant les phase de jeu
    et communication avec le serv (a moitier)
    %VAR% = Kernel(depart)
    depart = "yes" ou "no" """
    def __init__(self):
        Thread.__init__(self)
        self.depart = "" #donne la persone qui commence
        self.nb_pioche = 0 #numero de carte pioche
        self.myturn = 0
        self.turn = True
        self.card_att = ""
        self.defs = False
        self.card_def = ""
        self.rt_si_t_a_compris = ""
    def pioche(self):
        """piocher une carte"""
        try:
            user_main_bdd.new_card(str(fr.nb_by_name(deck_use[self.nb_pioche])))
        except:
            self.change_info(2, lang[21]) #vous ne pouvez plus piocher
        self.nb_pioche = self.nb_pioche+1 #rajoute 1 carte piocher
        Tk_game.reload()
    def send(self, msg):
        """envoyer des message au serveur"""
        client.client_send(msg)
    def receive(self):
        """recevoir des message du serveur"""
        return client.client_receive()
    def change_info(self, num, string):
        """changer les infos
        self.change_info(num, string)
        num = 1 ou 2 (numero du label)
        string = "" (message)"""
        if num == 1:
            Tk_game.info1.set(string)
        else:
            Tk_game.info2.set(string)
    def your_phase_principale(self):
        self.change_info(1, lang[22])
        self.myturn = 1
        self.pioche()
        eclat_user.set(eclat_user.get()+eclat_user_win.get())
        Tk_game.reload_var()
        while self.turn:
            time.sleep(0.1)
            if self.rt_si_t_a_compris != "":
                user_board_bdd.new_card(self.rt_si_t_a_compris)
                if user_board_bdd.destroy_u == "yes":
                    self.change_info(1, lang[40])
                    while self.turn:
                        time.sleep(0.1)
                    if self.depart != "":
                        ennemi_board_bdd.delete_carte(self.depart)
                    self.send(self.depart)
                    self.depart = ""
                    self.turn = True
                user_board_bdd.destroy_u = "NO FUCK YOU"
                self.change_info(1, lang[22])
                Tk_game.reload_var()
            self.rt_si_t_a_compris = ""
        self.turn = True
        self.send("fin")
    def ennemi_phase_principale(self):
        self.change_info(1, lang[23])
        self.myturn = 0
        ennemi_main_bdd.new_card("0")
        eclat_ennemi.set(eclat_ennemi.get()+eclat_ennemi_win.get())
        Tk_game.reload_var()
        while self.turn:
            recu = self.receive()
            if recu == "fin":
                self.turn = False
            else:
                ennemi_board_bdd.new_card(str(recu))
                if ennemi_board_bdd.destroy_u == "yes":
                    self.change_info(1, lang[40])
                    recu = self.receive()
                    if recu != "":
                        user_board_bdd.delete_carte(recu)
                    ennemi_board_bdd.destroy_u = "NO FUCK YOU"
                    self.change_info(1, lang[23])
                eclat_ennemi.set(eclat_ennemi.get()-int(fr.cout_carte_nb(recu)))
                ennemi_main_bdd.delete_card("0")
                kernel.change_info(2, lang[25]+fr.name_by_nb(str(recu)))
                Tk_game.reload_var()
        self.turn = True
    def your_phase_attaque(self):
        if len(user_board_bdd.nb) != 0:
            self.change_info(1, lang[26])
            self.myturn = 1
            while self.turn:
                time.sleep(0.1)
            self.turn = True
            time.sleep(latence)
            self.send("fin")
            if self.card_att != "":
                self.ennemi_phase_defense()
    def ennemi_phase_attaque(self):
        if len(ennemi_board_bdd.nb) != 0:
            self.change_info(1, lang[27])
            self.myturn = 0
            while self.turn:
                recu = self.receive()
                if recu == "fin":
                    self.turn = False
                else:
                    self.card_att = recu
            self.turn = True
            if self.card_att != "":
                self.your_phase_defense()
    def your_phase_defense(self):
        if len(user_board_bdd.nb) != 0:
            self.change_info(1, lang[28])
            self.change_info(2, fr.name_by_nb(self.card_att)+lang[30])
            self.myturn = 1
            if user_board_bdd.nb != []:
                while self.turn:
                    time.sleep(0.1)
            self.turn = True
            time.sleep(latence)
            self.send("fin")
            if self.defs == True:
                fr.set_newcard_by_nb(self.card_def)
                ennemi_board_bdd.att_carte(self.card_att, fr.card_att)
                fr.set_newcard_by_nb(self.card_att)
                user_board_bdd.att_carte(self.card_def, fr.card_att)
            else:
                fr.set_newcard_by_nb(self.card_att)
                user_life.set(int(user_life.get())-int(fr.card_att))
                Tk_game.reload_var()
        else:
            fr.set_newcard_by_nb(self.card_att)
            user_life.set(int(user_life.get())-int(fr.card_att))
            Tk_game.reload_var()
        self.card_att = ""
        self.card_def = ""
        self.defs = False
    def ennemi_phase_defense(self):
        if len(ennemi_board_bdd.nb) != 0:
            self.change_info(1, lang[29])
            self.change_info(2, fr.name_by_nb(self.card_att)+lang[31])
            if ennemi_board_bdd.nb != []:
                while self.turn:
                    recu = self.receive()
                    if recu == "fin":
                        self.turn = False
                    else:
                        self.defs = True
                        self.card_def = recu
            self.turn = True
            if self.defs == True:
                fr.set_newcard_by_nb(self.card_def)
                user_board_bdd.att_carte(self.card_att, fr.card_att)
                fr.set_newcard_by_nb(self.card_att)
                ennemi_board_bdd.att_carte(self.card_def, fr.card_att)
            else:
                fr.set_newcard_by_nb(self.card_att)
                ennemi_life.set(int(ennemi_life.get())-int(fr.card_att))
                Tk_game.reload_var()
        else:
            fr.set_newcard_by_nb(self.card_att)
            ennemi_life.set(int(ennemi_life.get())-int(fr.card_att))
            Tk_game.reload_var()
        self.card_att = ""
        self.card_def = ""
        self.defs = False
    def run(self):
        self.send(str(v))
        if self.receive() == str(v):
            time.sleep(latence)
            self.send("ok")
            if self.receive() == "ok":
                depart = random.random()
                self.send(depart)
                if float(depart) > float(self.receive()):
                    self.depart = "no"
                else:
                    self.depart = "yes"
        else:
            showerror(lang[18], lang[19]+"\n"+lang[20])
        for i in range(7):
            self.pioche()
            ennemi_main_bdd.new_card("0")
        if self.depart == "yes":
            self.depart = ""
            self.your_phase_principale()
            self.ennemi_phase_principale()
            while ennemi_life.get() > 0 or user_life.get() > 0:
                self.your_phase_principale()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
                self.your_phase_attaque()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
                self.ennemi_phase_principale()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
                self.ennemi_phase_attaque()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
        else:
            self.depart = ""
            self.ennemi_phase_principale()
            self.your_phase_principale()
            while ennemi_life.get() > 0 or user_life.get() > 0:
                self.ennemi_phase_principale()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
                self.ennemi_phase_attaque()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
                self.your_phase_principale()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
                self.your_phase_attaque()
                if ennemi_life.get() <= 0 or user_life.get() <= 0:
                    break
        if user_life.get() <= 0:
            print(lang[35])
            create_booster()
        elif ennemi_life.get() <=0:
            print(lang[36])
            for i in range(4):
                print(lang[49]+create_booster()+lang[50])
        client.client_close()
        retour()
"""_________________________________________________________________________________________________________"""
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
def starting_system():
    global kernel
    client.client_open(server_ip.get(), server_port.get())
    Tk_serv.choice_serv.destroy()
    Tk_game.place_game()
    Tk_game.reload()
    Tk_game.reload_var()
    kernel = Kernel()
    kernel.start()
def set_deck(evt):
    global deck_use
    deck_use = []
    x=0
    value=str(Tk_lector.var_deck_lector_listbox.get(Tk_lector.var_deck_lector_listbox.curselection()))
    for i in open("deck/"+value, "r").read().split('\n'):
        if fr.name_by_nb(i) in all_card:
            deck_use.append(fr.name_by_nb(i))
        else:
            showwarning(lang[7], lang[8]+"\n"+lang[9]+"\n"+lang[10])
            deck_use = []
            x=1
            break
    if x==0:
        random.shuffle(deck_use)
        Tk_lector.var_deck_lector.destroy()
        Tk_serv.place_serv()
        Tk_serv.choice_serv_button.configure(command=starting_system)
def start_game():
    Tk_lector.place_lector()
    Tk_lector.var_deck_lector_button.destroy()
    for item in os.listdir("deck"):
        Tk_lector.var_deck_lector_listbox.insert(END, item)
    Tk_lector.var_deck_lector_listbox.bind('<<ListboxSelect>>', set_deck)

for i in card_name:
    exec("Tk_game.photo"+str(card_name.index(i))+" = ImageTk.PhotoImage(fr.card_model("+str(fr.nb_by_name(i))+").resize((Tk_game.px, Tk_game.py)))")
"""
Tk_game.place_game()
for i in range(10):
    for i in card_nb:
        if i != card_nb[0] :
            user_main_bdd.new_card(i)
            ennemi_main_bdd.new_card(i)
Tk_game.reload_var()
Tk_game.reload()
fenetre.mainloop()
"""
if __name__ == "__main__":
    start_game()
    fenetre.mainloop()