from Card import *

fenetre.title("TESTEUR DE CARTE")
fenetre.geometry("%dx%d+0+0" % (600, 600))

defs = StringVar()
att = StringVar()
effect = StringVar()
nb = StringVar()
cout = StringVar()
rarete = StringVar()
name = StringVar()
nam = []
description = StringVar()
descriptio = []
rarity = ['0', "C", "O", "R", "M", "L", "TC", "TO"]
for i in os.listdir("lang"):
    na = codec.decode_fich("lang/"+i+"/name.txt").split("/")
    nam.append(na)
for i in os.listdir("lang"):
    descriptio.append(codec.decode_fich("lang/"+i+"/desc.txt").split("/"))


fr = Card()
def info():
    for i in card_name:
        fr.set_newcard_by_name(i)
        print("nb: "+fr.card_used)
        print("att: "+fr.card_att)
        print("def: "+fr.card_def)
        print("cout: "+fr.card_cout)
        for s in os.listdir("lang"):
            print(s+" var:")
            print("name: "+codec.decode_fich("lang/"+s+"/name.txt").split("/")[int(fr.nb_by_name(i))])
            print("desciption: "+codec.decode_fich("lang/"+s+"/desc.txt").split("/")[int(fr.nb_by_name(i))])

def bdd_one():
    global t, r
    t = Canvas(fenetre, width=600, height=600)
    r = Listbox(t, width=20,height=29,font=('times',13))
    d = Label(t,text="def: ")
    dv = Entry(t, textvariable=defs)
    a = Label(t, text="att: ")
    av = Entry(t, textvariable=att)
    e = Label(t, text="effect: ")
    ev = Entry(t, textvariable=effect)
    n = Label(t, text="nb: ")
    nv = Label(t, textvariable=nb)
    c = Label(t, text="cout: ")
    cv = Entry(t, textvariable=cout)
    rar = Label(t, text="rarity: ")
    rarv = OptionMenu(t, rarete, *rarity)
    b = Button(t, text="save card", command=save)
    b2 = Button(t, text="new card", command=new)
    b3 = Button(t, text="name", command=name_c)
    b4 = Button(t, text="descrip", command=desc_c)
    b5 = Button(t, text="info", command=info)

    t.pack()
    r.place(x=0, y=0)
    d.place(x=200, y=5)
    a.place(x=200, y=35)
    e.place(x=200, y=65)
    n.place(x=200, y=95)
    c.place(x=200, y=125)
    rar.place(x=200, y=155)
    dv.place(x=250, y=5)
    av.place(x=250, y=35)
    ev.place(x=250, y=65)
    nv.place(x=250, y=95)
    cv.place(x=250, y=125)
    rarv.place(x=250, y=155)

    b.place(x=200, y=185)
    b2.place(x=300, y=185)
    b3.place(x=200, y=215)
    b4.place(x=300, y=215)
    b5.place(x=400, y=185)

    r.bind('<<ListboxSelect>>', L_select)
    L_reload()
def L_select(evt):
    value=str(r.get(r.curselection()))
    fr.set_newcard_by_nb(value)
    defs.set(fr.card_def)
    att.set(fr.card_att)
    effect.set(fr.card_effect)
    nb.set(fr.card_used)
    cout.set(fr.card_cout)
    rarete.set(fr.card_rarity)
def L_reload():
    r.delete(0, END)
    for i in card_nb:
        r.insert(END, str(i))
def save():
    card_att[int(nb.get())] = att.get()
    card_def[int(nb.get())] = defs.get()
    card_effect[int(nb.get())] = effect.get()
    card_cout[int(nb.get())] = cout.get()
    card_rarity[int(nb.get())] = rarete.get()
    recreate_data()
    L_reload()
def recreate_data():
    liste = ["card/nb.txt", "card/att.txt", "card/def.txt", "card/effect.txt", "card/cout.txt", "card/rarity.txt"]
    lte = [card_nb, card_att, card_def, card_effect, card_cout, card_rarity]
    for i in liste:
        z = codec.encode("/".join(lte[liste.index(i)]))
        with open(i, "w") as f:
            f.write(z)
    for i in os.listdir("lang"):
        with open("lang/"+i+"/name.txt", "w") as f:
            f.write(codec.encode("/".join(nam[os.listdir("lang").index(i)])))
        with open("lang/"+i+"/desc.txt", "w") as f:
            f.write(codec.encode("/".join(descriptio[os.listdir("lang").index(i)])))
def new():
    card_nb.append(str(len(card_nb)))
    card_att.append('0')
    card_def.append('0')
    card_cout.append('0')
    card_rarity.append('TC')
    card_effect.append('')
    card_name.append("")
    for i in os.listdir("lang"):
        nam[os.listdir("lang").index(i)].append("")
        descriptio[os.listdir("lang").index(i)].append("")
    recreate_data()
    L_reload()
def name_c():
    global az, am
    t.destroy()
    az = Canvas(fenetre, width=600, height=600)
    am = Listbox(az, width=20,height=20,font=('times',13))
    for i in nam:
        am.insert(END, str(i[int(nb.get())]))
    sauve = Button(az, text="save", command=name_s)
    n = Entry(az, textvariable=name)
    tra = Button(az, text="return", command=ret)


    am.bind('<<ListboxSelect>>', n_select)

    az.pack()
    am.place(x=0, y=0)
    n.place(x=200,y=5)
    sauve.place(x=190, y=35)
    tra.place(x=250, y=35)
def name_s():
    nam[int(am.curselection()[0])][int(nb.get())] =name.get()
    recreate_data()
def n_select(evt):
    value=str(am.get(am.curselection()))
    name.set(value)
def ret():
    az.destroy()
    bdd_one()


def desc_c():
    global az, am
    t.destroy()
    az = Canvas(fenetre, width=600, height=600)
    am = Listbox(az, width=20,height=20,font=('times',13))
    for i in descriptio:
        am.insert(END, str(i[int(nb.get())]))
    sauve = Button(az, text="save", command=desc_s)
    n = Entry(az, textvariable=description)
    tra = Button(az, text="return", command=ret)


    am.bind('<<ListboxSelect>>', d_select)

    az.pack()
    am.place(x=0, y=0)
    n.place(x=200,y=5)
    sauve.place(x=190, y=35)
    tra.place(x=250, y=35)
def desc_s():
    descriptio[int(am.curselection()[0])][int(nb.get())] =description.get()
    recreate_data()
def d_select(evt):
    value=str(am.get(am.curselection()))
    description.set(value)
bdd_one()

fenetre.mainloop()