from .BattleCanvas import Battle
from .DeckCanvas import Deck
from tkinter import *


class PrincipalMenu(Canvas):
    def __init__(self, master, player_id, lib, game_version, battle_server):
        super().__init__(master)
        self.BattleCanvas = Battle(master, player_id, lib, game_version)
        self.DeckCanvas = Deck(master, lib)
        self.battle_server = battle_server

        # Principal Menu Demo

        self.Can = Canvas(self)
        Button(self.Can, text="Play", command=self.start_battle).grid()
        Button(self.Can, text="Deck", command=self.DeckCanvas.start_deck).grid(row=1)

    def start_battle(self):
        self.BattleCanvas.starting(self.battle_server)

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.Can.place(x=self.winfo_width()//2, y=self.winfo_height()//2, anchor=CENTER)
