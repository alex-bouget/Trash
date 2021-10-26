from ..System.DeckChoiceSystem import DeckChoiceSys
from tkinter import *


class DeckChoice(DeckChoiceSys):
    class Deck(DeckChoiceSys.DeckSys):
        def __init__(self, master, color, name, callback=None):
            super().__init__(master, color, name, callback)
            self.deleteButton = Button(self, text="delete", command=lambda deck_name=name: callback.get("delete",
                                                                                                        self.empty))

        def resize(self):
            self._resize()
            self.deleteButton.place(x=self.winfo_width() // 1.2, y=10)

    def __init__(self, master, color, all_deck, callback):
        super().__init__(master, color, all_deck, callback)
        self.AddCard = Button(self, text="create Deck", command=callback.get("add", self.empty))
        self.resize()

    def resize(self):
        self._resize()
        self.AddCard.place(x=self.winfo_width(), y=0, anchor=NE)
