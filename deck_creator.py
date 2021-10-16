from card import *

fr = Card()

def deckselect(evt):
    global photo, using_plan
    value=str(deck.me.get(deck.me.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout)]
    deckl.me.configure(text=cartestr[0]+lang[2]+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
    try:
        photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/'+fr.nb_by_name(value)+'.png'))
    except:
        for sei in os.listdir("mods"):
            if os.path.isfile("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"):
                photo = ImageTk.PhotoImage(Image.open("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"))
    Card_viever.me.configure(image=photo)
    using_plan = 1
def everyselect(evt):
    global photo, using_plan
    value=str(every_card.me.get(every_card.me.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout)]
    everyl.me.configure(text=cartestr[0]+lang[2]+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E")
    try:
        photo = ImageTk.PhotoImage(Image.open('card/png_'+lang[0]+'/'+fr.nb_by_name(value)+'.png'))
    except:
        for sei in os.listdir("mods"):
            if os.path.isfile("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"):
                photo = ImageTk.PhotoImage(Image.open("mods/"+sei+"/png/"+lang[0]+"_"+fr.nb_by_name(value)+".png"))
    Card_viever.me.configure(image=photo)
    using_plan = 2
def ajoute():
    if using_plan == 2:
        music.play_ambiant("click")
        deck.me.insert(END, fr.card_name)
def enleve():
    if using_plan == 1:
        music.play_ambiant("click")
        deck.me.delete(deck.me.get(0, END).index(fr.card_name))
def create_deck():
    music.play_ambiant("click")
    try:
        s = urlopen(server+"deck_creator2.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        if c == 1:
            s= open("other_code/deck_creator2.dat", "r")
            exec(s.read())
        else:
            s=decodefich("other_code/deck_creator2.dat")
            exec(s)
    for i in fr.card_all():
        every_card.me.insert(END, i)
    for i in card_mods:
        every_card.me.insert(END, fr.name_by_nb(i))
def set_deck(evt):
    music.play_ambiant("click")
    value=str(every_deck.me.get(every_deck.me.curselection()))
    with open("deck/"+value) as fichier:
        syst = fichier.read()
        syst = syst.split('\n')
    try:
        fr.name_by_nb(syst[1])
    except:
        if askyesno(lang[45], lang[46])==False:
            kernel.isAlive()
    for i in syst:
        try:
            deck.me.insert(END, fr.name_by_nb(i))
        except:
            deck.me.insert(END, i)
    x.me.destroy()
    aze = value.split('.')
    del aze[-1]
    aze = '.'.join(aze)
    deckname.set(aze)
    create_deck()
def change_deck():
    music.play_ambiant("click")
    try:
        s = urlopen(server+"deck_creator3.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        if c == 1:
            s= open("other_code/deck_creator3.dat", "r")
            exec(s.read())
        else:
            s=decodefich("other_code/deck_creator3.dat")
            exec(s)
    for item in os.listdir("deck"):
        every_deck.me.insert(END, item)
def create():
    systeme = []
    for i in deck.me.get(0, END):
        systeme.append(fr.nb_by_name(i))
    with open("deck/"+deckname.get()+".txt", "w") as fichier:
        fichier.write('\n'.join(systeme))
def finish():
    music.play_ambiant("click")
    if os.path.isfile("deck/"+deckname.get()+".txt"):
        if askokcancel(lang[39], deckname.get()+lang[40]+'\n'+lang[41]):
            music.play_ambiant("click")
            create()
        else:
            music.play_ambiant("click")
    else:
        create()
def open_creator():
    try:
        s = urlopen(server+"deck_creator1.txt")
        s = s.read()
        exec(s.decode(),globals())
    except:
        if c == 1:
            s= open("other_code/deck_creator1.dat", "r")
            exec(s.read())
        else:
            s=decodefich("other_code/deck_creator1.dat")
            exec(s)
try:
    s = urlopen(server+"deck_creator0.txt")
    s = s.read()
    exec(s.decode(),globals())
except:
    if c == 1:
        s= open("other_code/deck_creator0.dat", "r")
        exec(s.read())
    else:
        s=decodefich("other_code/deck_creator0.dat")
        exec(s)