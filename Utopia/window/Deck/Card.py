from ..System.CardSystem import CardSys


class Card(CardSys):
    def __init__(self, master, card_image, attack, defense, font_path, **kwargs):
        super().__init__(master, card_image=card_image, attack=attack, defense=defense,
                         font_path=font_path, compound='left', **kwargs)
        self.resize()

    def resize(self, rel=False):
        self._resize(rel)
