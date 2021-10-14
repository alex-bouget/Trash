import card as card
main = card.Card()
a = 0
while a!=int(main.card_tout):
    main.set_newcard_by_nb(a)
    print("nom: "+main.card_name)
    print("cout: "+main.card_cout)
    print("att: "+main.card_att)
    print("def: "+main.card_def)
    print("nb: "+main.card_used)
    print("_____________________")
    a = a+1