from tkinter import *


class ChoiceMenu(Canvas):
    class Choice(Canvas):
        def __init__(self, master, color):
            super().__init__(master, bg=color)

        def ChoiceReload(self):
            self.configure(height=self.master.master.winfo_height()//1.9, width=self.master.master.winfo_width()//1.1)

    def __init__(self, master, color):
        super().__init__(master, bg=color)
        self.TagCanvas = Canvas(self, bg=color)
        self.Frame = Frame(self.TagCanvas, bg=color)
        self.TagCanvas.create_window(0, 0, anchor='nw', window=self.Frame)
        self.bar = Scrollbar(self, command=self.TagCanvas.yview, orient="vertical")
        self.bar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.TagCanvas.configure(yscrollcommand=self.bar.set)
        self.bind("<MouseWheel>", self.Mouse)

    def Mouse(self, event):
        if self.winfo_ismapped():
            self.TagCanvas.yview("scroll", int(-1*(event.delta/120)), "units")

    def DataReload(self):
        self.configure(height=self.master.winfo_height(), width=self.master.winfo_width())
        self.TagCanvas.configure(height=self.winfo_height()//1.13, width=self.winfo_width()//1.36,
                                 scrollregion=(0, 0, 0, self.Frame.winfo_height()))
        self.TagCanvas.place(x=4, y=self.winfo_height()//7.6)
