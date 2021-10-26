from tkinter import *
from PIL import ImageTk, ImageDraw, ImageFont
from copy import deepcopy


class CardSys(Button):
    def __init__(self, master, card_image, attack, defense, font_path, **kwargs):
        super().__init__(master, **kwargs)
        self.ThreadFinish = False
        self.CardImage = deepcopy(card_image)
        self.CardDraw = self.CardImage
        self.ImageTk = ImageTk.PhotoImage(self.CardImage)
        self.FontPath = font_path
        self.attack = attack
        self.defence = defense
        draw = ImageDraw.Draw(self.CardDraw)
        draw.text((246, 1529), str(self.attack), (0, 0, 0), anchor="mm", font=ImageFont.truetype(self.FontPath, 160))
        draw.text((952, 1529), str(defense), (0, 0, 0), anchor="mm", font=ImageFont.truetype(self.FontPath, 160))
        self.ThreadFinish = True
        self._resize(True)

    def _resize(self, rel=False):
        if self.winfo_exists():
            if self.ThreadFinish:
                if self.ImageTk.width() != self.master.master.winfo_width() - 10 or rel:
                    try:
                        self.ImageTk = ImageTk.PhotoImage(self.CardDraw.resize(
                            (int((self.master.master.winfo_width() - 10)//1.2),
                             int((self.master.master.winfo_width() - 10) * 0.96))))
                        self.configure(image=self.ImageTk, height=int(self.master.master.winfo_width() * 0.96),
                                       width=int(self.master.master.winfo_width()//1.2))
                    except ValueError:
                        self.ImageTk = ImageTk.PhotoImage(self.CardDraw.resize((1, 1)))
                        self.configure(image=self.ImageTk, height=1, width=1)
