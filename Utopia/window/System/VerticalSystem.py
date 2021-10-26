from tkinter import *


class VerticalSys(Canvas):
    def __init__(self, master, card=None):
        super().__init__(master)
        if card is None:
            card = []
        self.configure(bg="red")
        self.Frame = Frame(self)
        self.create_window(0, 0, anchor="nw", window=self.Frame)
        self.bar = Scrollbar(self, command=self.yview, orient=VERTICAL)
        self.bar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.configure(yscrollcommand=self.bar.set)
        self.Card = card

    def resize(self):
        for card in self.Frame.winfo_children():
            card.resize()
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width() // 4)
        self.configure(scrollregion=(0, 0, 0, (self.winfo_height() // 1.22) * len(self.Card)))
