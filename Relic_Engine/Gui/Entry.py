from ..variables import Main, Camera
from tkinter import StringVar


def RelicEntry():
    class Entry:
        def __init__(self):
            self.entry = StringVar()

        def place(self):
            self.rectangle = Main.relic_engine.create_rectangle(
                int(Camera.cam_x - Camera.cam_x // 1.25),
                int(Camera.cam_y - Camera.cam_y // 2),
                int(Camera.cam_x + Camera.cam_x // 1.25),
                int(Camera.cam_y + Camera.cam_y // 2),
                fill="blue"
            )
            self.label = Main.relic_engine.create_text(
                Camera.cam_x,
                Camera.cam_y,
                font=("", 25)
            )
            Main.relic_engine.reload_function["Relic-Gui-Entry"] = self.reload
            Main.relic_engine.unbind_all()
            Main.windows.bind("<Key>", self.enter_key)
            Main.relic_engine.run()
            return self.entry.get()

        def enter_key(self, evt):
            if evt.keysym == "Return":
                self.finish()
            else:
                if evt.keysym == "BackSpace":
                    r = list(self.entry.get())
                    del r[-1]
                    self.entry.set("".join(r))
                else:
                    self.entry.set(self.entry.get() + str(evt.char))
            Main.relic_engine.itemconfigure(self.label, text=self.entry.get())

        def finish(self):
            Main.relic_engine.delete(self.rectangle, self.label)
            del Main.relic_engine.reload_function["Relic-Gui-Entry"]
            Main.windows.unbind("<Key>")
            Main.relic_engine.rebind_all()
            Main.relic_engine.stop()

        def reload(self, *evt):
            Main.relic_engine.coords(
                self.rectangle,
                int(Camera.cam_x - Camera.cam_x // 1.25),
                int(Camera.cam_y - Camera.cam_y // 2),
                int(Camera.cam_x + Camera.cam_x // 1.25),
                int(Camera.cam_y + Camera.cam_y // 2),
            )
            Main.relic_engine.coords(
                self.label, Camera.cam_x, Camera.cam_y
            )
    return Entry().place()
