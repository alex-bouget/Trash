from tkinter import Tk, BOTH, YES, Canvas
import time


class Relic(Canvas):
    def __init__(self):
        super().__init__(Tk())
        self.old_w = 0
        self.old_h = 0
        self.pack(fill=BOTH, expand=YES)
        self.reload_function = {}
        self.turn = True

    def bind(self):
        pass

    def unbind(self):
        pass

    def unbind_all(self):
        pass

    def rebind_all(self):
        pass

    def change_width(self):
        pass

    def change_height(self):
        pass

    def resize(self):
        pass

    def reload(self, evt=None, forced=False):
        if forced is True:
            self.old_h = self.master.winfo_height()-4
            self.old_w = self.master.winfo_width()-4
            self.configure(width=self.master.winfo_width() - 4,
                           height=self.master.winfo_height() - 4
                           )
            for function in self.reload_function.values():
                function()
        else:
            try:
                if str(evt.widget) == ".!relic":
                    if self.old_w != self.winfo_width() or self.old_h != self.winfo_height():
                        self.resize(width=self.master.winfo_width()-4,
                                    height=self.master.winfo_height()-4)
                        self.old_h = self.master.winfo_height()-4
                        self.old_w = self.master.winfo_width()-4
                        for function in self.reload_function.values():
                            function()
            except AttributeError:
                pass

    def run(self):
        self.master.bind("<Configure>", self.reload)
        while self.turn:
            self.update()
            time.sleep(.00001)
        self.turn = True

    def stop(self):
        self.turn = False
