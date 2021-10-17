"""v : version du jeu
fenetre : fenetre principale
Dolpe : monnaie de jeu
music : class pour musique
client : systeme principale pour les sockets
user_life : vie du joueur
ennemi_life : vie de l'ennemi
eclat_user : eclat du joueur
eclat_ennemi eclat de l'ennemi
server_ip : ip du serveur
server_port : port du serveur
deck_use : dictionnaire des cartes du deck (pour la pioche)
info : barre d'info 1
info2 : barre d'info 2
button_play : fonction du bouton principale
ennemi_nbmain : nombre de carte dans la main de l'ennemi
lang : dictionnaire des phrases demande par le jeu
encode_sys : si la bdd est encoder"""
v = "1.0"

import fich_crea

TK_x = int(open("save/resolution.txt", "r").read())
TK_y = int(TK_x*(2/3))

from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk, ImageFont, ImageDraw
import random
from threading import Thread
import time
import codec
import song
import urllib.request as serv
import os
import pytopy
import numpy as np
import Motor

server = "http://utopia-card.000webhostapp.com/Card/"
def down_card():
    """Mise a jour des cartes"""
    with serv.urlopen(server+"card/v.txt") as d:
        version=d.read().decode()
    print("download card ("+version+")")
    with serv.urlopen(server+"card/"+version+"/down.txt") as d:
        systeme = d.read().decode().split('\n')
    print(systeme)
    for i in systeme:
        print(i)
        if i == systeme[0]:
            directory = i.split(":/:")
            for create in directory:
                if os.path.isdir(create)==False:
                    os.mkdir(create)
        else:
            download = i.split('-->')
            print(download)
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
def retour():
    """retour"""
    fenetre.root.destroy()
    os.system("cmd /c return.bat")

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

if codec.ifencode("card/nb.txt"):
    encodesys = 1
else:
    encodesys = 0

fenetre = Motor.Engine("Utopia "+v, TK_x, TK_y)
"""
fenetre = Tk()
fenetre.geometry("%dx%d+0+0" % (TK_x, TK_y))
fenetre.iconphoto(False, PhotoImage(file="icone2.png"))
"""

Dolpe = IntVar()
def Change_Dolpe():
    """Changer le nombre de Dolpe dans la sauvegarde"""
    with open("save/Dell.dat", "w") as s:
        s.write(str(Dolpe.get()))
with open("save/Dell.dat", "r") as s:
    Dolpe.set(int(s.read()))
music = song.Music()
play = IntVar()
ambient_v = IntVar()
def musique():
    music.play_music = play.get()
    with open("save/options.txt", "w") as f:
        f.write(str(music.play_music)+'\n'+str(music.ambiant))
def ambient():
    music.ambiant = ambient_v.get()
    with open("save/options.txt", "w") as f:
        f.write(str(music.play_music)+'\n'+str(music.ambiant))

#__________________________________
#           GAME VARIABLE
#__________________________________

client = pytopy.Client()

user_life = IntVar()
user_life.set(20)
ennemi_life = IntVar()
ennemi_life.set(20)

eclat_ennemi = IntVar()
eclat_user = IntVar()

eclat_ennemi_win = IntVar()
eclat_user_win = IntVar()
eclat_ennemi_win.set(1)
eclat_user_win.set(1)

kernel = ""

server_ip = StringVar()
server_port = StringVar()

deck_use = []

button_play = StringVar()

ennemi_nbmain = IntVar()


#__________________________________
#         TKINTER VARIABLE
#__________________________________

with open("save/options.txt", "r") as agh:
    agh = agh.read().split('\n')
    music.play_music=agh[0]
    music.ambiant=agh[1]

if not os.path.isfile("save/lang.txt"):
    with open("save/lang.txt", "w") as s:
        s.write("en")

with open("save/lang.txt", "r") as s:
    with open("lang/"+s.read()+"/system.txt","r") as s:
        lang = s.read().split('\n')


class var_creator:
    def __init__(self):
        self.card_deck_bdd = []
        self.px = int(TK_x*(1/3))
        self.py = int(self.px*float(1.32))
        self.name = StringVar()
        self.name.set(lang[1])
        self.creator = Canvas(fenetre, width=TK_x, height=TK_y)
        self.every_card = Canvas(self.creator, height=TK_y, width=self.px+20)
        self.every_card_bar = Scrollbar(self.every_card, orient="vertical", command=self.every_card.yview)
        self.every_card2 = Frame(self.every_card)
        self.card_deck = Canvas(self.creator, height=TK_y, width=self.px+40)
        self.card_deck_bar = Scrollbar(self.card_deck, orient="vertical", command=self.card_deck.yview)
        self.card_deck2 = Frame(self.card_deck)
        self.ret = Button(self.creator, command=retour, text=lang[2])
        self.deck_name = Entry(self.creator, textvariable=self.name)
        self.save_b = Button(self.creator, text=lang[3])
    def place_creator(self):
        self.creator.pack()
        self.every_card.place(x=0,y=0)
        self.card_deck.place(x=TK_x-(self.px+45),y=0)
        self.card_deck_bar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.every_card_bar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.ret.place(x=(TK_x//2)-30, y=TK_y//1.2)
        self.deck_name.place(x=(TK_x//2.25)-30, y=TK_y//10)
        self.save_b.place(x=(TK_x//2.25)-30, y=TK_y//5)
class var_deck_lector:
    def __init__(self):
        self.var_deck_lector = Canvas(fenetre, height=TK_x, width=TK_y)
        self.var_deck_lector_listbox = Listbox(self.var_deck_lector, height=TK_x//30, width=TK_y)
        self.var_deck_lector_button = Button(self.var_deck_lector, text=lang[6])
    def place_lector(self):
        self.var_deck_lector.place(x=0, y=0)
        self.var_deck_lector_button.place(x=0, y=TK_y-30)
        self.var_deck_lector_listbox.place(x=0,y=0)
class var_game:
    def __init__(self):
        self.px = (TK_x//4)-40
        self.py = int(self.px*float(1.32))
        self.game = Canvas(fenetre, width=TK_x, height=TK_y)
        self.user_main = Canvas(self.game, width=TK_x//4, height=TK_y, bg="blue")
        self.user_main2 = Frame(self.user_main, bg="blue")
        self.user_main_bar = Scrollbar(self.user_main, orient="vertical", command=self.user_main.yview)
        self.ennemi_main = Canvas(self.game, width=TK_x//4, height=TK_y, bg="red")
        self.ennemi_main2 = Frame(self.ennemi_main, bg="red")
        self.ennemi_main_bar = Scrollbar(self.ennemi_main, orient="vertical", command=self.ennemi_main.yview)
        self.board_user = Canvas(self.game, width=(TK_x//4)*2, height=TK_y//2-35, bg="violet")
        self.board_user2 = Frame(self.board_user, bg="violet")
        self.board_user_bar = Scrollbar(self.board_user, orient="horizontal", command=self.board_user.xview)
        self.board_ennemi = Canvas(self.game, width=(TK_x//4)*2, height=TK_y//2-35, bg="green")
        self.board_ennemi2 = Frame(self.board_ennemi, bg="green")
        self.board_ennemi_bar = Scrollbar(self.board_ennemi, orient="horizontal", command=self.board_ennemi.xview)
        self.info1 = StringVar()
        self.info2 = StringVar()

        self.info_photo = Image.open("card/info.png").convert("RGBA")
        self.info_photo_draw = ImageDraw.Draw(self.info_photo)

        self.info_canvas = Label(self.game, width=(TK_x//4)*2, height=60)


        self.photo_suivant = ImageTk.PhotoImage(Image.open("suivant.png").resize((100,100)))
        self.suivant = Button(self.game, image=self.photo_suivant)
        self.help_card = Canvas(self.game, width=(TK_x//4)*2, height=10)
        self.ME = Label(self.help_card)
    def place_game(self):
        self.game.place(x=0,y=0)
        self.user_main.place(x=0,y=0)
        self.user_main_bar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.board_ennemi.place(x=TK_x//4,y=0)
        self.board_ennemi_bar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        self.board_user.place(x=TK_x//4,y=TK_y//2-30)
        self.board_user_bar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        self.ennemi_main.place(x=TK_x-(TK_x//4),y=0)
        self.ennemi_main_bar.place(relx=1, rely=0, relheight=1, anchor='ne')

        self.info_canvas.place(x=TK_x//4,y=TK_y-61)


        self.suivant.place(x=TK_x-120, y=TK_y-100)
        self.help_card.place(x=TK_x//4, y=0)
        self.ME.place(x=0, y=0)
        self.board_ennemi.create_window(0, 0, anchor='nw', window=self.board_ennemi2)
        self.user_main.create_window(0, 0, anchor='nw', window=self.user_main2)
        self.ennemi_main.create_window(0, 0, anchor='nw', window=self.ennemi_main2)
        self.board_user.create_window(0, 0, anchor='nw', window=self.board_user2)
    def reload(self):
        self.user_main.update_idletasks()
        self.user_main.configure(scrollregion=self.user_main.bbox('all'), yscrollcommand=self.user_main_bar.set)
        self.ennemi_main.update_idletasks()
        self.ennemi_main.configure(scrollregion=self.ennemi_main.bbox('all'), yscrollcommand=self.ennemi_main_bar.set)
        self.board_user.update_idletasks()
        self.board_user.configure(scrollregion=self.board_user.bbox('all'), xscrollcommand=self.board_user_bar.set)
        self.board_ennemi.update_idletasks()
        self.board_ennemi.configure(scrollregion=self.board_ennemi.bbox('all'), xscrollcommand=self.board_ennemi_bar.set)
    def reload_var(self):
        self.info_photo = Image.open("card/info.png").convert("RGBA")
        self.info_photo_draw = ImageDraw.Draw(self.info_photo)
        self.info_photo_draw.text((0, 0),self.info1.get(),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        self.info_photo_draw.text((0, 30),self.info2.get(),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        self.info_photo_draw.text((270, 0),lang[11]+str(user_life.get()),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        self.info_photo_draw.text((270, 30),lang[12]+str(ennemi_life.get()),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        self.info_photo_draw.text((430, 0),lang[13]+str(eclat_user.get()),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        self.info_photo_draw.text((430, 30),lang[14]+str(eclat_ennemi.get()),(0,0,0),font=ImageFont.truetype("font.ttf", 16))
        self.info_photo_tk = ImageTk.PhotoImage(self.info_photo.resize((TK_x//4*2, 60)))
        self.info_canvas.configure(image=self.info_photo_tk)
class var_serv:
    def __init__(self):
        self.choice_serv = Canvas(fenetre, width=TK_x, height=TK_y)
        self.choice_serv_ip = Entry(self.choice_serv, textvariable=server_ip)
        self.choice_serv_ip_l = Label(self.choice_serv, text=lang[15])
        self.choice_serv_port = Entry(self.choice_serv, textvariable=server_port)
        self.choice_serv_port_l = Label(self.choice_serv, text=lang[16])
        self.choice_serv_button = Button(self.choice_serv, text=lang[17])
    def place_serv(self):
        self.choice_serv.place(x=0,y=0)
        self.choice_serv_ip_l.place(x=TK_x//4, y=TK_y//4)
        self.choice_serv_ip.place(x=TK_x//2, y=TK_y//4)
        self.choice_serv_port_l.place(x=TK_x//4, y=TK_y//2)
        self.choice_serv_port.place(x=TK_x//2, y=TK_y//2)
        self.choice_serv_button.place(x=TK_x//3.5, y=TK_y//1.5)
class ennemi:
    def __init__(self):
        self.ennemi_can = Canvas(fenetre, width=TK_x, height=TK_y)
        self.ennemi_choice = StringVar()
        self.ennemi_all_choice = [None]
        self.choice = OptionMenu(self.ennemi_can, self.ennemi_choice, *self.ennemi_all_choice)
        self.rafraich = Button(self.ennemi_can, text="rafraichir")
        self.finish = Button(self.ennemi_can, text="choice")
    def place_ennemi(self):
        self.ennemi_can.place(x=0, y=0)
        self.choice.place(x=TK_x//2, y=TK_y//4)
        self.finish.place(x=TK_x//2, y=TK_y//3)
        self.rafraich.place(x=0, y=0)
    def change_menu(self, new_menu):
        self.choice.destroy()
        self.choice = OptionMenu(self.ennemi_can, self.ennemi_choice, *new_menu)
        self.choice.place(x=TK_x//2, y=TK_y//4)