from tkinter import *
from ...Lang import getlang
from PIL import Image, ImageTk


class PrincipalMenu(Canvas):
    def __init__(self, master, callback=None):
        super().__init__(master)
        if callback is None:
            callback = {}
        # Principal Menu Demo
        self.lab = self.create_image(0, 0, anchor="nw")
        self.Can = Canvas(self)
        self.image = Image.open("Ressources/menu_back.jpg")
        self.img = ImageTk.PhotoImage(self.image)
        Button(self.Can, text=getlang()["PrincipalMenu"]["init"][0], command=callback.get("Play", self.empty)).grid()
        Button(self.Can, text=getlang()["PrincipalMenu"]["init"][1],
               command=callback.get("Deck", self.empty)).grid(row=1)

    @staticmethod
    def empty():
        pass

    def resize(self):
        try:
            self.img = ImageTk.PhotoImage(self.image.resize((self.winfo_width(), self.winfo_height())))
            self.itemconfig(self.lab, image=self.img)
        except:
            pass
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.Can.place(x=self.winfo_width()//2, y=self.winfo_height()//2, anchor=CENTER)
