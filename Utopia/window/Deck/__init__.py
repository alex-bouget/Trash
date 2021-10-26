from .DeckCanvas import Deck
from .EveryCard import EveryCard
from .InfoCanvas import Info
from tkinter import *


class DeckCanvas(Canvas):
    def __init__(self, master, font_path, model, card, callback=None):
        super().__init__(master)
        if callback is None:
            callback = {}
        self.DeckCanvas = Deck(self, font_path, model, card)
        self.EveryCard = EveryCard(self, font_path, model, card, function=self.DeckCanvas.add_card)
        self.Info = Info(self, callback.get("save_quit", self.empty))
        self.EveryCard.place(x=0, y=0)
        self.resize()

    def add_deck(self, obj):
        for card in obj:
            self.DeckCanvas.add_card(card)

    def delete_deck(self):
        for card in self.DeckCanvas.deck:
            self.DeckCanvas.delete_card(card)

    @staticmethod
    def empty(self):
        pass

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.DeckCanvas.place(x=self.master.winfo_width(), y=self.master.winfo_height(), anchor=SE)
        self.Info.place(x=self.master.winfo_width()//2, y=self.master.winfo_height()//2, anchor=CENTER)
        self.DeckCanvas.resize()
        self.EveryCard.resize()
