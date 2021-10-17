from Card import *
import pytopy
import random

client = pytopy.Client()

ennemi_board_bdd = board_card("ennemi")
user_board_bdd = board_card("user")
user_main_bdd = main()
ennemi_main_bdd = main()

fr = Card()

class IA:
    def __init__(self):
        self.nb_pioche = 0
        self.card_att = ""
        self.card_def = ""
    def pioche(self):
        try:
            user_main_bdd.new_card(str(deck_use[self.nb_pioche]))
        except:
            print("L'ia ne peux plus piocher")
        self.nb_pioche = self.nb_pioche+1 #rajoute 1 carte piocher
    def myprincipale(self):
        self.pioche()
        eclat_Ia.set(eclat_Ia.get()+eclat_win_Ia.get())
        r = []
        for i in user_main_bdd.nb:
            r.append(i)
        for i in r:
            if "1" in card_tag[int(i)]: #gagne des eclat
                if eclat_Ia.get() >= int(fr.cout_carte_nb(i)):
                    if "3" in card_tag[int(i)] and Ia_life.get() >= 8:
                        user_main_bdd.delete_card(i)
                        eclat_Ia.set(int(eclat_Ia.get()-int(fr.cout_carte_nb(i))))
                        client.client_send(i)
                        user_board_bdd.new_card(i)
        r = []
        for i in r:
            r.append(i)
        for i in user_board_bdd.nb: #met des creatures
            if "4" in card_tag[int(i)]:
                if eclat_Ia.get() >= int(fr.cout_carte_nb(i)):
                    if "3" not in card_tag[int(i)] and Ia_life.get() >= 8:
                        user_main_bdd.delete_card(i)
                        eclat_Ia.set(int(eclat_Ia.get()-int(fr.cout_carte_nb(i))))
                        client.client_send(i)
                        user_board_bdd.new_card(i)
        r = []
        for i in user_main_bdd.nb:
            r.append(i)
        for i in r: #gagne la vie
            if "2" in card_tag[int(i)]:
                if eclat_Ia.get() >= int(fr.cout_carte_nb(i)):
                    if "3" in card_tag[int(i)] and Ia_life.get() >= 8:
                        user_main_bdd.delete_card(i)
                        eclat_Ia.set(int(eclat_Ia.get()-int(fr.cout_carte_nb(i))))
                        client.client_send(i)
                        user_board_bdd.new_card(i)
        r = []
        for i in user_main_bdd.nb:
            r.append(i)
        if len(r) != 0:
            for i in r: #detruis crea
                if "6" in card_tag[int(i)]:
                    if eclat_Ia.get() >= int(fr.cout_carte_nb(i)):
                        if "3" in card_tag[int(i)] and Ia_life.get() >= 8:
                            user_main_bdd.delete_card(i)
                            eclat_Ia.set(int(eclat_Ia.get()-int(fr.cout_carte_nb(i))))
                            client.client_send(i)
                            user_board_bdd.new_card(i)
        client.client_send("fin")
    def ennemiprincipale(self):
        ennemi_main_bdd.new_card("0")
        eclat_ennemi.set(eclat_ennemi.get()+eclat_win_ennemi.get())
        while True:
            recu = client.client_receive()
            if recu == "fin":
                break
            else:
                ennemi_board_bdd.new_card(str(recu))
                eclat_ennemi.set(eclat_ennemi.get()-int(fr.cout_carte_nb(str(recu))))
                ennemi_main_bdd.delete_card("0")
    def myattaque(self):
        if len(user_board_bdd.nb) != 0:
            if len(ennemi_board_bdd.nb) == 0:
                self.card_att = user_board_bdd.nb[user_board_bdd.atts.index(max(user_board_bdd.atts))]
            else:
                max_def = int(max(ennemi_board_bdd.defs))
                min_att_for_def = []
                for i in user_board_bdd.atts:
                    if int(i) >= max_def:
                        min_att_for_def.append(i)
                if len(min_att_for_def) != 0:
                    self.card_att = user_board_bdd.nb[user_board_bdd.atts.index(min(min_att_for_def))]
                else:
                    self.card_att = user_board_bdd.nb[user_board_bdd.atts.index(min(user_board_bdd.atts))]
            client.client_send(self.card_att)
            client.client_send("fin")
            self.ennemidefence()
    def ennemiattaque(self):
        if len(ennemi_board_bdd.nb) != 0:
            while True:
                recu = client.client_receive()
                if recu == "fin":
                    break
                else:
                    self.card_att = recu
            if self.card_att != "":
                self.mydefence()
    def mydefence(self):
        if len(user_board_bdd.nb) != 0:
            fr.set_newcard_by_nb(self.card_att)
            if fr.card_att == max(ennemi_board_bdd.atts):
                self.card_def = user_board_bdd.nb[user_board_bdd.atts.index(max(user_board_bdd.atts))]
            else:
                self.card_def = user_board_bdd.nb[user_board_bdd.atts.index(min(user_board_bdd.atts))]
            client.client_send(self.card_def)
            client.client_send("fin")
            fr.set_newcard_by_nb(self.card_def)
            user_board_bdd.att_carte(self.card_att, fr.card_att)
            fr.set_newcard_by_nb(self.card_att)
            ennemi_board_bdd.att_carte(self.card_def, fr.card_att)
        else:
            fr.set_newcard_by_nb(self.card_att)
            Ia_life.set(int(Ia_life.get())-int(fr.card_att))
        self.card_att = ""
        self.card_def = ""
    def ennemidefence(self):
        if len(ennemi_board_bdd.nb) != 0:
            while True:
                recu = self.receive()
                if recu == "fin":
                    break
                else:
                    self.card_def = recu
            if self.card_def != "":
                fr.set_newcard_by_nb(self.card_def)
                user_board_bdd.att_carte(self.card_att, fr.card_att)
                fr.set_newcard_by_nb(self.card_att)
                ennemi_board_bdd.att_carte(self.card_def, fr.card_att)
            else:
                fr.set_newcard_by_nb(self.card_att)
                ennemi_life.set(ennemi_life.get()-int(fr.card_att))
        else:
            fr.set_newcard_by_nb(self.card_att)
            ennemi_life.set(ennemi_life.get()-int(fr.card_att))
        self.card_att = ""
        self.card_def = ""
    def commence(self):
        for i in range(7):
            self.pioche()
            ennemi_main_bdd.new_card("0")
        self.myprincipale()
        self.ennemiprincipale()
        while Ia_life.get() >= 0 or ennemi_life.get() >= 0:
            self.myprincipale()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
            self.myattaque()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
            self.ennemiprincipale()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
            self.ennemiattaque()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
    def commence_pas(self):
        for i in range(7):
            self.pioche()
            ennemi_main_bdd.new_card("0")
        self.ennemiprincipale()
        self.myprincipale()
        while Ia_life.get() >= 0 or ennemi_life.get() >= 0:
            self.ennemiprincipale()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
            self.ennemiattaque()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
            self.myprincipale()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break
            self.myattaque()
            if ennemi_life.get() <= 0 or Ia_life.get() <= 0:
                break


def call_ia(ip, port, client_open, deck):
    global Ia_class, deck_use
    Ia_class = IA()
    deck_use = open(deck, "r").read().split('\n')
    random.shuffle(deck_use)
    client.client_open(ip, port)
    client.client_send("r "+str(client_open))
    if client.client_receive() == "bon":
        client.client_send(client.client_receive())
        client.client_send(client.client_receive())
        depart = random.random()
        client.client_send(depart)
        if float(depart) > float(client.client_receive()):
            Ia_class.commence_pas()
        else:
            Ia_class.commence()
        client.client_close()


if __name__ == "__main__":
    Ia_class = IA()
    deck_use = open("deck", "r").read().split('\n')
    random.shuffle(deck_use)
    print("ip:port")
    ip_port = input().split(":")
    if len(ip_port) >= 2:
        client.client_open(ip_port[0], ip_port[1])
    else:
        client.client_open(ip_port[0], '')
    print("Client cb ?")
    client_cb = input()
    client.client_send("r "+str(client_cb))
    if client.client_receive() == "bon":
        client.client_send(client.client_receive())
        client.client_send(client.client_receive())
        depart = random.random()
        client.client_send(depart)
        if float(depart) > float(client.client_receive()):
            Ia_class.commence_pas()
        else:
            Ia_class.commence()
        client.client_close()