from ..variables import Main, Camera


class RelicText:
    def __init__(self, text, color="grey"):
        self.rectangle = Main.relic_engine.create_rectangle(
            int(Camera.cam_x // 4),
            int(Main.y//1.5),
            int(Camera.cam_x * 1.75),
            int(Main.y),
            fill=color,
        )
        self.text = Main.relic_engine.create_text(
            Camera.cam_x,
            Main.y//1.25,
            font=("", 25)
        )
        self.write_text(text, 0)
        Main.relic_engine.unbind_all()
        Main.windows.bind("<Return>", self.finish)
        Main.relic_engine.reload_function["Relic-Gui-Text"] = self.reload
        Main.relic_engine.run()

    def write_text(self, text, number):
        if number <= len(list(text)):
            Main.relic_engine.itemconfigure(self.text, text="".join(list(text)[0:number]))
            Main.windows.after(50, lambda text_a=text, number_a=number+1: self.write_text(text_a, number_a))

    def finish(self, *evt):
        Main.relic_engine.delete(self.rectangle, self.text)
        Main.windows.unbind("<Return>")
        del Main.relic_engine.reload_function["Relic-Gui-Text"]
        Main.relic_engine.rebind_all()
        Main.relic_engine.turn = False

    def reload(self, *evt):
        Main.relic_engine.coords(
            self.rectangle,
            int(Camera.cam_x // 4),
            int(Main.y//1.5),
            int(Camera.cam_x * 1.75),
            int(Main.y)
        )
        Main.relic_engine.coords(self.text, Camera.cam_x, Main.y//1.25)
