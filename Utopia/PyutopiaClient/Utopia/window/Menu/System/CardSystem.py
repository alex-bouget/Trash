from tkinter import *
from PIL import ImageTk, ImageDraw, ImageFont
from copy import deepcopy
from threading import Thread


class CardSys(Button):
    def __init__(self, master, card_name, card_image, attack, defense, font_path, thread=False, **kwargs):
        super().__init__(master, **kwargs)
        self.CardName = card_name
        self.ThreadFinish = False
        self.CardImage = card_image
        self.FontPath = font_path
        self.attack = attack
        self.defence = defense
        if thread:
            Thread(target=self.thread).start()
        else:
            self.thread()

    def thread(self):
        self.CardDraw = deepcopy(self.CardImage)
        self.ImageTk = ImageTk.PhotoImage(self.CardImage)
        draw = ImageDraw.Draw(self.CardDraw)
        draw.text((246, 1529), str(self.attack), (0, 0, 0), anchor="mm", font=ImageFont.truetype(self.FontPath, 160))
        draw.text((952, 1529), str(self.defence), (0, 0, 0), anchor="mm", font=ImageFont.truetype(self.FontPath, 160))
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

    def resize(self, rel=False):
        self._resize(rel)
