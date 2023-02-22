from .Menu.Deck import Deck
from .Menu.Deck.DeckChoice import DeckChoice
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import os
from ..Lang import getlang


class DeckSystem:
    def __init__(self, master, lib):
        self.DeckCanvas = Deck(master, os.path.join(lib.Card.BddFolder, "font.ttf"),
                               lib.Card.Model, lib.Card.Card.AllCard.CardData, {"save_quit": self.save_quit})
        self.DeckChoice = DeckChoice(master, "grey", lib.Deck.get_deck_name(), {"add": self.new_deck,
                                                                                "set": self.set_deck,
                                                                                "delete": lib.Deck.delete_deck})
        self.lib = lib
        self.name = ""

    def new_deck(self):
        name = askstring(getlang()["DeckSystem"]["new_deck"][0], getlang()["DeckSystem"]["new_deck"][1])
        self.lib.Deck.add_deck(name, [])
        self.set_deck(name)

    def set_deck(self, name):
        self.DeckCanvas.place(x=0, y=0)
        self.DeckChoice.place_forget()
        self.DeckCanvas.delete_deck()
        self.DeckCanvas.add_deck(self.lib.Deck.get_deck(name))
        self.name = name
        self.DeckCanvas.Info.DeckName.set(self.name)
        self.lib.Discord.change_activity(state="on deck creator")

    def save_quit(self):
        if len(self.DeckCanvas.DeckCanvas.deck) < 20:
            showinfo(getlang()["DeckSystem"]["save_quit"][0], getlang()["DeckSystem"]["save_quit"][1])
        else:
            self.lib.Deck.change_deck(name=self.name, obj=self.DeckCanvas.DeckCanvas.deck)
            self.DeckCanvas.place_forget()

    def start_deck(self):
        self.DeckChoice.all_deck = self.lib.Deck.get_deck_name()
        self.DeckChoice.ReloadFrame()
        self.DeckChoice.place(x=0, y=0)
        self.DeckChoice.resize()
