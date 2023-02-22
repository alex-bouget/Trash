from ..System.CardSystem import CardSys, deepcopy
from PIL import ImageTk, ImageDraw, ImageFont


class Card(CardSys):
    def __init__(self, master, card_name, card_image, attack, defense, font_path, height=True, **kwargs):
        super().__init__(master, card_name=card_name, card_image=card_image, attack=attack,
                         defense=defense, font_path=font_path, **kwargs)
        self.height = height
        self.resize()

    def change(self, att, defense, lock=True):
        self.attack = att
        self.defence = defense
        self.CardDraw = deepcopy(self.CardImage)
        draw = ImageDraw.Draw(self.CardDraw)
        draw.text((246, 1529), str(att), (0, 0, 0), anchor="mm", font=ImageFont.truetype(self.FontPath, 160))
        draw.text((952, 1529), str(defense), (0, 0, 0), anchor="mm", font=ImageFont.truetype(self.FontPath, 160))
        if lock:
            self.resize(True)

    def resize(self, rel=False):
        if self.height:
            if self.winfo_exists():
                if self.ThreadFinish:
                    if self.ImageTk.height() != self.master.master.winfo_height() - 10 or rel:
                        try:
                            self.ImageTk = ImageTk.PhotoImage(self.CardDraw.resize(
                                (int((self.master.master.winfo_height() - 10) // 1.175),
                                 int((self.master.master.winfo_height() - 10) // 1.2))))
                            self.configure(image=self.ImageTk, height=int(self.master.master.winfo_height() // 1.2),
                                           width=int(self.master.master.winfo_height() // 1.175))
                        except ValueError:
                            self.ImageTk = ImageTk.PhotoImage(self.CardDraw.resize((1, 1)))
                            self.configure(image=self.ImageTk, height=1, width=1)
        else:
            self._resize(rel)
