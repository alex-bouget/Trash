"""BDD de carte pour Utopia"""
import codec

import urllib.request as serv
import os

server = "http://utopia-card.000webhostapp.com/Card/"
def down_card():
    """Mise a jour des cartes"""
    with serv.urlopen(server+"card/v.txt") as d:
        version=d.read().decode()
    print("download card ("+version+")")
    with serv.urlopen(server+"card/"+version+"/down.txt") as d:
        systeme = d.read().decode().split('\n')
    for i in systeme:
        if i == systeme[0]:
            directory = i.split(":/:")
            for create in directory:
                if os.path.isdir(create)==False:
                    os.mkdir(create)
        else:
            download = i.split('-->')
            print("download: "+download[1])
            try:
                serv.urlretrieve(server+'card/'+version+"/d/"+download[0], download[1])
            except:
                try:
                    serv.urlretrieve(server+'card/'+version+"/d/"+download[0], download[1])
                except:
                    serv.urlretrieve(server+'card/'+version+"/d/"+download[0], download[1])
    with open("card/v.txt", "w") as d:
        d.write(version)

class IntVar():
    def __init__(self, nb=0):
        self.me = nb
    def get(self):
        return self.me
    def set(self, nb):
        self.me = nb

if codec.ifencode("card/nb.txt"):
    card_nb = codec.decode_fich("card/nb.txt").split('/')
    card_att = codec.decode_fich("card/att.txt").split('/')
    card_rarity = codec.decode_fich("card/rarity.txt").split('/')
    card_def = codec.decode_fich("card/def.txt").split('/')
    card_cout = codec.decode_fich("card/cout.txt").split('/')
    card_effect = codec.decode_fich("card/effect.txt").split('/')
else:
    card_nb = open("card/nb.txt", "r").read().split('/')
    card_att = open("card/att.txt", "r").read().split('/')
    card_rarity = open("card/rarity.txt", "r").read().split('/')
    card_def = open("card/def.txt", "r").read().split('/')
    card_cout = open("card/cout.txt", "r").read().split('/')
    card_effect = open("card/effect.txt", "r").read().split('/')

card_tag = []
for i in open("card/tag_card.txt", "r").read().split("\n"):
    card_tag.append(i.split(","))

eclat_win_Ia = IntVar(1)
eclat_win_ennemi = IntVar(1)

Ia_life = IntVar(20)
ennemi_life = IntVar(20)

eclat_Ia = IntVar()
eclat_ennemi = IntVar()

class Card:
    def __init__(self):
        self.card_used = ""
        self.card_att = ""
        self.card_def = ""
        self.card_name = ""
        self.card_effect = ""
        self.card_cout = ""
        self.card_rarity = ""
    def var_for_card(self, nb):
        self.card_used = card_nb[nb]
        self.card_att = card_att[nb]
        self.card_cout = card_cout[nb]
        self.card_def = card_def[nb]
        self.card_effect = card_effect[nb]
        self.card_rarity = card_rarity[nb]
    def set_newcard_by_nb(self, nbe):
        self.var_for_card(card_nb.index(str(nbe)))
    def cout_carte_nb(self, nb):
        return card_cout[card_nb.index(str(nb))]
    def name_by_nb(self, nb):
        return card_name[card_nb.index(str(nb))]
class board_card:
    def __init__(self, user):
        self.nb = []
        self.defs = []
        self.atts = []
        self.user = user
        self.card = Card()
        self.effect = ""
        self.destroy_u = ""
    def new_card(self, nb):
        self.card.set_newcard_by_nb(nb)
        self.nb.append(nb)
        self.defs.append(self.card.card_def)
        self.atts.append(self.card.card_att)
        self.effect = self.card.card_effect
        if self.effect != "":
            exec(self.effect,locals())
        self.att_carte(self.card.card_used, 0)
    def delete_carte(self, nb):
        carte_data = self.nb.index(nb)
        del self.atts[carte_data], self.defs[carte_data], self.nb[carte_data]
    def att_carte(self, nb, degats):
        self.defs[self.nb.index(nb)] = str(int(self.defs[self.nb.index(nb)])-int(degats))
        if int(self.defs[self.nb.index(nb)]) <= 0:
            self.delete_carte(nb)
    """ EFFET DE CARTE: PAS TOUCHE"""
    def ulife(self, x):
        if self.user == "user":
            Ia_life.set(Ia_life.get()+int(x))
        else:
            ennemi_life.set(ennemi_life.get()+int(x))
    def elife(self, x):
        if self.user == "user":
            ennemi_life.set(ennemi_life.get()-int(x))
        else:
            Ia_life.set(Ia_life.get()-int(x))
    def uclat(self, x):
        if self.user == "user":
            eclat_Ia.set(eclat_Ia.get()+int(x))
        else:
            eclat_ennemi.set(eclat_ennemi.get()+int(x))
    def mylife(self):
        if self.user == "user":
            return Ia_life.get()
        else:
            return ennemi_life.get()
    def win_eclat(self, x):
        if self.user == "user":
            eclat_win_Ia.set(eclat_win_Ia.get()+int(x))
            if eclat_win_Ia.get() <= 0:
                eclat_win_Ia.set(1)
        else:
            eclat_win_ennemi.set(eclat_win_ennemi.get()+int(x))
            if eclat_win_ennemi.get() <= 0:
                eclat_win_ennemi.set(1)
    def destroy(self):
        self.destroy_u = "yes"
    def more_def(self, nb, inc):
        self.defs[nb] = str(int(self.defs[nb])+inc)
    def more_att(self, nb, inc):
        self.atts[nb] = str(int(self.atts[nb])+inc)


class main():
    def __init__(self):
        self.nb = []
    def new_card(self, nb):
        self.nb.append(nb)
        print(self.nb)
    def delete_card(self, nb):
        self.nb.remove(nb)
        print(self.nb)

if os.path.isfile("card/v.txt"):
    with open("card/v.txt", "r") as t:
        var_version = t.read()
    try:
        try:
            var_version_s=serv.urlopen(server+"card/v.txt").read().decode()
        except:
            try:
                var_version_s=serv.urlopen(server+"card/v.txt").read().decode()
            except:
                var_version_s=serv.urlopen(server+"card/v.txt").read().decode()
        if var_version != var_version_s:
            down_card()
    except:
        pass
else:
    if os.path.isdir("card")==False:
        os.mkdir("card")
    down_card()

