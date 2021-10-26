from tkinter import *
from .Card import Card


class BoardCanvas(Canvas):
    def __init__(self, master, font_path, model, function):
        super().__init__(master)
        self.root = master
        self.configure(bg="blue")
        self.Frame = Frame(self)
        self.model = model
        self.create_window(0, 0, anchor="nw", window=self.Frame)
        self.FontPath = font_path
        self.Card = {}
        self.command = self.empty
        self.bar = Scrollbar(self, command=self.xview, orient=HORIZONTAL)
        self.bar.place(relx=0, rely=1, relwidth=1, anchor='sw')
        self.configure(xscrollcommand=self.bar.set)
        self.change_command(function)

    def empty(self, game_dict):
        pass

    def add_card(self, ide, card_image, attack, defence):
        self.Card[ide] = Card(self.Frame, ide, card_image, attack, defence, self.FontPath,
                              command=lambda card_id=ide: self.command(card_id))
        self.Card[ide].pack(side=LEFT)
        self.resize()

    def change_command(self, function):
        for canvas in self.Card.values():
            canvas.configure(command=function)
        self.command = function

    def reload_Dict(self, game_dict):
        for key in range(len(game_dict)):
            if key > len(self.Card) - 1:
                self.add_card(key, self.model[game_dict[key]["Id"]], game_dict[key]["att"], game_dict[key]["def"])
            if game_dict[key]["state"] == "Dead":
                self.Card[key].destroy()
            if game_dict[key]["att"] != self.Card[key].attack or game_dict[key]["def"] != self.Card[key].defence:
                self.Card[key].change(game_dict[key]["att"], game_dict[key]["def"])
        self.resize()

    def resize(self):
        for card in self.Frame.winfo_children():
            card.resize()
        self.configure(height=self.root.winfo_height() // 3,
                       width=self.root.winfo_width() - (self.root.winfo_width() // 4))
        self.configure(scrollregion=(0, 0, (self.winfo_width() // 1.21) * len(self.Card), 0))
