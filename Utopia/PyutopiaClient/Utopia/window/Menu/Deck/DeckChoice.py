from ..System.DeckChoiceSystem import DeckChoiceSys
from tkinter import *
from ....Lang import getlang


class DeckChoice(DeckChoiceSys):
    class Deck(DeckChoiceSys.DeckSys):
        def __init__(self, master, color, name, callback=None):
            super().__init__(master, color, name, callback)
            self.Button.configure(text=getlang()["DeckChoiceSystem"]["init"][1])
            self.deleteButton = Button(self, text=getlang()["DeckChoice"]["init"][0],
                                       command=lambda deck_name=name: callback.get("delete", self.empty))

        def resize(self):
            self._resize()
            self.deleteButton.place(x=self.winfo_width() // 1.2, y=10)

    def __init__(self, master, color, all_deck, callback):
        super().__init__(master, color, all_deck, callback, DeckChoice.Deck)
        self.AddCard = Button(self, text=getlang()["DeckChoice"]["init"][1], command=callback.get("add", self.empty))
        self.resize()

    def resize(self):
        self._resize()
        self.AddCard.place(x=self.winfo_width()-20, y=5, anchor=NE)
