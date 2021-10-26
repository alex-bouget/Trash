from tkinter import *


class LoadingSys(Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.label = self.create_text(0, 0, text="", anchor=CENTER)
        self.StartFinish = False

    def wr(self, text):
        self.itemconfig(self.label, text=text)

    def resize(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.move(self.label, (self.winfo_width() // 2)-self.coords(self.label)[0],
                  (self.winfo_height() // 2)-self.coords(self.label)[1])
