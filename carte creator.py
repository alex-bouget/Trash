from Card import *
fr = Card()

if os.path.isdir("Card_model") == False:
    os.mkdir("Card_model")

for i in card_nb:
    fr.card_model(i).save("Card_model/"+i+".png")
fenetre.destroy()