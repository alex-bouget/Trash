from tkinter import Canvas
from MariusLauncher.Element.Element import Element
from copy import deepcopy


class CanvasElement(Canvas, Element):
    def __init__(self, master, json, content_number):
        super().__init__(master)
        self.js = json
        self.root = self.nametowidget(".")
        self.content_number = deepcopy(content_number)
        self.resize()
