from tkinter import *


class Info(Canvas):
    def __init__(self, master, function):
        super().__init__(master)
        self.DeckName = StringVar()
        Entry(self, textvariable=self.DeckName).grid()
        Button(self, text="Save and quit", command=function).grid(row=1)
