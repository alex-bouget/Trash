from ..System.VerticalSystem import VerticalSys
from ..System.CardSystem import CardSys


def Card(master, card_name, card_image, attack, defense, font_path, **kwargs):
    return CardSys(master, card_name, card_image, attack, defense, font_path, thread=False, compound='left', **kwargs)


class EveryCard(VerticalSys):
    def __init__(self, master, font_path, model, card, function):
        super().__init__(master)
        self.model = model
        self.CardSystem = card
        self.FontPath = font_path
        self.change_command(function)
        self.Set = False

    def change_command(self, function):
        for card in self.Card:
            card.configure(command=function)
        self.command = function

    def set_card(self):
        if len(self.Card) == 0:
            for ide, card in self.CardSystem.items():
                self.Card.append(Card(self.Frame, ide, self.model[ide], card.Att, card.Def, self.FontPath,
                                      command=lambda card_id=ide: self.command(card_id)))
                self.Card[-1].pack()
        self.Set = True
        self.resize()
