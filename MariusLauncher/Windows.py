from tkinter import Tk


class Windows(Tk):
    def __init__(self):
        super().__init__()
        self.old_h = 0
        self.old_w = 0
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
                        for child in self.winfo_children():
                            if child.winfo_ismapped():
                                child.resize()
                        self.old_h = self.winfo_height()
                        self.old_w = self.winfo_width()
                else:
                    evt.widget.resize()
            except AttributeError:
                pass
