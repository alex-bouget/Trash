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
    card_desciption = codec.decode_fich("lang/"+lang[0]+"/desc.txt").split('/')
else:
    card_name = open("lang/"+lang[0]+"/name.txt", "r").read().split('/')
    card_nb = open("card/nb.txt", "r").read().split('/')
    card_att = open("card/att.txt", "r").read().split('/')
    card_rarity = open("card/rarity.txt", "r").read().split('/')
    card_def = open("card/def.txt", "r").read().split('/')
    card_cout = open("card/cout.txt", "r").read().split('/')
    card_effect = open("card/effect.txt", "r").read().split('/')
    card_desciption = open("lang/"+lang[0]+"/desc.txt", "r").read().split('/')
for i in os.listdir("mods"):
    if os.path.isdir("mods/"+i):
        for x in codec.decode_fich("mods/"+i+"/lang/"+lang[0]+"/name.txt").split('/'):
            card_name.append(x)
        for x in codec.decode_fich("mods/"+i+"/card/nb.txt").split('/'):
            card_nb.append(i+mods_nb_enter+x)
        for x in codec.decode_fich("mods/"+i+"/card/att.txt").split('/'):
            card_att.append(x)
        for x in codec.decode_fich("mods/"+i+"/card/rarity.txt").split('/'):
            card_rarity.append(x)
        for x in codec.decode_fich("mods/"+i+"/card/def.txt").split('/'):
            card_def.append(x)
        for x in codec.decode_fich("mods/"+i+"/card/cout.txt").split('/'):
            card_cout.append(x)
        for x in codec.decode_fich("mods/"+i+"/card/effect.txt").split('/'):
            card_effect.append(x)
        for x in codec.decode_fich("mods/"+i+"/lang/"+lang[0]+"/desc.txt").split('/'):
            card_desciption.append(x)
    elif zipfile.is_zipfile("mods/"+i):
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("card/nb.txt").decode()).split("/"):
            card_nb.append(i.split(".")[0]+mods_nb_enter+x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("card/att.txt").decode()).split("/"):
            card_att.append(x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("card/def.txt").decode()).split("/"):
            card_def.append(x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("card/rarity.txt").decode()).split("/"):
            card_rarity.append(x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("card/cout.txt").decode()).split("/"):
            card_cout.append(x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("card/effect.txt").decode()).split("/"):
            card_effect.append(x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("lang/"+lang[0]+"/desc.txt").decode()).split("/"):
            card_desciption.append(x)
        for x in codec.decode(zipfile.ZipFile("mods/"+i, "r").read("lang/"+lang[0]+"/name.txt").decode()).split("/"):
            card_name.append(x)
for i in card_nb:
    print(i)

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
    for i in range(len(codec.decode_fich("card/nb.txt").split('/'))):
        try:
            if card_debloque[i] == "1":
                all_card.append(str(i))
        except IndexError:
            card_debloque.append("0")
            with open("save/card.dat", "w") as f:
                f.write("\n".join(card_debloque))


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
    def card_model(self, nb):
        try:
            if len(str(nb).split(mods_nb_enter)) >= 2:
                if zipfile.is_zipfile("mods/"+str(nb.split(mods_nb_enter)[0]+".zip")):
                    tete = Image.open(BytesIO(zipfile.ZipFile("mods/"+str(nb.split(mods_nb_enter)[0])+".zip", "r").read("card/tete/"+str(nb.split(mods_nb_enter)[1])+".png"))).convert("RGBA")
                else:
                    tete = Image.open("mods/"+str(nb.split(mods_nb_enter)[0])+"/card/tete/"+str(nb.split(mods_nb_enter)[1])+".png").convert("RGBA")
            else:
                tete = Image.open("card/tete/"+str(nb)+".png").convert("RGBA")
        except FileNotFoundError:
                tete = Image.open("card/tete/error.png").convert("RGBA")
        background = Image.open("card/card/"+card_rarity[card_nb.index(str(nb))]+".png").convert("RGBA")
        if tete.size == (291,219):
            background.paste(tete, (4, 5), tete)
        else:
            background.paste(tete, (0, 0), tete)
        draw = ImageDraw.Draw(background)
        draw.text((5, 230),self.name_by_nb(nb),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        if card_rarity[card_nb.index(str(nb))] != "O":
            if card_rarity[card_nb.index(str(nb))] == "TO":
                draw.text((273, 233),card_cout[card_nb.index(str(nb))]+"E",(0,0,0),font=ImageFont.truetype("font.ttf", 12))
            elif card_rarity[card_nb.index(str(nb))] != "0":
                draw.text((15, 337),card_att[card_nb.index(str(nb))],(0,0,0),font=ImageFont.truetype("font.ttf", 48))
                draw.text((165, 337),card_def[card_nb.index(str(nb))],(0,0,0),font=ImageFont.truetype("font.ttf", 48))
                draw.text((273, 295),card_cout[card_nb.index(str(nb))]+"E",(0,0,0),font=ImageFont.truetype("font.ttf", 12))
        else:
            draw.text((273, 233),card_cout[card_nb.index(str(nb))]+"E",(0,0,0),font=ImageFont.truetype("font.ttf", 12))
        draw.text((5, 250),"\n".join(card_desciption[card_nb.index(str(nb))].split("=_=")),(0,0,0),font=ImageFont.truetype("font.ttf", 14))
        return background
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
            exec(self.effect,locals())
        self.TK.reload()
        self.att_carte(self.card.card_used, 0)
    def delete_carte(self, nb):
        carte_data = self.nb.index(nb)
        if self.nb.count(nb) >1:
            exec("self.d"+str(nb)+".configure(text=str(self.nb.count(nb)-1))")
        else:
            exec("self.d"+str(nb)+".destroy()")
        del self.atts[carte_data], self.defs[carte_data], self.nb[carte_data]
        self.TK.reload()
    def att_carte(self, nb, degats):
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
    def more_def(self, nb, inc):
        self.defs[nb] = str(int(self.defs[nb])+inc)
    def more_att(self, nb, inc):
        self.atts[nb] = str(int(self.atts[nb])+inc)


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