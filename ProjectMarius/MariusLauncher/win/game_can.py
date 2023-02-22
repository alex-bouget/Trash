from tkinter import Canvas, Label, Button


class GameCanvas(Canvas):
    def __init__(self, root, name, button_value, command):
        super(GameCanvas, self).__init__(root)
        self.name = Label(self, text=name)
        self.button = Button(self, text=button_value, command=command)

    def reload(self):
        self.name.grid(row=0, column=0)
        self.middle.grid(row=0, column=1)
        self.button.grid(row=0, column=2)