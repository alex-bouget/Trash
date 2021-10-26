from .lib import UtopiaLib
from .window.Loading.StartCanvas import StartCanvas
from .window.Principal_Menu import PrincipalMenu
from tkinter import *


class Utopia(Tk):
    def __init__(self, ide, battle_server, version):
        super().__init__()
        self.id = ide
        self.configure(width=720, height=480)
        self.Lib = UtopiaLib(battle_server, "Data/", "fr")
        self.start = StartCanvas(self, self.Lib)
        self.start.place(x=0, y=0)
        self.battle_server = battle_server+"Battle/B1/"
        self.Menu = PrincipalMenu(self, ide, self.Lib, version, self.battle_server)
        self.bind("<Configure>", self.resize)
        self.after(500, self.test)
        self.resize(forced=True)

    def test(self):
        if self.start.StartFinish:
            self.start.place_forget()
            self.Menu.place(x=0, y=0)
        else:
            self.after(500, self.test)

    def resize(self, evt=None, forced=False):
        if forced is True:
            for child in self.winfo_children():
                child.resize()
        else:
            print(str(evt.widget))
            try:
                if str(evt.widget) == ".":
                    for child in self.winfo_children():
                        if child.winfo_ismapped():
                            child.resize()
                else:
                    evt.widget.resize()
            except AttributeError:
                pass
