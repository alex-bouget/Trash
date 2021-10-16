"""BDD de carte pour Utopia"""
from variable import *
if encodesys:
    card_name = codec.decode_fich("lang/"+lang[0]+"/name.txt").split('/')
    card_nb = codec.decode_fich("card/nb.txt").split('/')
    card_att = codec.decode_fich("card/att.txt").split('/')
    card_rarity = codec.decode_fich("card/rarity.txt").split('/')
    card_def = codec.decode_fich("card/def.txt").split('/')
    card_cout = codec.decode_fich("card/cout.txt").split('/')
    card_effect = codec.decode_fich("card/effect.txt").split('/')
else:
    card_name = open("lang/"+lang[0]+"/name.txt", "r").read().split('/')
    card_nb = open("card/nb.txt", "r").read().split('/')
    card_att = open("card/att.txt", "r").read().split('/')
    card_rarity = open("card/rarity.txt", "r").read().split('/')
    card_def = open("card/def.txt", "r").read().split('/')
    card_cout = open("card/cout.txt", "r").read().split('/')
    card_effect = open("card/effect.txt", "r").read().split('/')

all_card = []
if os.path.isfile("save/card.dat")==False:
    pute=[]
    for i in range(len(card_nb)):
        if i == 1 or i ==7 or i == 14:
            pute.append("1")
        else:
            pute.append("0")
    with open("save/card.dat", "w") as f:
        f.write("\n".join(pute))

with open("save/card.dat", "r") as s:
    card_debloque = s.read().split('\n')
    for i in range(len(card_debloque)):
        if card_debloque[i] == "1":
            all_card.append(card_name[i])

class Card:
    def __init__(self):
        self.card_used = ""
        self.card_att = ""
        self.card_def = ""
        self.card_name = ""
        self.card_effect = ""
        self.card_cout = ""
        self.card_rarity = ""
        self.card_tout = len(all_card)-1
    def var_for_card(self, nb):
        self.card_used = card_nb[nb]
        self.card_name = card_name[nb]
        self.card_att = card_att[nb]
        self.card_cout = card_cout[nb]
        self.card_def = card_def[nb]
        self.card_effect = card_effect[nb]
        self.card_rarity = card_rarity[nb]
    def set_newcard_by_nb(self, nbe):
        self.var_for_card(card_nb.index(str(nbe)))
    def set_newcard_by_name(self, name):
        self.var_for_card(card_name.index(str(name)))
    def cout_carte_nb(self, nb):
        return card_cout[card_nb.index(str(nb))]
    def cout_carte_name(self, name):
        return card_cout[card_name.index(str(name))]
    def nb_by_name(self, name):
        return card_nb[card_name.index(str(name))]
    def name_by_nb(self, nb):
        return card_name[card_nb.index(str(nb))]
    def card_all(self):
        h = all_card
        return(h)
class board_card:
    def __init__(self, user, board_enter, Tk_g, click):
        self.nb = []
        self.defs = []
        self.atts = []
        self.user = user
        self.card = Card()
        self.board = board_enter
        self.TK = Tk_g
        self.click = click
        self.effect = ""
        self.destroy_u = ""
    def new_card(self, nb):
        if self.nb.count(nb) >= 1:
            exec("self.d"+str(nb)+".configure(text=str(self.nb.count(nb)+1))")
        else:
            r = lambda: self.click_card(str(nb))
            exec("self.d"+str(nb)+"= Button(self.board, text=str(self.nb.count(nb)+1), image=self.TK.photo"+str(nb)+", command=r, compound='left')")
            exec("self.d"+str(nb)+".pack(side=LEFT)")
        self.card.set_newcard_by_nb(nb)
        self.nb.append(nb)
        self.defs.append(self.card.card_def)
        self.atts.append(self.card.card_att)
        self.effect = self.card.card_effect
        if self.effect != "":
            exec(self.effect)
        self.TK.reload()
        self.att_carte(self.card.card_used, 0)
        print(nb[-1])
    def delete_carte(self, nb):
        carte_data = self.nb.index(nb)
        if self.nb.count(nb) >1:
            exec("self.d"+str(nb)+".configure(text=str(self.nb.count(nb)-1))")
        else:
            exec("self.d"+str(nb)+".destroy()")
        del self.atts[carte_data], self.defs[carte_data], self.nb[carte_data]
        self.TK.reload()
    def att_carte(self, nb, degats):
        print(nb)
        self.defs[self.nb.index(nb)] = str(int(self.defs[self.nb.index(nb)])-int(degats))
        if int(self.defs[self.nb.index(nb)]) <= 0:
            self.delete_carte(nb)
    def click_card(self, nb):
        self.click(nb)
    """ EFFET DE CARTE: PAS TOUCHE"""
    def ulife(self, x):
        if self.user == "user":
            user_life.set(user_life.get()+int(x))
        else:
            ennemi_life.set(ennemi_life.get()+int(x))
        self.TK.reload_var()
    def elife(self, x):
        if self.user == "user":
            ennemi_life.set(ennemi_life.get()-int(x))
        else:
            user_life.set(user_life.get()-int(x))
        self.TK.reload_var()
    def uclat(self, x):
        if self.user == "user":
            eclat_user.set(eclat_user.get()+int(x))
        else:
            eclat_ennemi.set(eclat_ennemi.get()+int(x))
        self.TK.reload_var()
    def mylife(self):
        if self.user == "user":
            return user_life.get()
        else:
            return ennemi_life.get()
    def win_eclat(self, x):
        if self.user == "user":
            eclat_user_win.set(eclat_user_win.get()+int(x))
            if eclat_user_win.get() <= 0:
                eclat_user_win.set(1)
        else:
            eclat_ennemi_win.set(eclat_ennemi_win.get()+int(x))
            if eclat_ennemi_win.get() <= 0:
                eclat_ennemi_win.set(1)
    def destroy(self):
        self.destroy_u = "yes"


class main():
    def __init__(self, board_enter, Tk_g, click):
        self.nb = []
        self.board = board_enter
        self.TK = Tk_g
        self.click = click
    def new_card(self, nb):
        if self.nb.count(nb) >= 1:
            exec("self.d"+str(nb)+".configure(text=str(self.nb.count(nb)+1))")
        else:
            r = lambda: self.click_card(str(nb))
            exec("self.d"+str(nb)+"= Button(self.board, text=str(self.nb.count(nb)+1), image=self.TK.photo"+str(nb)+", command=r, compound='left')")
            exec("self.d"+str(nb)+".pack()")
        self.nb.append(nb)
        self.TK.reload()
    def delete_card(self, nb):
        if self.nb.count(nb) >1:
            exec("self.d"+str(nb)+".configure(text=str(self.nb.count(nb)-1))")
        else:
            exec("self.d"+str(nb)+".destroy()")
        self.nb.remove(nb)
        self.TK.reload()
    def click_card(self, nb):
        self.click(nb)