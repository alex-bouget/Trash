from .WidgetElement.ButtonElement import ButtonElement


class GameElement(ButtonElement):
    def __init__(self, master, json, content_number):
        super().__init__(master, json, content_number)
