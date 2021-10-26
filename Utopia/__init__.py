from .lib import UtopiaLib
from .window import Game
from tkinter import *
import logging


class Utopia(Tk):
    def __init__(self, principal_server, battle_server, folder, version):
        super().__init__()
        self.configure(width=720, height=480)
        self.Lib = UtopiaLib(principal_server, battle_server, folder, "fr", version)
        self.battle_server = battle_server+"Battle/B1/"
        self.Game = Game(self, self.Lib, self.battle_server)
        self.old_w = 0
        self.old_h = 0
        self.tk_log = logging.getLogger("Tkinter")
        self.bind("<Configure>", self.resize)
        self.resize(forced=True)

    def resize(self, evt=None, forced=False):
        if forced is True:
            self.old_w = self.winfo_width()
            self.old_h = self.winfo_height()
            for child in self.winfo_children():
                child.resize()
        else:
            try:
                if str(evt.widget) == ".":
                    if self.old_w != self.winfo_width() or self.old_h != self.winfo_height():
                        self.tk_log.debug("resize all window")
                        for child in self.winfo_children():
                            if child.winfo_ismapped():
                                child.resize()
                        self.old_h = self.winfo_height()
                        self.old_w = self.winfo_width()
                else:
                    self.tk_log.debug("resize " + str(evt.widget))
                    evt.widget.resize()
            except AttributeError:
                pass
