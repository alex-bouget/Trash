from tkinter import *
from ....Lang import getlang


class Eclat(Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.Eclat = IntVar()
        Label(self, text=getlang()["Info"]["init"][0]).grid()
        Label(self, textvariable=self.Eclat).grid(column=1, row=0)

    def resize(self):
        pass


class Life(Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.Life = IntVar()
        Label(self, text=getlang()["Info"]["init"][1]).grid()
        Label(self, textvariable=self.Life).grid(column=1, row=0)

    def resize(self):
        pass


class Phase(Canvas):
    def __init__(self, master):
        super().__init__(master)
        self.Phase = StringVar()
        self.Your_or_not = StringVar()
        Label(self, text=getlang()["Info"]["init"][2]).grid()
        Label(self, textvariable=self.Your_or_not).grid(column=1, row=0)
        Label(self, textvariable=self.Phase).grid(column=2, row=0)

    def resize(self):
        pass


class InfoCanvas(Canvas):
    def __init__(self, master, pass_command):
        super().__init__(master, bg="grey")
        self.Info_grid = Canvas(self)
        self.User = {"Eclat": Eclat(self.Info_grid), "Life": Life(self.Info_grid)}
        self.Enemy = {"Eclat": Eclat(self.Info_grid), "Life": Life(self.Info_grid)}
        self.Phase = Phase(self.Info_grid)
        Label(self.Info_grid, text=getlang()["Info"]["init"][3]).grid(column=0, row=0)
        Label(self.Info_grid, text=getlang()["Info"]["init"][4]).grid(row=1, column=0)
        self.User["Life"].grid(column=1, row=0)
        self.User["Eclat"].grid(column=2, row=0)
        self.Enemy["Life"].grid(column=1, row=1)
        self.Enemy["Eclat"].grid(column=2, row=1)
        Button(self.Info_grid, text=getlang()["Info"]["init"][7], command=pass_command).grid(row=0, column=3, rowspan=2)
        self.Phase.grid(row=2, column=0)

    def change_eclat(self, value, user=True):
        if user:
            self.User["Eclat"].Eclat.set(value)
        else:
            self.Enemy["Eclat"].Eclat.set(value)

    def change_life(self, value, user=True):
        if user:
            self.User["Life"].Life.set(value)
        else:
            self.Enemy["Life"].Life.set(value)

    def change_Phase(self, value, user=True):
        if user:
            self.Phase.Your_or_not.set(getlang()["Info"]["init"][5])
        else:
            self.Phase.Your_or_not.set(getlang()["Info"]["init"][6])
        self.Phase.Phase.set(value)

    def resize(self):
        self.configure(height=self.master.winfo_height() // 3,
                       width=self.master.winfo_width() - (self.master.winfo_width() // 4))
        self.Info_grid.place(anchor=CENTER, x=self.winfo_width() // 2, y=self.winfo_height() // 2)
