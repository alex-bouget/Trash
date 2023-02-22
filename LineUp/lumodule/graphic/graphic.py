from tkinter import Tk
from tkhtmlview import HTMLLabel

class Main(Exec):
    def __init__(self, global_variable, global_class):
        super(Main, self).__init__()
        self.global_variable = global_variable
        self.global_class = global_class
    
    def begin(self, *args):
        self.graphic = ["<!DOCTYPE html>", "<html>"]
    
    def end(self, *args):
        self.graphic.append("</html>")
    
    def view(self, *args):
        root = Tk()
        label = HTMLLabel(root, html="\n".join(self.graphic))
        label.pack()
        root.mainloop()
    
    def text(self, *args):
        self.graphic.append(args[0])
    
    def style(self, *args):
        self.graphic.append("style=\"")
        for i in args[0].decoded_line:
            self.graphic.append(i[1].decoded_line[0] +
                ": " + i[1].decoded_line[1]+";")
        self.graphic.append("\"")
    
    def win(self, *args):
        self.graphic.append("<"+args[0])
        for i in args[1].decoded_line:
            i[1].execute(self.global_variable, self.global_class)
        self.graphic.append(">")
        if (len(args) >= 3):
            for i in args[2].decoded_line:
                i[1].execute(self.global_variable, self.global_class)
        self.graphic.append("</"+args[0]+">")