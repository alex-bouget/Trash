from tkinter import *


class PrincipalMenu(Canvas):
    def __init__(self, master, callback=None):
        super().__init__(master)
        if callback is None:
            callback = {}
        # Principal Menu Demo
        self.Can = Canvas(self)
        Button(self.Can, text="Play", command=callback.get("Play", self.empty)).grid()
        Button(self.Can, text="Deck", command=callback.get("Deck", self.empty)).grid(row=1)

    @staticmethod
    def empty():
        print("empty")
        pass

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.Can.place(x=self.winfo_width()//2, y=self.winfo_height()//2, anchor=CENTER)
