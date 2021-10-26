from .Deck import DeckCanvas
from .Deck.DeckChoice import DeckChoice
from tkinter.simpledialog import askstring
import os


class Deck:
    def __init__(self, master, lib):
        self.DeckCanvas = DeckCanvas(master, os.path.join(lib.BddFolder, lib.AuthServerName, "font.ttf"),
                                     lib.Model, lib.Card.Card.Card, {"save_quit": self.save_quit})
        self.DeckChoice = DeckChoice(master, "grey", lib.Deck.get_deck_name(), {"add": self.new_deck,
                                                                                "set": self.set_deck,
                                                                                "delete": lib.Deck.delete_deck})
        self.lib = lib
        self.name = ""

    def new_deck(self):
        name = askstring("new_deck", "name of your new deck:")
        self.lib.Deck.add_deck(name, [])
        self.set_deck(name)

    def set_deck(self, name):
        self.DeckCanvas.delete_deck()
        self.DeckCanvas.add_deck(self.lib.Deck.get_deck(name))
        self.name = name
        self.DeckCanvas.place(x=0, y=0)
        self.DeckChoice.place_forget()
        self.DeckCanvas.Info.DeckName.set(self.name)
        if not self.DeckCanvas.EveryCard.Set:
            self.DeckCanvas.EveryCard.set_card()

    def save_quit(self):
        self.lib.Deck.change_deck(name=self.name, obj=self.DeckCanvas.DeckCanvas.deck)
        self.DeckCanvas.place_forget()

    def start_deck(self):
        self.DeckChoice.place(x=0,y=0)
