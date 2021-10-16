from card import *

fenetre.title("TESTEUR DE CARTE")
t = Canvas(fenetre, width=200, height=100)

fr = Card()
cartestr = [" "," "," "," "," "]
everyl = Label(t, text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E, N"+cartestr[4])

def everyselect(evt):
    global photo
    value=str(every_card.get(every_card.curselection()))
    fr.set_newcard_by_name(value)
    cartestr =[str(fr.card_name), str(fr.card_att), str(fr.card_def), str(fr.card_cout), str(fr.card_used)]
    everyl.configure(text=cartestr[0]+", att/def: "+cartestr[1]+"/"+cartestr[2]+", "+cartestr[3]+"E, N"+cartestr[4])
    photo = ImageTk.PhotoImage(Image.open('card/png_fr/'+fr.nb_by_name(value)+'.png'))
    Card_viever.configure(image=photo)
def decoder():
    if ifencode("card/nb.txt"):
        r = ["card/att.txt","card/def.txt","card/cout.txt","card/nb.txt","card/effect.txt","card/rarity.txt","other_code/deck_creator0.dat","other_code/deck_creator1.dat","other_code/deck_creator2.dat","other_code/deck_creator3.dat","other_code/start0.dat","other_code/start1.dat","other_code/start2.dat","other_code/start3.dat"]
        for i in r:
            att = decodefich(i)
            if att != False:
                att = att.split('/')
                att = '\n/'.join(att)
                f = open(i, "w")
                f.write(att)
                f.close()
        for i in os.listdir("langS"):
            att = decodefich("langS/"+i)
            if att != False:
                att = att.split('/')
                att = '\n/'.join(att)
                f = open("langS/"+i, "w")
                f.write(att)
                f.close()
        x.configure(text="fichier decoder")
def encoder():
    if ifencode("card/name.txt") == False:
        r = ["card/att.txt","card/def.txt","card/cout.txt","card/nb.txt","card/effect.txt","card/rarity.txt","other_code/deck_creator0.dat","other_code/deck_creator1.dat","other_code/deck_creator2.dat","other_code/deck_creator3.dat","other_code/start0.dat","other_code/start1.dat","other_code/start2.dat","other_code/start3.dat"]
        for i in r:
            att = encodefich(i)
            f = open(i, "w")
            f.write(att)
            f.close()
        for i in os.listdir("langS"):
            att = encodefich("langS/"+i)
            f = open("langS/"+i, "w")
            f.write(att)
            f.close()
        x.configure(text="fichier encoder")
def info():
    a = 0
    while a!=int(fr.card_tout+1):
        fr.set_newcard_by_nb(a)
        print("nom: "+fr.card_name)
        print("cout: "+fr.card_cout)
        print("att: "+fr.card_att)
        print("def: "+fr.card_def)
        print("nb: "+fr.card_used)
        print("_____________________")
        a = a+1
photo = ImageTk.PhotoImage(Image.open("card/png_fr/0.png"))

if ifencode("card/nb.txt"):
    x = Label(t, text="fichier encoder")
else:
    x = Label(t, text="fichier decoder")


Card_viever = Label(t, image=photo)
every_card=Listbox(t,width=20,height=20,font=('times',13))
every_card.bind('<<ListboxSelect>>', everyselect)
t.pack()
x.grid()
everyl.grid(row=0,column=1)
every_card.grid(row=1,column=0)
Card_viever.grid(row=1,column=1)
z = Button(t, text="encoder les fichiers", command=encoder)
y = Button(t, text="decoder les fichiers", command=decoder)
g = Button(t, text="sortir les info de cartes", command=info)
z.grid(row=2)
y.grid(row=2,column=1)
g.grid(row=3)

for i in range(len(card_debloque)-1):
        every_card.insert(END, fr.name_by_nb(i+1))
fenetre.mainloop()