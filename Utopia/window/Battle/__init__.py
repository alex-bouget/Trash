from tkinter import *
from .Hand import HandCanvas
from .Board import BoardCanvas
from .Info import InfoCanvas


class GameCanvas(Canvas):
    def __init__(self, master, player_id, font_path, model, card, callback=None):
        super().__init__(master)
        if callback is None:
            callback = {}
        self.root = master
        self.PlayerId = player_id
        self.Callback = callback
        self.hand = HandCanvas(self, font_path, model, card, self.Callback.get("Hand", self.empty))
        self.Board = BoardCanvas(self, font_path, model, self.Callback.get("Board", self.empty))
        self.EnemyBoard = BoardCanvas(self, font_path, model, self.Callback.get("Enemy", self.empty))
        self.Info = InfoCanvas(self, self.Callback.get("Pass", self.empty))

    @staticmethod
    def empty(value):
        pass

    def change_battle(self, dico):
        print(dico)
        enemy = [i for i in dico.keys() if i != self.PlayerId][0]
        self.Info.change_life(dico[self.PlayerId]["Life"])
        self.Info.change_life(dico[enemy]["Life"], False)
        self.Info.change_eclat(dico[self.PlayerId]["Eclat"])
        self.Info.change_eclat(dico[enemy]["Eclat"], False)
        self.Info.change_Phase(dico["Phase"]["Phase"], self.PlayerId == dico["Phase"]["PlayerId"])
        self.Board.reload_Dico(dico[self.PlayerId]["Board"])
        self.EnemyBoard.reload_Dico(dico[enemy]["Board"])
        self.hand.reload_Dico(dico[self.PlayerId]["Hand"])

    def resize(self):
        self.configure(height=self.root.winfo_height(), width=self.root.winfo_width())
        self.hand.place(x=0, y=0)
        self.Board.place(x=self.winfo_width() // 4, y=0)
        self.EnemyBoard.place(x=self.winfo_width() // 4, y=self.winfo_height() // 3)
        self.Info.place(x=self.winfo_width() // 4, y=2 * (self.winfo_height() // 3))
        self.hand.resize()
        self.Board.resize()
        self.EnemyBoard.resize()
        self.Info.resize()
