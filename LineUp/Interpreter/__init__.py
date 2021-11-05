from .line import Line
from ..exit import Exit
from ..variable import Variable


class Interpreter:
    def __init__(self, module):
        self.global_variable = {
            "e": Exit(self),
            "v": Variable(self)
        }
        self.global_class = module

    def set_class(self, name, value):
        self.global_class[name] = value

    def execute(self, file):
        for i in open(file).read().split("\n"):
            Line(i).execute(self.global_variable, self.global_class)
