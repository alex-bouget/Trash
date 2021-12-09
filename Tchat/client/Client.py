import Windows
from tkinter import *

class Client(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.configure(height=480, width=720)
    def start(self):
        Windows.connect_to_server(self)._place(x=360, y=240, anchor=CENTER)
        Windows.discussion(self).place(x=0, y=0)
        self.mainloop()

if __name__ == "__main__":
    Client().start()