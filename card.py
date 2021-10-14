from tkinter import PhotoImage
card_name = open("card/name.txt", "r")
card_att = open("card/att.txt", "r")
card_def = open("card/def.txt", "r")
card_nb = open("card/nb.txt", "r")
card_cout = open("card/cout.txt", "r")
card_name = card_name.read()
card_att = card_att.read()
card_def = card_def.read()
card_nb = card_nb.read()
card_cout = card_cout.read()
card_name = card_name.split('\n')
card_att = card_att.split('\n')
card_def = card_def.split('\n')
card_nb = card_nb.split('\n')
card_cout = card_cout.split('\n')
class Card:
    def __init__(self):
        self.card_used = ""
        self.card_att = ""
        self.card_def = ""
        self.card_name = ""
        self.card_cout = ""
        self.card_tout = len(card_nb)
    def var_for_card(self, nb):
        self.card_used = card_nb[nb]
        self.card_name = card_name[nb]
        self.card_att = card_att[nb]
        self.card_cout = card_cout[nb]
        self.card_def = card_def[nb]
    def set_newcard_by_nb(self, nbe):
        Card.var_for_card(self, card_nb.index(str(nbe)))
    def set_newcard_by_name(self, name):
        Card.var_for_card(self, card_name.index(str(name)))
    def cout_carte_nb(self, nb):
        return card_cout(card_nb.index(str(nb)))
    def cout_carte_name(self, name):
        return card_cout(card_name.index(str(name)))
    def nb_by_name(self, name):
        return card_nb[card_name.index(str(name))]
    def name_by_nb(self, nb):
        return card_name[card_nb.index(str(nb))]




