from ..System.VerticalSystem import VerticalSys
from .Card import Card


class Deck(VerticalSys):
    def __init__(self, master, font_path, model, card):
        super().__init__(master, {})
        self.model = model
        self.CardSystem = card
        self.Card = {}
        self.deck = []
        self.FontPath = font_path

    def add_card(self, ide):
        if ide in self.deck:
            self.Card[ide].configure(text=str(self.deck.count(ide)+1))
        else:
            self.Card[ide] = Card(self.Frame, self.model[ide], self.CardSystem[ide].Att, self.CardSystem[ide].Def,
                                  self.FontPath, command=lambda card_id=ide: self.delete_card(ide), text=str(1))
            self.Card[ide].pack()
            self.resize()
        self.deck.append(ide)

    def delete_card(self, ide):
        if self.deck.count(ide) == 1:
            self.Card[ide].destroy()
            del self.Card[ide]
            self.resize()
        else:
            self.Card[ide].configure(text=str(self.deck.count(ide)-1))
        del self.deck[self.deck.index(ide)]
