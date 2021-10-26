from tkinter import *


class LoadingSys(Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.wr = StringVar()
        self.label = Label(self, textvariable=self.wr)
        self.StartFinish = False

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.label.place(anchor=CENTER, x=self.winfo_width() // 2, y=self.winfo_height() // 2)
