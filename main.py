import game.start as start
import deck_creator as deck
from tkinter import *
sa = Canvas(deck.fenetre, width=200, height=100)
sa.pack()
def play():
    sa.destroy()
    start.open_game_system()
def crea():
    sa.destroy()
    deck.open_creator()
Button(sa, text="jouer", command=play).grid(row=0,column=0)
Button(sa, text="Decks", command=crea).grid(row=1)
sa.mainloop()