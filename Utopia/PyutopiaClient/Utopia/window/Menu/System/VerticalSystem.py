from tkinter import *


class VerticalSys(Canvas):
    def __init__(self, master, card=None):
        super().__init__(master)

        def ResizeFrame(self_frame):
            self_frame.master.configure(scrollregion=(0, 0, 0, self_frame.winfo_height()))

        if card is None:
            card = []
        self.configure(bg="red")
        self.Frame = Frame(self)
        setattr(self.Frame, "resize", lambda: ResizeFrame(self.Frame))
        self.create_window(0, 0, anchor="nw", window=self.Frame)
        self.bar = Scrollbar(self, command=self.yview, orient=VERTICAL)
        self.bar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.configure(yscrollcommand=self.bar.set)
        self.Card = card

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width() // 4)
        for card in self.Frame.winfo_children():
            card.resize()
