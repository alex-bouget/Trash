from .ChoiceSystem import ChoiceMenu
from tkinter import *
from ....Lang import getlang


class DeckChoiceSys(ChoiceMenu):
    class DeckSys(ChoiceMenu.Choice):
        def __init__(self, master, color, name, callback=None):
            super().__init__(master, color)
            if callback is None:
                callback = {}
            self.deckLabel = Label(self, text=name, bg=color)
            self.Button = Button(self, text=getlang()["DeckChoiceSystem"]["init"][0],
                                 font=(None, 40), command=lambda deck_name=name:
                                 callback.get("set", self.empty)(deck_name))
            self.deckLabel.place(x=4, y=4)

        @staticmethod
        def empty(arg):
            pass

        def _resize(self):
            self.ChoiceReload()
            self.Button.place(x=self.winfo_width() // 2.6, y=self.winfo_height() // 6.7)

        def resize(self):
            self._resize()

    def __init__(self, master, color, all_deck, callback, system):
        super().__init__(master, color)
        self.return_menu = Button(self, text=getlang()["DeckChoice"]["init"][2], command=self.place_forget)
        self.color = color
        self.all_deck = all_deck
        self.callback = callback
        self.deckCanvas = []
        self.sys = system
        self.ReloadFrame()

    @staticmethod
    def empty(arg):
        pass

    def ReloadFrame(self):
        for choice in self.deckCanvas:
            choice.destroy()
        self.deckCanvas = []
        for deck in self.all_deck:
            self.deckCanvas.append(self.sys(self.Frame, self.color, deck, self.callback))
            self.deckCanvas[-1].pack()
        self._resize()

    def _resize(self):
        self.DataReload()
        self.return_menu.place(x=self.winfo_width() - 20, y=self.winfo_height() - 5, anchor=SE)
        for choice in self.deckCanvas:
            self.after_idle(choice.resize)

    def resize(self):
        self._resize()
