from tkinter import *
from .Hand import HandCanvas
from .Board import BoardCanvas
from .Info import InfoCanvas
from tkinter.messagebox import showinfo
from ....Lang import getlang


class GameCanvas(Canvas):
    def __init__(self, master, player_id, font_path, model, all_card, callback=None):
        super().__init__(master)
        if callback is None:
            callback = {}
        self.root = master
        self.PlayerId = player_id
        self.Callback = callback
        self.hand = HandCanvas(self, font_path, model, all_card, self.Callback.get("Hand", self.empty))
        self.Board = BoardCanvas(self, font_path, model, self.Callback.get("Board", self.empty))
        self.EnemyBoard = BoardCanvas(self, font_path, model, self.Callback.get("Enemy", self.empty))
        self.Info = InfoCanvas(self, self.Callback.get("Pass", self.empty))

    @staticmethod
    def empty(value):
        pass

    def change_battle(self, game_dict):
        enemy = [i for i in game_dict.keys() if i != self.PlayerId][0]
        self.Info.change_life(game_dict[self.PlayerId]["Life"])
        self.Info.change_life(game_dict[enemy]["Life"], False)
        self.Info.change_eclat(game_dict[self.PlayerId]["Eclat"])
        self.Info.change_eclat(game_dict[enemy]["Eclat"], False)
        self.Info.change_Phase(game_dict["Phase"]["Phase"], self.PlayerId == game_dict["Phase"]["PlayerId"])
        self.Board.reload_Dict(game_dict[self.PlayerId]["Board"])
        self.EnemyBoard.reload_Dict(game_dict[enemy]["Board"])
        self.hand.reload_Dict(game_dict[self.PlayerId]["Hand"])
        if game_dict[enemy]["Life"] <= 0 and game_dict[self.PlayerId]["Life"] <= 0:
            showinfo(getlang()["Battle"]["change_battle"][0])
            return "Finish"
        elif game_dict[self.PlayerId]["Life"] <= 0:
            showinfo(getlang()["Battle"]["change_battle"][2])
            return "Finish"
        elif game_dict[enemy]["Life"] <= 0:
            showinfo(getlang()["Battle"]["change_battle"][1])
            return "Finish"
        else:
            return "ui"

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
