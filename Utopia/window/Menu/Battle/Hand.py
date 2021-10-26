from ..System.VerticalSystem import VerticalSys
from .Card import Card


class HandCanvas(VerticalSys):
    def __init__(self, master, font_path, model, card, function):
        super().__init__(master)
        self.model = model
        self.old_dict = []
        self.CardSystem = card
        self.Card = []
        self.FontPath = font_path
        self.change_command(function)

    def change_command(self, function):
        for card in self.Card:
            card.configure(command=function)
        self.command = function

    def add_card(self, ide, card_image, attack, defence):
        self.Card.append(Card(self.Frame, card_image, attack, defence, self.FontPath, False,
                              command=lambda card_id=ide: self.command(card_id)))
        self.Card[-1].pack()
        self.resize()

    def reload_Dict(self, game_dict):
        if game_dict != self.old_dict:
            self.old_dict = game_dict
            for card in self.Card:
                card.destroy()
            self.Card = []
            for card in game_dict:
                self.add_card(card, self.model[card], self.CardSystem.getAtt(card), self.CardSystem.getDef(card))
