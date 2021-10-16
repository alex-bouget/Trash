from game.lifeclat import *
if c == 1:
    card_name = open("langS/"+lang[0]+"_name.txt", "r")
    card_att = open("card/att.txt", "r")
    card_def = open("card/def.txt", "r")
    card_nb = open("card/nb.txt", "r")
    card_cout = open("card/cout.txt", "r")
    card_effect = open("card/effect.txt", "r")
    card_rarity = open("card/rarity.txt", "r")
    card_name = card_name.read()
    card_att = card_att.read()
    card_def = card_def.read()
    card_nb = card_nb.read()
    card_cout = card_cout.read()
    card_effect = card_effect.read()
    card_rarity = card_rarity.read()
    card_name = card_name.split('\n/')
    card_att = card_att.split('\n/')
    card_def = card_def.split('\n/')
    card_nb = card_nb.split('\n/')
    card_cout = card_cout.split('\n/')
    card_effect = card_effect.split('\n/')
    card_rarity = card_rarity.split('\n/')
else:
    card_name = decodefich("langS/"+lang[0]+"_name.txt")
    card_att = decodefich("card/att.txt")
    card_def = decodefich("card/def.txt")
    card_nb = decodefich("card/nb.txt")
    card_cout = decodefich("card/cout.txt")
    card_effect = decodefich("card/effect.txt")
    card_rarity = decodefich("card/rarity.txt")
    card_name = card_name.split('/')
    card_att = card_att.split('/')
    card_def = card_def.split('/')
    card_nb = card_nb.split('/')
    card_cout = card_cout.split('/')
    card_effect = card_effect.split('/')
    card_rarity = card_rarity.split('/')
if os.path.isfile("save/card.dat")==False:
    s = open("save/card.dat", "w")
    h= []
    for i in range(len(card_nb)):
        if i == 0 or i == 1 or i ==7 or i == 14:
            h.append("1")
        else:
            h.append("0")
    s.write('\n'.join(h))
    s.close()
card_debloque = open("save/card.dat", "r")
card_debloque = card_debloque.read()
card_debloque = card_debloque.split('\n')
all_card = []
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
        self.card_tout = len(all_card)-1
    def var_for_card(self, nb):
        self.card_used = card_nb[nb]
        self.card_name = card_name[nb]
        self.card_att = card_att[nb]
        self.card_cout = card_cout[nb]
        self.card_def = card_def[nb]
        self.card_effect = card_effect[nb]
    def set_newcard_by_nb(self, nbe):
        self.var_for_card(card_nb.index(str(nbe)))
    def set_newcard_by_name(self, name):
        self.var_for_card(card_name.index(str(name)))
    def cout_carte_nb(self, nb):
        return card_cout(card_nb.index(str(nb)))
    def cout_carte_name(self, name):
        return card_cout(card_name.index(str(name)))
    def nb_by_name(self, name):
        return card_nb[card_name.index(str(name))]
    def name_by_nb(self, nb):
        return card_name[card_nb.index(str(nb))]
    def card_all(self):
        h = all_card
        del h[0]
        return(h)
class board_card:
    def __init__(self, user):
        self.names = []
        self.defs = []
        self.atts = []
        self.user = user
        self.card = Card()
        self.effect = ""
    def new_card(self, name):
        self.card.set_newcard_by_nb(name)
        self.names.append(self.card.card_name)
        self.defs.append(self.card.card_def)
        self.atts.append(self.card.card_att)
        self.effect = self.card.card_effect
        if self.user == "user":
            if self.effect != "":
                exec(self.effect)
            card_planu.me.insert(END, self.card.card_name)
            user_main.me.delete(user_main.me.get(0, END).index(self.card.card_name))
        else:
            if self.effect != "":
                exec(self.effect)
            card_plane.me.insert(END, self.card.card_name)
        self.att_carte(self.card.card_name, 0)
    def delete_carte(self, name):
        carte_data = self.names.index(name)
        del self.atts[carte_data]
        del self.defs[carte_data]
        del self.names[carte_data]
        if self.user == "user":
            card_planu.me.delete(card_planu.me.get(0, END).index(name))
        else:
            card_plane.me.delete(card_plane.me.get(0, END).index(name))
        photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/0.png'))
        Card_view.me.configure(image=photo)
    def att_carte(self, name, degats):
        self.defs[self.names.index(name)] = str(int(self.defs[self.names.index(name)])-int(degats))
        if int(self.defs[self.names.index(name)]) <= 0:
            self.delete_carte(name)
    def ulife(self, x):
        if self.user == "user":
            change_life("u", -int(x))
        else:
            change_life("e", -int(x))
    def elife(self, x):
        if self.user == "user":
            change_life("e", int(x))
        else:
            change_life("u", int(x))
    def uclat(self, x):
        if self.user == "user":
            change_eclat("u", int(x))
        else:
            change_eclat("e", int(x))
    def mylife(self):
        if self.user == "user":
            return userlife.get()
        else:
            return ennemilife.get()