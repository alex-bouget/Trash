from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import os
import sys
import shutil
import codec
from PIL import ImageTk, Image

order = []
rarity = ['0', "C", "O", "R", "M", "L", "TC", "TO"]
with open("all_lang.txt") as f:
    all_lang = f.read().split("\n")
if os.path.isdir("BDD")==False:
    os.mkdir("BDD")
TK_x = 720
TK_y = int(TK_x*(2/3))

def compile_data():
    if os.path.isdir("Output")==False:
        os.mkdir("Output")
    if os.path.isdir("Output/"+BDD_using.get()):
        shutil.rmtree("Output/"+BDD_using.get(), ignore_errors=True)
    shutil.copytree("for compile", "Output/"+BDD_using.get())
    nb = []
    att = []
    defs = []
    cout = []
    effet = []
    rarete = []
    name = []
    desc = []
    tag = []
    for i in all_lang:
        name.append([])
        desc.append([])
        try:
            os.mkdir("Output/"+BDD_using.get()+'/lang/'+i)
        except:
            pass

    for i in open("BDD/"+BDD_using.get()+"/order.txt").read().split("\n"):
        if os.path.isfile("BDD/"+BDD_using.get()+'/tete/'+i+".png")==False:
            if messagebox.askyesno("No Head", "no head for card "+i+"\nContinue ?"):
                pass
            else:
                break
        else:
            shutil.copy("BDD/"+BDD_using.get()+"/tete/"+i+".png", "Output/"+BDD_using.get()+'/card/tete/'+i+".png")
        nb.append(i)
        with open("BDD/"+BDD_using.get()+'/card/'+i+"/data.txt") as f:
            temp = f.read().split('\n')
        att.append(temp[0])
        defs.append(temp[1])
        cout.append(temp[2])
        effet.append(temp[3])
        rarete.append(temp[4])
        tag.append(temp[5])
        for x in all_lang:
            with open("BDD/"+BDD_using.get()+'/card/'+i+"/"+x+".txt") as r:
                temp = r.read().split("\n")
                print(temp)
                name[all_lang.index(x)].append(temp[0])
                desc[all_lang.index(x)].append(temp[1])
    print(len(rarete))
    with open("Output/"+BDD_using.get()+'/card/nb.txt', "w") as f:
        f.write(codec.encode("/".join(nb)))
    with open("Output/"+BDD_using.get()+'/card/att.txt', "w") as f:
        f.write(codec.encode("/".join(att)))
    with open("Output/"+BDD_using.get()+'/card/def.txt', "w") as f:
        f.write(codec.encode("/".join(defs)))
    with open("Output/"+BDD_using.get()+'/card/cout.txt', "w") as f:
        f.write(codec.encode("/".join(cout)))
    with open("Output/"+BDD_using.get()+'/card/rarity.txt', "w") as f:
        f.write(codec.encode("/".join(rarete)))
    with open("Output/"+BDD_using.get()+'/card/effect.txt', "w") as f:
        f.write(codec.encode("/".join(effet)))
    with open("Output/"+BDD_using.get()+'/card/tag_card.txt', "w") as f:
        f.write("\n".join(tag))
    for i in all_lang:
        print(name[all_lang.index(i)])
        with open("Output/"+BDD_using.get()+"/lang/"+i+"/name.txt", "w") as f:
            f.write(codec.encode("/".join(name[all_lang.index(i)])))
        with open("Output/"+BDD_using.get()+"/lang/"+i+"/desc.txt", "w") as f:
            f.write(codec.encode("/".join(desc[all_lang.index(i)])))
    with open("Output/"+BDD_using.get()+"/down.txt", "w") as f:
        f.write("card:/:card/card:/:card/tete:/:lang")
        for i in all_lang:
            f.write(":/:lang/"+i)
        for i in tree("Output/"+BDD_using.get()):
            if i=="down.txt":
                pass
            else:
                f.write("\n"+i+"-->"+i)
def tree(rst):
    ret = []
    for i in os.listdir(rst):
        if os.path.isdir(rst+"/"+i):
            for s in tree(rst+"/"+i):
                ret.append(i+"/"+s)
        else:
            ret.append(i)
    return(ret)



def save(number):
    with open("BDD/"+BDD_using.get()+"/card/"+number+"/data.txt", "w") as f:
        f.write(card_data.att.get()+"\n"+card_data.defs.get()+"\n"+card_data.cout.get()+"\n"+card_data.effect.get()+"\n"+card_data.rarete.get()+"\n"+card_data.tag_card.get())
def retourlang():
    global lang_data
    lang_data.c.destroy()
    lang_data = lang_var()
    card_data.place()
    temp = lambda: save(str(card_data.nb.get()))
    card_data.b.configure(command=temp)
    temp = lambda: new_image(card_data.nb.get())
    card_data.b2.configure(command=temp)
    card_data.b3.configure(command=lang)
    card_data.b4.configure(command=retour)
def savelang():
    with open("BDD/"+BDD_using.get()+"/card/"+card_data.nb.get()+"/"+lang_data.lang.get()+".txt", "w") as f:
        f.write(lang_data.name.get()+"\n"+lang_data.desc.get())
def lang():
    global card_data
    card_data.card.destroy()
    temp = card_data.nb.get()
    card_data = card_var()
    card_data.new_var(temp)
    lang_data.place()
    lang_data.b.configure(command=savelang)
    lang_data.b3.configure(command=retourlang)
def new_image(nb):
    image = filedialog.askopenfilename(filetypes=[("png image 291*219","*.png")])
    shutil.copy(image, "BDD/"+BDD_using.get()+"/tete/"+nb+".png")
def retour():
    global card_data
    card_data.card.destroy()
    card_data = card_var()
def open_card_list(evt):
    card(Bdd.Card.get(Bdd.Card.curselection()))
def card(number):
    card_data.place()
    temp = lambda: save(str(number))
    card_data.new_var(number)
    card_data.b.configure(command=temp)
    temp = lambda: new_image(card_data.nb.get())
    card_data.b2.configure(command=temp)
    card_data.b3.configure(command=lang)
    card_data.b4.configure(command=retour)
def create_card():
    temp = simpledialog.askstring("data name", "what is the data name of card ?")
    if temp != None:
        os.mkdir("BDD/"+BDD_using.get()+"/card/"+temp)
        with open("BDD/"+BDD_using.get()+"/card/"+temp+"/data.txt", "w") as f:
            f.write("0\n0\n0\n\nTC\n")
        for i in all_lang:
            with open("BDD/"+BDD_using.get()+"/card/"+temp+"/"+i+".txt", "w") as f:
                f.write(i+" name\n"+i+" description")
        order.append(temp)
        recreate_order()
        reload_card()
def new_BDD():
    name = simpledialog.askstring("name of new bdd", "what is the of your new BDD ?")
    if name != None:
        os.mkdir("BDD/"+name)
        os.mkdir("BDD/"+name+"/card")
        os.mkdir("BDD/"+name+"/tete")
        open("BDD/"+name+"/order.txt", "w").close()
        open_bdd(name)
def select_lector(evt):
    open_bdd(r.var_deck_lector_listbox.get(r.var_deck_lector_listbox.curselection()))
def recreate_order():
    with open("BDD/"+BDD_using.get()+"/order.txt", "w") as f:
        f.write("\n".join(order)+"\n")
def open_bdd(name):
    BDD_using.set(name)
    with open("BDD/"+BDD_using.get()+"/order.txt") as f:
        for i in f.read().split("\n"):
            order.append(i)
        del order[-1]
    r.var_deck_lector.destroy()
    Bdd.place()
    reload_card()
    Bdd.Card.bind('<<ListboxSelect>>', open_card_list)
    Bdd.create.configure(command=create_card)
    Bdd.compile.configure(command=compile_data)
def reload_card():
    Bdd.Card.delete(0, END)
    for i in open("BDD/"+BDD_using.get()+"/order.txt").read().split("\n"):
        Bdd.Card.insert(END, i)
class BDD:
    def __init__(self):
        self.BDD = Canvas(fenetre, height=TK_y, width=TK_x)
        self.Card = Listbox(self.BDD, height=TK_x//30, width=TK_y)
        self.create = Button(self.BDD, text="create new card")
        self.compile = Button(self.BDD, text="Compile")
    def place(self):
        self.BDD.place(x=0, y=0)
        self.create.place(x=0, y=TK_y-30)
        self.Card.place(x=0,y=0)
        self.compile.place(x=100, y=TK_y-30)
class var_deck_lector:
    def __init__(self):
        self.var_deck_lector = Canvas(fenetre, height=TK_y, width=TK_x)
        self.var_deck_lector_listbox = Listbox(self.var_deck_lector, height=TK_x//30, width=TK_y)
        self.var_deck_lector_button = Button(self.var_deck_lector, text="create new BDD")
    def place_lector(self):
        self.var_deck_lector.place(x=0, y=0)
        self.var_deck_lector_button.place(x=0, y=TK_y-30)
        self.var_deck_lector_listbox.place(x=0,y=0)
class card_var:
    def __init__(self):
        self.defs = StringVar()
        self.att = StringVar()
        self.effect = StringVar()
        self.nb = StringVar()
        self.cout = StringVar()
        self.rarete = StringVar()
        self.tag_card = StringVar()

        self.card = Canvas(fenetre, height=TK_y, width=TK_x)
        self.def_label = Label(self.card,text="def: ")
        self.def_entry = Entry(self.card, textvariable=self.defs)
        self.att_label = Label(self.card, text="att: ")
        self.att_entry = Entry(self.card, textvariable=self.att)
        self.effect_label = Label(self.card, text="effect: ")
        self.effect_entry = Entry(self.card, textvariable=self.effect)
        self.n_label = Label(self.card, text="nb: ")
        self.n_entry = Label(self.card, textvariable=self.nb)
        self.cout_label = Label(self.card, text="cout: ")
        self.cout_entry = Entry(self.card, textvariable=self.cout)
        self.rarete_label = Label(self.card, text="rarity: ")
        self.rarete_entry = OptionMenu(self.card, self.rarete, *rarity)
        self.tag_card_label = Label(self.card, text="tag_card: ")
        self.tag_card_entry = Entry(self.card, textvariable=self.tag_card)
        self.b = Button(self.card, text="save card")
        self.b2 = Button(self.card, text="image")
        self.b3 = Button(self.card, text="language")
        self.b4 = Button(self.card, text="return")
        self.photo = Label(self.card)
        self.photol = ""
    def place(self):
        self.card.place(x=5, y=5)
        self.n_label.place(x=5, y=5)
        self.att_label.place(x=5, y=40)
        self.def_label.place(x=5, y=80)
        self.cout_label.place(x=5, y=120)
        self.rarete_label.place(x=5, y=160)
        self.effect_label.place(x=5, y=200)
        self.tag_card_label.place(x=5, y=240)
        self.b.place(x=5, y=280)
        self.b2.place(x=100, y=280)
        self.b3.place(x=200, y=280)
        self.b4.place(x=300, y=280)
        self.n_entry.place(x=100, y=0)
        self.att_entry.place(x=100, y=40)
        self.def_entry.place(x=100, y=80)
        self.cout_entry.place(x=100, y=120)
        self.rarete_entry.place(x=100, y=160)
        self.effect_entry.place(x=100, y=200)
        self.tag_card_entry.place(x=100, y=240)
        self.photo.place(x=400, y=10)
    def new_var(self, nb):
        with open("BDD/"+BDD_using.get()+"/card/"+nb+"/data.txt", "r") as f:
            temp = f.read().split('\n')
        try:
            self.photol = ImageTk.PhotoImage(Image.open("BDD/"+BDD_using.get()+"/tete/"+nb+".png"))
        except:
            self.photol = ImageTk.PhotoImage(Image.open("no photo.png"))
        self.photo.configure(image=self.photol)
        self.nb.set(nb)
        self.att.set(temp[0])
        self.defs.set(temp[1])
        self.cout.set(temp[2])
        self.effect.set(temp[3])
        self.rarete.set(temp[4])
        self.tag_card.set(temp[5])
class lang_var:
    def __init__(self):
        self.lang = StringVar()
        self.desc = StringVar()
        self.name = StringVar()
        self.c = Canvas(fenetre, height=TK_y, width=TK_x)
        self.s = OptionMenu(self.c, self.lang, *all_lang, command=self.choice)
        self.desc_label = Label(self.c, text="description")
        self.desc_entry = Entry(self.c, textvariable=self.desc)
        self.name_label = Label(self.c, text="name")
        self.name_entry = Entry(self.c, textvariable=self.name)
        self.b = Button(self.c, text="save card")
        self.b3 = Button(self.c, text="return")
    def place(self):
        self.c.place(x=0, y=0)
        self.s.place(x=0, y=0)
        self.desc_label.place(x=0, y=80)
        self.name_label.place(x=0, y=40)
        self.b.place(x=0, y=120)
        self.desc_entry.place(x=100, y=80)
        self.name_entry.place(x=100, y=40)
        self.b3.place(x=100, y=120)
    def choice(self, evt):
        with open("BDD/"+BDD_using.get()+"/card/"+card_data.nb.get()+"/"+self.lang.get()+".txt", "r") as f:
            temp = f.read().split('\n')
        self.desc.set(temp[1])
        self.name.set(temp[0])


fenetre = Tk()
fenetre.title("Utopia BDD")
fenetre.geometry(str(TK_x)+"x"+str(TK_y))
Bdd = BDD()
card_data = card_var()
lang_data = lang_var()
r = var_deck_lector()
r.place_lector()
for i in os.listdir("BDD"):
    r.var_deck_lector_listbox.insert(END, i)
r.var_deck_lector_button.configure(command=new_BDD)
r.var_deck_lector_listbox.bind('<<ListboxSelect>>', select_lector)
BDD_using = StringVar()
def start():
    fenetre.mainloop()